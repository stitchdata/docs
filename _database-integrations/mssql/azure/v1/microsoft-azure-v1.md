---
title: Microsoft Azure SQL Database (v1)
keywords: microsoft azure, azure, database integration, etl azure, azure etl
permalink: /integrations/databases/microsoft-azure/v1
summary: "Connect and replicate data from your Microsoft Azure SQL database using Stitch's Microsoft Azure integration."
show-in-menus: false

key: "microsoft-azure-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "microsoft-azure"
display_name: "Microsoft Azure SQL Database"

hosting-type: "microsoft-azure"

this-version: "1.0"

driver: "7.2.1.jre8"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"

## Stitch features
api-type: "platform.mssql"
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

log-based-replication-minimum-version: "n/a"
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
  - item: "**Privileges in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: |
      **If using Log-based Incremental Replication**, you'll need the `ALTER DATABASE` privilege in {{ integration.display_name }}. This is required to complete the setup for Log-based Incremental Replication.

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

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/databases/setup/syncing.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}
