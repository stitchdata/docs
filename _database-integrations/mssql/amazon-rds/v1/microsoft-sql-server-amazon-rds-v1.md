---
title: Amazon Microsoft SQL Server RDS (v1)
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-rds-microsoft-sql-server/v1
summary: "Connect and replicate data from your Amazon Microsoft SQL Server RDS using Stitch's Microsoft SQL Server integration."
show-in-menus: false

key: "amazon-mssql-rds-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "sql-server-rds"
display_name: "Amazon Microsoft SQL Server RDS"

hosting-type: "amazon"

this-version: "1"

driver: "7.2.1.jre8"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

singer: true
repo-url: https://github.com/singer-io/tap-mssql
certified: true
setup-name: "Microsoft SQL Server"

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"

# Stitch features
api-type: "platform.mssql"
versions: "2012 through 2017"
ssh: true
ssl: true

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

log-based-replication-minimum-version: "2012"
log-based-replication-master-instance: true
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Privileges in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: "**Privileges in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."

  - item: "**A database running {{ integration.display_name }} version {{ page.versions }}.** {{ integration.display_name }} 2012 is the miminum version that Stitch supports for this type of integration."

  - item: |
      **If using Log-based Incremental Replication**, you'll need:

      - **The `ALTER DATABASE` privilege in Microsoft SQL Server.** This is required to complete the setup for Log-based Incremental Replication.

## Based on this AWS doc, enabling mixed mode auth shouldn't be necessary:
## https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Enable Log-based Incremental Replication with Change Tracking"
    anchor: "enable-log-based-incremental-change-tracking"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#db-user)." %}
      
      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      {% for substep in step.substeps %}
      - [Step 2.{{ forloop.index }}: {{ substep.title }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Verify database compatibility"
        anchor: "verify-database-compatibility"
        content: |
          {% include integrations/databases/setup/binlog/mssql-enable-change-tracking.html type="verify-compatibility" %}

      - title: "Enable change tracking for the database"
        anchor: "enable-database-change-tracking"
        content: |
          {% include integrations/databases/setup/binlog/mssql-enable-change-tracking.html type="enable-database" %}

      - title: "Enable change tracking for tables"
        anchor: "enable-table-change-tracking"
        content: |
          {% include integrations/databases/setup/binlog/mssql-enable-change-tracking.html type="enable-table" %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Locate RDS connection details in AWS"
        anchor: "locating-rds-database-details"
        content: |
          {% include shared/connection-details/amazon.html %}

      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSH connection details"
        anchor: "ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" %}
      
      - title: "Define Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#create-replication-schedule)." %}

          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}
      
      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

      - title: "Save the integration"
        anchor: "save-integration"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/databases/setup/syncing.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}
