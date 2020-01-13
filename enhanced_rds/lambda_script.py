# Copyright (C) 2017-2018 SignalFx, Inc. All rights reserved.
# Copyright (C) 2019-2020 Splunk, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import boto3
import gzip
import json
import base64
import io
from signalfx import SignalFx
from datetime import datetime
from enhanced_rds.metric_maps import METRICS_MICROSOFT_DIMS,\
    METRICS_MICROSOFT, \
    PROCESS_METRICS_MICROSOFT, \
    METRICS, PROCESS_METRICS,\
    METRICS_AURORA_DIMS, \
    METRICS_DIMS


def decrypt_token(encrypted_key):
    """
    Uses the KMS client to decrypt the customer's access token.

    :param encrypted_key: The encrypted access token
    :return: The decrypted access token
    """

    kms = boto3.client('kms')
    return kms.decrypt(
        CiphertextBlob=base64.b64decode(encrypted_key)
    )['Plaintext']


def get_access_token():
    """
    Determines whether the access token provided is encrypted and returns the
    plain text access token.

    :return: The plain text access token
    """

    if 'encrypted_access_token' in os.environ.keys():
        return decrypt_token(os.environ.get('encrypted_access_token'))
    else:
        return os.environ.get('access_token')


def get_realm():
    """
    Return the realm from an environment variable, or default to us0

    :return: String for a realm
    """

    if 'realm' in os.environ.keys():
        return os.environ.get('realm')
    else:
        return "us0"


def parse_timestamp(timestamp):
    """
    Takes a timestamp string and returns it as an integer of the number of
    milliseconds since epoch.

    :param timestamp: String in RfC3339 format representing a timestamp.
    :return: The timestamp in milliseconds (int).
    """

    datetime_values = re.split(r'\D', timestamp)
    datetime_values.remove('')
    datetime_values = map(lambda val: int(val), datetime_values)

    dt_timestamp = datetime(*datetime_values)
    epoch = datetime.utcfromtimestamp(0)

    return int((dt_timestamp - epoch).total_seconds() * 1000)


def create_metric_entry(group, metric, value, timestamp, inst_rsrc_id,
                        aws_unique_id, engine, extra_dims=None):
    """
    Builds a dict representing a single point of a metric, ready to be
    reported.

    :param group: The prefix of the metric name. (unicode)
    :param metric: The specific metric name (unicode)
    :param value: The value of the metric (float)
    :param timestamp: The timestamp in RfC3339 format (string)
    :param inst_rsrc_id: The region-unique identifier for the db instance
                         provided by RDS (string)
    :param aws_unique_id: Internally-used identifier containing service,
                          region, instance id, and AWS owner id (string)
    :param engine: The db engine type (e.g. MySQL, Postgres, etc.) (string)
    :param extra_dims: A dict mapping a metric group to which of its values
                       need to be used as additional dimensions on each metric
                       (dict)
    :return: A dict in the format of a metric entry for the SignalFx Python
             client
    """

    entry = {
        'metric': group + '.' + metric,
        'value': value,
        'timestamp': parse_timestamp(timestamp),
        'dimensions': {
            'instanceResourceID': inst_rsrc_id,
            'AWSUniqueId': aws_unique_id,
            'Namespace': 'AWS/RDS',
            'EngineName': engine
        }
    }

    # Add extra dimensions to identify instances of metric groups when
    # necessary e.g. multiple file systems
    if extra_dims:
        entry['dimensions'].update(extra_dims)

    return entry


def parse_process_overviews(process_list):
    """
    Extracts the two process list items that provide overview on OS and RDS
    processes as groups within the instance, so they can be used to create
    metrics under those two groups.

    :param process_list: The process list as delivered by CloudWatch Logs,
                         which is a list of metrics for every active process
                         within the instance as well as two process items with
                         overview info for OS and RDS processes (list of dicts)
    :return: A dict mapping the group name to the dict of information for that
             group (dict of dicts)
    """

    return dict(
        (process_info[u'name'].replace(u' ', u''), process_info)
        for process_info in process_list
        if process_info[u'name'] in [u'OS processes', u'RDS processes'])


def extract_region(function_arn):
    """
    Extracts the AZ from the Lambda's ARN

    :param function_arn: The ARN of this Lambda (string)
    :return: The AZ (string)
    """
    return function_arn.split(':')[3]


def parse_logs(owner_id, function_arn, log_dict, desired_metric_list,
               process_metric_list, extra_dims_map):
    """
    Takes in information from CloudWatch Logs, as well as customer-specific
    configuration, and builds the list of entry dicts for a single payload.

    :param owner_id: The AWS owner id (string)
    :param function_arn: The ARN of the Lambda function (string)
    :param log_dict: A map of all the metric information for this payload
                     (dict)
    :param desired_metric_list: A list of the metric groups desired by the
                                customer (list)
    :param process_metric_list: A list of the process metrics available for the
                                db engine used by this instance (list)
    :param extra_dims_map: A dict mapping a metric group to which of its values
                           need to be used as additional dimensions on each
                           metric (dict)
    :return: A list of the entry dicts for this payload (list of dicts)
    """

    instance_id = log_dict['instanceID']
    instance_resource_id = log_dict['instanceResourceID']
    timestamp = log_dict['timestamp']
    engine = log_dict['engine']

    # Extract the AWS region in which this Lambda is running from the Lambda
    # ARN
    region = extract_region(function_arn)

    # Build the AWSUniqueId dimension for internal use
    aws_unique_id = '_'.join(['rds', instance_id, region, owner_id])

    # Pull the RDS and OS process overview info from the process list
    process_metrics = parse_process_overviews(log_dict[u'processList'])

    metric_entries = []
    for group in desired_metric_list:
        if group in process_metrics.keys():
            # Grab the 'OSprocesses' or 'RDSprocesses' metrics
            metric_group = process_metrics[group]
        else:
            metric_group = log_dict[group]

        if group in extra_dims_map.keys():
            # The current metric group may have multiple 'instances' e.g. a set
            # of metrics for each file system
            for group_instance in metric_group:
                # Contains the values that will be the dimensions to
                # differentiate each metric group 'instance'
                extra_dims = {dim: group_instance[dim]
                              for dim in extra_dims_map[group]}

                for metric in [name for name in group_instance.keys()
                               if name not in extra_dims.keys()]:
                    metric_entries.append(create_metric_entry(
                        group,
                        metric,
                        group_instance[metric],
                        timestamp,
                        instance_resource_id,
                        aws_unique_id,
                        engine,
                        extra_dims
                    ))
        else:
            if 'name' in metric_group.keys():
                # Only the process metrics have 'name' attributes
                metric_keys = process_metric_list
            else:
                metric_keys = metric_group.keys()

            for metric in metric_keys:
                metric_entries.append(create_metric_entry(
                    group,
                    metric,
                    metric_group[metric],
                    timestamp,
                    instance_resource_id,
                    aws_unique_id,
                    engine
                ))

    return metric_entries


