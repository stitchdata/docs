---
title: Microsoft Azure MySQL (v1)
keywords: microsoft azure, azure, database integration, etl azure, azure etl
permalink: /integrations/databases/microsoft-azure-mysql
summary: "Connect and replicate data from your Microsoft Azure SQL database using Stitch's Microsoft Azure MySQL integration."
show-in-menus: true

key: "microsoft-azure-mysql-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "microsoft-azure-mysql"
display_name: "Microsoft Azure MySQL"

connection-type: "integration"
hosting-type: "microsoft-azure"

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
tier: "Standard"
port: 3306
db-type: "mysql"

## Stitch features
api-type: "platform.mysql"
ssh: true
ssl: true

setup-name: "MySQL"

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
select-all: "sometimes"
select-all-reason: "Log-based Incremental Replication must be enabled and set as the default Replication Method to use the Select All feature."

table-level-reset: true

## Replication methods

define-replication-methods: true
set-default-replication-method: true

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
      **If using Log-based Incremental Replication:**, you'll need:

      1. Privileges in Microsoft Azure that allow you to modify server parameters.
      2. A master server that adheres to [Microsoft's requirements](https://docs.microsoft.com/en-us/azure/mysql/concepts-data-in-replication#requirements){:target="new"}.
      3. A MySQL database running MySQL version {{ integration.log-based-replication-minimum-version }} or newer.


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
          {% capture server-instructions %}
          1. In your **Azure portal**, locate and open the **Azure Database for MySQL** database you want to connect to Stitch.
          2. Click **Settings > Server Parameters**.
          3. Define the following server settings:

          {% assign server-settings = site.data.taps.extraction.database-setup.server-settings.mysql.microsoft-azure-mysql %}

          {% for setting in server-settings %}
             - `{{ setting.name }}` - `{{ setting.value }}`
          {% endfor %}

             Refer to the **Server settings list** tab for more info about these settings.

          4. Click **Save** when finished.
          5. When finished, restart your MySQL server to ensure the changes take effect.
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
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch:

      {% for substep in step.substeps %}
      - [Step 4.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Locate {{ destination.display_name }} connection details"
        anchor: "locate-connection-details"
        content: |
          In this step, you'll retrieve the server address for the {{ integration.display_name }} you want to connect to Stitch. 
          
          This is the value you'll enter in the **Host** field in Stitch in the next step.

          {% include shared/connection-details/microsoft-azure.html %}

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