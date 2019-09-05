---
title: Google CloudSQL MySQL
keywords: google cloudsql, cloudsql, cloud sql, database integration, etl cloudsql, cloudsql etl, cloudsql mysql, cloudsql mysql etl
permalink: /integrations/databases/google-cloudsql-mysql
summary: "Connect and replicate data from your Google CloudSQL MySQL database using Stitch's Google CloudSQL MySQL integration."
show-in-menus: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "cloudsql-mysql"
display_name: "Google CloudSQL MySQL"
singer: true

repo-url: https://github.com/singer-io/tap-mysql

# this-version: "1.0"

hosting-type: "google-cloudsql"

driver: |
  [PyMySQL 0.7.11](https://pymysql.readthedocs.io/en/latest/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"

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

log-based-replication-minimum-version: "5.6.2"
log-based-replication-master-instance: true

log-based-replication-read-replica: false
log-based-replication-read-replica-reason: "Google CloudSQL MySQL doesn't support binary logging on read replicas."

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice: |
  This article only applies to **MySQL-based** CloudSQL databases.

  If you want to connect a **PostgreSQL-based** CloudSQL instance, use [these instructions]({{ link.integrations.database-integration | prepend: site.baseurl | replace: "INTEGRATION","google-cloudsql-postgresql" }}).

requirements-list:
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

# https://cloud.google.com/sql/docs/mysql/configure-ip

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#db-user)." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

    substeps:
      - title: "Enable automated backups and binary logging"
        anchor: "enable-automated-backups-binary-logging"
        content: |
          In this step, you'll enable automated backups and binary logging for the {{ integration.display_name }} database. This is required to use Log-based Incremental Replication.

          {% capture server-instructions %}
          {% include layout/inline_image.html type="right" file="integrations/cloudsql-enable-binary-logging.png" alt="" max-width="500px" %}
          1. On the **Instance details** page in Google Cloud Platform, click the **Edit** option at the top of the page.
          2. In the **Configuration options** section, open **Enable auto backups**.
          3. If unchecked, check the **Automate backups** option and select a window for automated backups.

             **Note**: This is required to use Log-based Incremental Replication.
          3. If unchecked, check the **Enable binary logging** option.
          4. Click **Save**.

          When binary logging is enabled, Google Cloud SQL will define the required server settings using their pre-defined defaults. Refer to the <a href="#server-settings-details" data-toggle="tab">Server settings list</a> tab for explanations of these parameters and their default values. **No other configuration is required on your part.**
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
      - title: "Locate the database connection details in Google"
        anchor: "locate-database-connection-details"
        content: |
          In this step, you'll locate the {{ integration.display_name }} database's IP address in the Google Cloud Platform console. This will be used to complete the setup in Stitch.

          {% include shared/connection-details/google-cloudsql.html %}

      - title: "Define the database connection details in Stitch"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}

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