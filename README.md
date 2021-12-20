>ℹ️&nbsp;&nbsp;SignalFx was acquired by Splunk in October 2019. See [Splunk SignalFx](https://www.splunk.com/en_us/investor-relations/acquisitions/signalfx.html) for more information.

# SignalFx Enhanced RDS Monitoring Integration

These instructions describe the steps to deploy the Lambda function to
parse and report your Enhanced RDS metrics to SignalFx. You can deploy the function either from the Serverless Application Repository (which is recommended) or by building and deploying from source. 

## Installation
Choose a deployment method and follow the steps below to encrypt your SignalFx access token, customize the metrics sent to SignalFx, and create and deploy the Lamda function.

### Prerequisites
Before you begin, you must enable the Enhanced Monitoring option for the RDS instances you want to monitor using this integration. [Click here for instructions on enabling Enhanced Monitoring](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html).

* [Deploying through the Serverless Application Repository](#deploying-through-the-serverless-application-repository)
* [Building from source](#building-from-source)
* [Metrics collected by this integration](#metric-groups-collected-by-this-integration)

#### If you are upgrading from version 0.1.0 (Python 2.7) to version 0.2.0 (Python 3.x)
If you are upgrading to version 0.2.0, ensure that the AWS Lambda handler is set to `enhanced_rds.lambda_script.lambda_handler`.

#### Encrypting your SignalFx access token
The Lambda function uses your SignalFx access token to send metrics to SignalFx, as an environment variable to the function. While Lambda encrypts all environment variables at rest and decrypts them upon invocation, AWS recommends that all sensitive information such as access tokens be encrypted using a KMS key before function deployment, and decrypted at runtime within the code.

Both Serverless Application Repository and build from source deployment procedures below include instructions for using either an encrypted or non-encrypted access token.

## Deploying through the Serverless Application Repository
Deploying through the Serverless Application Repository is a four-step process if you manually encrypt your access token, and a three-step process otherwise:

### 1. Set up an encryption key and encrypt your access token (if desired)
Start with this step only if you chose to manually encrypt your access token.
Either create a new KMS encryption key or select a preexisting one. **The key
must be in the same availability zone as the RDS instances you are
monitoring.** You can create and manage encryption keys from IAM in the AWS
management console. Documentation about KMS encryption from the CLI can be found
[here](http://docs.aws.amazon.com/cli/latest/reference/kms/encrypt.html). Make sure you have access to the cipher text output by the encryption as well as the key ID of the encryption key you used.

### 2. Create the Lambda function
Click `Create Function` from the list of Lambda functions in your AWS console.
Make sure you are in the intended availability zone. Select the
`Serverless Application Repository` option in the upper right corner.
Search for `signalfx rds` and choose the appropriate entry based on whether you
encrypted your access token.

To access the templates directly, find the template for encrypted access
tokens [here](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-2:254067382080:applications~signalfx-enhanced-rds-metrics-encrypted).
The template for non-encrypted access tokens is [here](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-2:254067382080:applications~signalfx-enhanced-rds-metrics).

### 3. Fill out application parameters
Under `Configure application parameters`, choose a name for your function and fill out the fields accordingly.

**Parameters for the template using encrypted access tokens**
- `EncryptedSignalFxAuthToken`: The Ciphertext blob output from your encryption of your SignalFx organization's access token
- `KeyId`: The key ID of your KMS encryption key; it is the last section of the key's ARN.
- `SelectedMetricGroups`: The metric groups you wish to send. Enter `All` if you want all available metrics. Otherwise, list the names of desired metric groups, spelled exactly as they are below, separated by single spaces. See [Metrics collected by this integration](#metric-groups-collected-by-this-integration) for options.
- `Realm`: Your SignalFx Realm. To determine what realm you are in, check your profile page in the SignalFx web application. Default: `us0`.

**Parameters for the template using non-encrypted access tokens**
- `SignalFxAuthToken`: Your SignalFx organization's access token
- `SelectedMetricGroups`: The metric groups you wish to send. Enter `All` if you want all available metrics. Otherwise, list the names of desired metric groups, spelled exactly as they are below, separated by single spaces. See [Metrics collected by this integration](#metric-groups-collected-by-this-integration) for options.
- `Realm`: Your SignalFx realm. To determine what realm you are in, check your profile page in the SignalFx web application. Default: `us0`.

#### SignalFx realms defined:
A realm is a self-contained deployment of SignalFx in which your organization is hosted.
Different realms have different API endpoints.
For example, the endpoint for sending data in the us1 realm is ingest.us1.signalfx.com,
and the endpoint for the eu0 realm is ingest.eu0.signalfx.com. If you try to send data to the incorrect realm,
your access token will be denied.

### 4. Deploy the function and configure the trigger
Click `Deploy`. After the function has finished deploying, navigate to the
function's main page.

Under the `Configuration` tab, scroll through the list on the left and
select CloudWatch Logs as the source of the trigger. You can then configure the trigger:

* Select `RDSOSMetrics` as the log group.
* Choose an appropriate name for the filter, and leave the filter pattern
blank.
* Make sure the `Enabled` switch is activated.

Click `Add`, then click `Save` in the upper right corner.

That's it! Your metrics are on the way to SignalFx ingest!

## Building from source

### 1. Set up the execution role
The execution role just needs basic Lambda execution permissions and KMS
decrypt permissions (if you wish to encrypt your SignalFx access token). If you
don't want to create one, you can select from a list of templates when you
create the lambda function.

### 2. Set up an encryption key and encrypt access token
Only follow this step if you chose to encrypt your access token. Either create
a new KMS encryption key or select a preexisting one. **The key must be in the
same availability zone as the RDS instances you are monitoring.** You can
create and manage encryption keys from IAM in the AWS management console.
Documentation on KMS encryption from the CLI can be found
[here](http://docs.aws.amazon.com/cli/latest/reference/kms/encrypt.html).
Make sure you have access to the cipher text output by the encryption as well
as the key id of the encryption key you used.

### 3. Clone the source repo and build the deployment package
You can find the repo
[here](https://github.com/signalfx/enhanced-rds-monitoring).
After you have cloned the repo, do the following:
```
$ cd enhanced-rds-monitoring
$ ./build.sh
```
The package will be named `enhanced_rds.zip`. This is the file to upload for the Lambda.

### 4. Create and configure the Lambda function
From the Lambda creation screen, make sure you have selected
`Build from scratch`. Select a name for your function. For `Runtime` select
`Python3.8` (although `Python3.6` and `Python3.7` are also supported). For the execution role, either select the role you want to use or
select `Create from Template` and add KMS decrypt permissions if necessary. You
will also need to choose a name for the role.

For subsequent tabs, follow the instructions below.

#### Designer
The only thing to be done here is to set up the trigger from CloudWatch Logs:
1. Select CloudWatch Logs from the list on the left. A section labelled
`Configure triggers` is displayed. For the `Log group` field, select
`RDSOSMetrics`. 
2. Choose a filter name, but leave the filter
pattern blank. You can disable the trigger to start if you want (though you
will need to manually enable it later to start sending metrics)
3. Click Add.

#### Function code
Once the function is created you can change the configurations: Upload the ZIP
file containing the deployment package, then change the text in `Handler` to be
`enhanced_rds.lambda_script.lambda_handler`.

#### Environment variables

First create an environment variable called `groups`. This will store the list of metric groups to be reported. To report all available metrics, enter `All`. Otherwise, list the names of desired metric groups, spelled exactly as above, separated by single spaces.

Next, create a variable to store your SignalFx access token. Create a field called `encrypted_access_token` to store an encrypted SignalFx access token, or simply `access_token` to store an unencrypted token. Paste your access token into the value field.

If you use `encrypted_access_token`, follow the steps below to encrypt it:
  * Under `Encryption configuration`, check the box to `Enable helpers for encryption in transit`. A new field will appear labelled `KMS key to encrypt in transit`.
  * Select the encryption key you wish to use from the dropdown. A button labelled `Encrypt` will appear next to your environment variables.
  * Click the `Encrypt` button next to `encrypted_access_token` once. The value will be replaced by a Ciphertext blob.

If you are not in the `us0` realm in SignalFx, you need to specify a `realm` environment variable. To determine which realm you are in, check your profile page in the SignalFx web application.

#### Basic settings
Under basic settings, set `Timeout` to `0 min 5 sec`.

Click `Save`, and once the trigger is enabled, your function will start sending
your metrics to SignalFx!

## Metric groups collected by this integration

The following metric groups are collected by this integration. To collect all of them, use `All` at configuration time. To select a subset, choose metric groups by name. You can find documentation on the available metrics
[here](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html).

**Metric Groups (except for SQLServer)**
- cpuUtilization
- diskIO
- fileSys
- loadAverageMinute
- memory
- network
- swap
- tasks
- OSprocesses*
- RDSprocesses*

**SQLServer Metric Groups**
- cpuUtilization
- disks
- memory
- network
- system
- OSprocesses*
- RDSprocesses*

\* Process-based metric group added by SignalFx, does not appear in AWS
documentation.
