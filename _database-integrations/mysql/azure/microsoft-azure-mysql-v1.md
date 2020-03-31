---
title: Microsoft Azure MySQL (v1)
keywords: microsoft azure, azure, database integration, etl azure, azure etl
permalink: /integrations/databases/microsoft-azure-mysql/v1
summary: "Connect and replicate data from your Microsoft Azure SQL database using Stitch's Microsoft Azure MySQL integration."
show-in-menus: true

key: "microsoft-azure-mysql-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "microsoft-azure-mysql"
display_name: "Microsoft Azure MySQL"

hosting-type: "generic"

this-version: "1"

driver: |
  [PyMySQL 0.9.3](https://pymysql.readthedocs.io/en/latest/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

singer: true
repo-url: https://github.com/singer-io/tap-mysql
certified: true

tap-name: "MySQL"

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"

## Stitch features
api-type: "platform.mysql"
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

log-based-replication-minimum-version: "5.6.2"
log-based-replication-master-instance: true
log-based-replication-read-replica: true

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://dev.mysql.com/doc/refman/8.0/en/create-user.html){:target="new"} is required to create a database user for Stitch.
  - item: |
      **The `GRANT OPTION` privilege in {{ integration.display_name }}.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option){:target="new"} is required to grant the necessary privileges to the Stitch database user.
  - item: |
      **For Log-based replication:**
      1. Privileges in Azure that allow you to modify server parameters.
      2. MySQL master server must be in a General Purpose or Memory Optimized pricing tier. These are the tiers that allow you to create read replicas of your server.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#db-user)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}
    substeps:
      - title: "Configure server settings"
        anchor: "configure-database-server-settings"
        content: |
          In this step, you'll configure your {{ integration.display_name }} server to use Log-based Incremental Replication.

          {% capture server-instructions %}
          1. In your **Azure portal**, locate your **Azure Database for MySQL** server.
          2. Click **Settings > Server Parameters**.
          3. Define the requred server settings using their pre-defined defaults. Refer to the <a href="#server-settings-details" data-toggle="tab">Server settings list</a> tab for explanations of these parameters and their default values. **No other configuration is required on your part.**
          {% endcapture %}
          
          {% include integrations/templates/configure-server-settings.html %}
          
      - title: "Retrieve server IDs"
        anchor: "server-id"
        content: |
          {% include integrations/databases/setup/binlog/mysql-server-id.html %}

  - title: "Create a Stitch database user"
    anchor: "db-user"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

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
          {% include shared/database-connection-settings.html type="ssl" ssl-fields=true %}

      - title: "Define the Log-based Replication setting"
        anchor: "define-default-replication-method"
        content: |
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