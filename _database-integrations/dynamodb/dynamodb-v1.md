---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/databases/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Amazon DynamoDB (v1)
keywords: amazon-dynamodb, database integration, etl amazon-dynamodb, amazon-dynamodb etl
permalink: /integrations/databases/amazon-dynamodb
summary: "Connect and replicate data from your Amazon DynamoDB database using Stitch's Amazon DynamoDB integration."

show-in-menus: true
key: "dynamodb-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "amazon-dynamodb"
display_name: "Amazon DynamoDB"

singer: true
tap-name: "tap-dynamodb"
repo-url: "https://github.com/singer-io/tap-dynamodb"
status-url: "https://status.aws.amazon.com/"

this-version: "1"

hosting-type: "amazon"

driver: |
  [Boto 3 1.9.57](https://boto3.amazonaws.com/v1/documentation/api/1.9.57/index.html){:target="new"}


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.driver | flatify | strip }}. [TODO]


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

frequency: "1 hour"
tier: "Free"
db-type: "dynamodb"

api-type: "platform.dynamodb"

## Stitch features

versions: "n/a"
ssh: false
ssl: false

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: true
log-based-replication-read-replica: "n/a"

## Other Replication Methods

key-based-incremental-replication: false
full-table-replication: true

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: |
      **Permissions in AWS Identity Access Management (IAM) that allow you to create policies, create roles, and attach policies to roles**. This is required to grant Stitch authorization to {{ integration.display_name }}.
  - item: |
      **If using Log-based Incremental replication, streams must be enabled in {{ integration.display_name }} for every table you want to replicate using this method.** Additionally, each stream must use the `New Image` or `New and Old Images` option in AWS. Refer to the [Replication](#log-based-incremental-replication-details) section for more info.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Retrieve your Amazon Web Services account ID"
    anchor: "retrieve-aws-account-id"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="retrieve-account-id" %}

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#connect-stitch)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      For every table you want to replicate using Log-based Incremental replication, you'll need to enable {{ integration.display_name }} streams. Each stream must use the `New Image` or `New and Old Images` option in AWS or replication will be unsuccessful.

      Refer to [Amazon's documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html#Streams.Enabling){:target="new"} for instructions on enabling and configuring streams.
      
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "connect-stitch"
    content: |
      {% include shared/database-connection-settings.html type="general" %}

  - title: "Create a replication schedule"
    anchor: "create-replication-schedule"
    content: |
      {% capture notice %}
      **Note**: If using Log-based Incremental Replication, keep in mind that Amazon purges {{ integration.display_name }} streams after 24 hours. To ensure you don't lose data, set the integration's Replication Frequency to an interval less than 24 hours. For example: 12 hours.

      If Stitch identifies a stream that has aged out, Stitch will automatically reset the table and queue a full re-replication.
      {% endcapture %}

      {% include integrations/shared-setup/replication-frequency.html notice=notice %}

  - title: "Grant access to {{ integration.display_name }} using AWS IAM"
    anchor: "grant-access-bucket-iam"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="aws-iam-access-intro" %}

    substeps:
      - title: "Create an IAM policy"
        anchor: "create-iam-policy"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="create-iam-policy" %}
          
      - title: "Create an IAM role for Stitch"
        anchor: "create-stitch-iam-role"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="create-stitch-iam-role" %}

      - title: "Check and save the connection in Stitch"
        anchor: "check-save-stitch-connection"
        content: |
          {% include integrations/shared-setup/aws-s3-iam-setup.html type="check-and-save" %}

  - title: "Select data to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/databases/setup/syncing.html %}


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      {% for section in integration.replication-sections %}
      {% if section.title %}
      - [{{ section.summary | flatify }}](#{{ section.anchor }})
      {% endif %}
      {% endfor %}

  - title: "Log-based Incremental Replication"
    anchor: "log-based-incremental-replication-details"
    summary: "Details about Log-based Incremental Replication via {{ integration.display_name }} streams"
    content: |
      Stitch's {{ integration.display_name }} integration uses [{{ integration.display_name }} Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html){:target="new"} to perform Log-based Incremental Replication. To use Log-based Incremental Replication, streams must be enabled on every table in {{ integration.display_name }} you want to replicate using this Replication Method. 

      Refer to [Amazon's documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html#Streams.Enabling){:target="new"} for instructions on enabling streams for {{ integration.display_name }} tables.

      **Note**: The **Manage Stream** option must be one of the following, or replication will be unsuccessful:

        - `New Image`
        - `New and old images`
 
      {% include note.html type="single-line" content="**Note**: DynamoDB streams are purged after 24 hours. To ensure you don't lose data, set the integration's Replication Frequency to an interval less than 24 hours. For example: 12 hours. If Stitch identifies a stream that has aged out, Stitch will automatically reset the table and queue a full re-replication." %}

  - title: "Full Table Replication"
    anchor: "full-table-replication-details"
    summary: "Details about Full Table Replication using scans and eventually consistent reads"
    content: |
      To perform Full Table Replications with Stitch's {{ integration.display_name }} integration, Stitch uses scans to return data. A scan returns data by accessing all items within a table. As queries require you to specify the hash key (Primary Key), Stitch uses scans to simplify setup and replication. For more information about scans, click [here](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html){:target="new"}.

      Additionally, Stitch's {{ integration.display_name }} integration only uses eventually consistent reads from your selected {{ integration.display_name }} tables. **Note**: This means that you will not see all of your recent data right away due to a delay from Amazon, but it will eventually catch up and return the latest records. For more information on {{ integration.display_name }} read consistency, refer to [Amazon's documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html){:target="new"}.
---
{% assign integration = page %}
{% include misc/data-files.html %}
{% include misc/icons.html %}