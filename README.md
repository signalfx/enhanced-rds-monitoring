# SignalFx Enhanced RDS Monitoring Integration

Source code for an AWS Lambda blueprint that allows users to send enhanced RDS
metrics to the SignalFx platform.

## Installation/Configuration

### Enable Enhanced Monitoring

On your AWS account, go to the RDS dashboard, then go to the Instances view.
From here, you can select whichever RDS instances you want to monitor. For such
an instance, select it, go to the Instance Actions tab, and select Modify. The
enhanced monitoring option is at the bottom of the list of possible changes.
You must either select a role, or allow AWS to automatically create a role with
the necessary permissions. You must also select your resolution (frequency of
reporting). After you confirm, there will be a short configuration period,
after which your instance will automatically report its metrics to a log group
called RDSOSMetrics which will be created for the purpose by AWS.

### Set up the Lambda

#### Create an encryption key

The next step is to set up the Lambda script that will parse the logs, format
the data, and send it to the SignalFx ingest API. To do this you will need an
encryption key to use to encrypt your SignalFx access token.

#### Select blueprint and trigger

When you begin creating the function, you will want to select the SignalFx
blueprint (just search for signalfx in the search bar). After that you will be
prompted to select a trigger for the function, which is just the source of the
data stream. Select CloudWatch Logs, select RDSOSMetrics from the Log Group
dropdown, and choose a filter name (the name is not important). Leave
everything else blank.

#### Configure function

Create a name for the function (this is how the function will appear on your
Lambda dashboard). Leave Python 2.7 as the selected runtime. Under the Lambda
function code window, select the checkbox under Enable encryption helpers.
Select the encryption key you created from the dropdown. Under Environment
variables, create a new one with the key *access_token* and paste in your
SignalFx access token as the value. Click 'Encrypt' on that row to encrypt the
token. Hereafter, only the encrypted version of the token will be stored in the
Lambda configuration.

#### Select desired metric groups

This step is only necessary if you don't care about some of the metric groups
and don't need them reported (see the RDS Enhanced Monitoring page
[here](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)
for documentation). Once you know what you want, create a new environment
variable with the key *groups* (for a list of the metric groups desired) or
*groups_out* for the groups you want excluded. ONLY CREATE ONE OF THESE: if you
create both, groups_out will be ignored.

#### Create execution role

Leave the Handler field alone. On the Role dropdown, select create new role
from template, and give it a descriptive name. Under Policy templates, you
should already see `KMS decryption permissions`, which will be sufficient.



And that's it! The next page will allow you to review the configurations you
just set before creating the function. Once you're satisfied with the settings,
create the function! You should be redirected to your list of Lambda functions,
and the new one should appear. All that you need to do now is click on the
function name, select the Triggers tab, and enable the CloudWatch Logs trigger.
The metrics will be reported to SignalFx at the interval you selected for your
RDS instances.