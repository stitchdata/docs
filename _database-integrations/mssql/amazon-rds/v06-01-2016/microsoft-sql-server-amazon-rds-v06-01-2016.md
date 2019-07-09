---
title: Amazon Microsoft SQL Server RDS (v06-01-2016)
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-rds-microsoft-sql-server/v06-01-2016
summary: "Connect and replicate data from your Amazon Microsoft SQL Server RDS using Stitch's Microsoft SQL Server integration."
show-in-menus: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "sql-server-rds"
display_name: "Amazon Microsoft SQL Server RDS"

hosting-type: "amazon"

this-version: "06-01-2016"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true
setup-name: "Microsoft SQL Server"

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"

## Stitch features

versions: "2000 through 2016"
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
  - item: |
      **Privileges in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: "**Privileges in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: |
      **A database that uses case-insensitive collation**. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support#Collation_Defn){:target="new"} for more info.

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