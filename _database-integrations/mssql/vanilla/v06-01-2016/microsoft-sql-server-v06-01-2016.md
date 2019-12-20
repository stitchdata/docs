---
title: Microsoft SQL Server (v06-01-2016)
keywords: microsoft sql server, sql server, mssql, database integration, etl mssql, mssql etl, sql server etl
permalink: /integrations/databases/microsoft-sql-server/v06-01-2016
summary: "Connect and replicate data from your Microsoft SQL Server database using Stitch's Microsoft SQL Server integration."
show-in-menus: false
input: false

key: "mssql-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mssql"
display_name: "Microsoft SQL Server"

hosting-type: "generic"

this-version: "06-01-2016"

driver: "6.2.2.jre7"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Deprecated"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"

## Stitch features

versions: "2000 - 2016"
ssh: true
ssl: true

## General replication features

anchor-scheduling: false
cron-scheduling: false

extraction-logs: false
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
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
      A server that:
      
      - **Uses case-insensitive collation**. Refer to [Microsoft's documentation]({{ site.data.taps.links.mssql.collation }}){:target="new"} for more info.
      - Allows connections over TCP/IP
      - Allows mixed mode authentication

requirements-info: "**Make sure your server is set up properly before continuing**. If you need some help figuring out your hosting details, we recommend looping in a member of your engineering team."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "#connect-stitch"
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


## Troubleshooting {#troubleshooting}

### Connection issues and collation

If you're experiencing connection issues and have verified that the database user has the correct permissions, check your server's collation setting.

Connecting MSSQL to Stitch successfully requires that your server use **case-insensitive** collation.

### Data discrepancies and database user language settings

If you're missing data, check that the database user's language setting is set to `us_english`. Using a different setting can cause problems with replication, including issues with properly identifying new and updated data.
