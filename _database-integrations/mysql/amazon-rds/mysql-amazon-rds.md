---
title: Amazon MySQL RDS (v1)
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-rds-mysql
summary: "Connect and replicate data from your Amazon RDS MySQL using Stitch's MySQL integration."
show-in-menus: true

key: "mysql-rds-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mysql-rds"
display_name: "Amazon MySQL RDS"

this-version: "1"

hosting-type: "amazon"

driver: |
  [PyMySQL 0.7.11](https://pymysql.readthedocs.io/en/latest/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true
singer: true
repo-url: https://github.com/singer-io/tap-mysql
setup-name: "MySQL"

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"

## Stitch features
api-type: "platform.mysql"
versions: "n/a"
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
      **Privileges in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: |
      **The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://dev.mysql.com/doc/refman/8.0/en/create-user.html){:target="new"} is required to create a database user for Stitch.
  - item: |
      **The `GRANT OPTION` privilege in {{ integration.display_name }}.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option){:target="new"} is required to grant the necessary privileges to the Stitch database user.

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
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#create-a-database-user)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}
    substeps:
      - title: "Configure the database parameter group"
        anchor: "configure-database-parameter-group"
        content: |
          In this step, you'll configure the database parameters required to use Log-based Incremental Replication.
          
          {% include integrations/databases/setup/binlog/amazon-rds/mysql-rds.html %}

## I believe this is only applicable to MySQL and not Aurora,
## as I can't find evidence of it being necessary in Aurora's
## documentation.
      - title: "Define the backup retention period"
        anchor: "define-backup-retention-period"
        content: |
          {% capture mysql-rds-backup-requirement %}
          **Enabling automatic backups is required to use Log-based Incremental Replication.** In Amazon RDS, enabling automatic backups also enables binary logging, which is what Stitch uses to perform Log-based Incremental Replication.

          Skipping this step or disabling automatic backups will cause replication issues in Stitch.

          Refer to the **Transaction Size** section of [Amazon's Importing Data into a MySQL DB Instance](https://docs.aws.amazon.com/en_us/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.Other.html){:target="new"} documentation for more info.
          {% endcapture %}
          {% include note.html type="single-line" content=mysql-rds-backup-requirement %}

          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="backup-retention-period" %}

      - title: "Apply parameter changes and reboot the database"
        anchor: "apply-changes-reboot-database"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="reboot-the-instance" %}

      - title: "Retrieve server IDs"
        anchor: "server-id"
        content: |
          {% include integrations/databases/setup/binlog/mysql-server-id.html %}

      - title: "Define the binlog retention setting"
        anchor: "define-binlog-retention-setting"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="binlog-retention-hours" %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      {% include note.html type="single-line" content="**Note**: You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Locate the database connection details in AWS"
        anchor: "locating-rds-database-details"
        content: |
          {% include shared/connection-details/amazon.html %}

      - title: "Define the database connection details in Stitch"
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