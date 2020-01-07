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

title: Amazon DynamoDB
keywords: amazon-dynamodb, database integration, etl amazon-dynamodb, amazon-dynamodb etl
permalink: /integrations/databases/amazon-dynamodb
summary: "Connect and replicate data from your Amazon DynamoDB database using Stitch's Amazon DynamoDB integration."

show-in-menus: true
key: "amazon-dynamodb-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "amazon_dynamodb"
display_name: "Amazon DynamoDB"

singer: true
tap-name: "tap-dynamodb"
repo-url: "https://github.com/singer-io/tap-dynamodb"
status-url: "https://status.aws.amazon.com/"

this-version: "1.0"

hosting-type: "amazon" ## amazon, microsoft, google, etc.

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
port: ## Database's default port - ex: 3306
db-type: "dynamodb"

## Stitch features

versions: "n/a"
ssh: false
ssl: false

## General replication features

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: false

## Replication methods

define-replication-methods: false

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: false

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **An Amazon Web Services (AWS) account.** Signing up is free - [click here](https://aws.amazon.com){:target="new"} or go to `https://aws.amazon.com` to create an account if you don't have one already.
  - item: |
      **Permissions in AWS Identity Access Management (IAM) that allow you to create policies, create roles, and attach policies to roles**. This is required to grant Stitch authorization to your DynamoDB bucket.

# File requirements are in: _data/taps/extraction/file-systems/file-requirements.yml
  - item: |
      **Files that adhere to Stitch's file requirements**:

      {{ site.data.taps.extraction.file-systems.file-requirements.support-table | flatify }}



# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Retrieve your Amazon Web Services account ID"
    anchor: "retrieve-aws-account-id"
    content: |
      {% include integrations/shared-setup/aws-s3-iam-setup.html type="retrieve-account-id" %}
      
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include shared/database-connection-settings.html type="general" %}


  - title: "Define the historical sync"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/shared-setup/configure-table-settings-file-server.html type="define-historical-sync" %}

  - title: "Create a replication schedule"
    anchor: "create-replication-schedule"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Grant access to your bucket using AWS IAM"
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
  - title: "Log-based Incremental Replication"
    anchor: "log-based-incremental-replication"
    summary: "Details about Log-based Incremental Replication via DynamoDB streams."
    content: |
      This integration supports Full Table and Log-based replication. Log-based replication is done through DynamoDB streams, not Amazon Kinesis streams. In order to use streams, they must be enabled on the tables created in DynamoDB. When in your AWS account, go to the `manage streams` section and choose `New Image` or `New and old images`. If one of these aren't selected, the integration will fail during sync. This is handled on a table-by-table basis, so you must enable streams on each.
 
      In AWS, streams are only retained for 24 hours, so when setting up a log-based replication, be sure to set the replication frequency to a time less than 24 hours. If not, you will be at risk of your data aging out.

---
{% assign integration = page %}
{% include misc/data-files.html %}
{% include misc/icons.html %}