def parse_process_data(process_list):
    """
    Extracts information from the process list to send as events.

    :param process_list: The list of dicts for each process on the db instance
                         (list of dicts)
    :return: A b64 encoded, gzip compressed JSON object of the process lists,
             formatted as required by ingest (string)
    """

    processes_data = {}

    for process in [prc for prc in process_list if prc['id'] != 0]:
        process_metrics = [
            'root',  # userId
            20,  # priority
            0,  # nice value
            process['vss'],  # virtual memory size
            process['rss'],  # resident memory size
            0,  # shared memory size
            'R',  # process status
            process['cpuUsedPc'],  # % CPU
            float(process['memoryUsedPc']) / process['rss'],  # % MEM
            '0:00.00',  # CPU time
            process['name']  # Process name
        ]
        processes_data[process['id']] = process_metrics

    # Serialize to JSON format, encode in base64, and use gzip compression
    data_as_json = json.dumps(processes_data)

    compressed_data = io.StringIO()
    with gzip.GzipFile(fileobj=compressed_data, mode='w') as f:
        f.write(data_as_json)

    return base64.b64encode(compressed_data.getvalue())


def parse_payload(payload):
    """
    Takes in the raw payload from CloudWatch Logs, extracts the owner id and
    the message, which is decoded, decompressed, and parsed into a Python dict.

    :param payload: The raw message delivered from CloudWatch (dict)
    :return: A tuple of the AWS owner id and a dict as parsed from the JSON
             object in the payload (string, dict)
    """

    message_data = payload['awslogs']['data']
    decoded_data = base64.b64decode(message_data)

    compressed_data = io.BytesIO(decoded_data)
    with gzip.GzipFile(fileobj=compressed_data, mode='r') as f:
        decompressed_data = f.read()

    log_event = json.loads(decompressed_data)
    owner_id = log_event['owner']
    metrics_as_json = log_event['logEvents'][0]['message']
    return owner_id, json.loads(metrics_as_json)


def pull_metric_names(engine):
    """
    Sets the necessary configurations based on the db engine used by this
    instance so we look for the proper keys.

    :param engine: The db engine type (string)
    :return: A tuple of a list of the desired metric groups, a list of the
             metrics available for the process overviews, and a dict containing
             information about which groups need extra dimensions
             (list, list, dict)
    """

    # Check engine type
    if engine.lower() == 'sqlserver':
        full_metrics_list = METRICS_MICROSOFT
        process_overview_metrics = PROCESS_METRICS_MICROSOFT
        extra_dims_map = METRICS_MICROSOFT_DIMS
    elif engine.lower().startswith('aurora'):
        full_metrics_list = METRICS
        process_overview_metrics = PROCESS_METRICS
        extra_dims_map = METRICS_AURORA_DIMS
    else:
        full_metrics_list = METRICS
        process_overview_metrics = PROCESS_METRICS
        extra_dims_map = METRICS_DIMS

    if os.environ['groups'] != 'All':
        # Pick user-selected metrics
        desired_metrics = [str(group, 'utf-8') for group
                           in os.environ.get('groups').split(' ')]
        metric_list = [group for group in full_metrics_list
                       if group in desired_metrics]
    else:
        # DEFAULT: Take all metrics
        metric_list = full_metrics_list

    return metric_list, process_overview_metrics, extra_dims_map


def lambda_handler(event, context):
    """
    Entry point for the lambda function. Processes the input, builds the metric
    entries and process events, and sends them to ingest.

    :param event: The message from CloudWatch Logs (dict)
    :param context: The context object, containing information about the Lambda
                    function itself
    :return: None
    """

    access_token = get_access_token()
    realm = get_realm()
    api_url = 'https://api.%s.signalfx.com' % realm
    ingest_url = 'https://ingest.%s.signalfx.com' % realm

    with SignalFx(api_endpoint=api_url,
                  ingest_endpoint=ingest_url).ingest(access_token) as ingest:

        # Pull out, decompress, and decode the message from CloudWatch Logs
        owner_id, log_dict = parse_payload(event)

        # Creates the appropriate lists/dicts of desired metrics
        desired_metrics_info = pull_metric_names(log_dict['engine'])

        # Reads through the payload from logs and creates the desired metric
        # objects
        function_arn = context.invoked_function_arn
        metric_entries = parse_logs(owner_id, function_arn, log_dict,
                                    *desired_metrics_info)

        # Send the metrics to ingest
        ingest.send(gauges=metric_entries)
