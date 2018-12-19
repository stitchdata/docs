---
title: Amazon Aurora (MySQL) RDS
keywords: amazon aurora, aurora, database integration, etl aurora, aurora etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-aurora
summary: "Connect and replicate data from your Amazon Aurora RDS database using Stitch's Aurora integration."
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://mysql.topostgres.com/"
show-in-menus: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "aurora-rds"
display_name: "Aurora RDS"
singer: true
author: "Stitch"
author: "Stitch"
tap-name: "MySQL"
repo-url: https://github.com/singer-io/tap-mysql

# this-version:

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true
setup-name: "Amazon Aurora"

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"
icon: /images/integrations/icons/amazon-aurora.svg

versions: "n/a"
ssh: true
ssl: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: true
read-replica-binlog: false
view-replication: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice: "Stitch's {{ integration.display_name }} integration only supports MySQL-backed instances."

requirements-list:
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.

  - item: |
      **To connect the master instance if using binlog replication.** As per [Amazon's documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Limitations){:target="new"}, binlog replication can't be enabled on Aurora read replicas.
  - item: "**The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://dev.mysql.com/doc/refman/8.0/en/create-user.html) is required to create a database user for Stitch."
  - item: "**The `GRANT OPTION` privilege in {{ integration.display_name }}.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option) is required to grant the necessary privileges to the Stitch database user."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "Configure database server settings"
    anchor: "server-settings"
    content: |
      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}
    substeps:
      - title: "Configure the database parameter group"
        anchor: "configure-database-parameter-group"
        content: |
          In this step, you'll create a new database cluster parameter group.
           
          {% include integrations/databases/setup/binlog/amazon-rds/aurora-rds.html %}

      - title: "Apply the parameter group to the database"
        anchor: "apply-parameter-group-to-database"
        content: |
          Next you'll apply the parameter group to the {{ integration.display_name }} database.

          1. In AWS, click the **Instances** option in the menu on the left side of the page.
          2. Select the instance you're connecting to Stitch.
          3. Click **Instance actions > Modify**.
          4. In the **Modify DB Instance** page, scroll down to the **Database options** section.
          5. From the **DB parameter group** dropdown, select the parameter group you created in the previous step.

      - title: "Define the backup retention period"
        anchor: "define-backup-retention-period"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="backup-retention-period" %}

      - title: "Apply parameter changes and reboot the database"
        anchor: "apply-changes-reboot-database"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="reboot-the-instance" %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      {% include note.html type="single-line" content="You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Retrieve server IDs"
    anchor: "server-id"
    content: |
      {% include integrations/databases/setup/binlog/mysql-server-id.html %}

  - title: "Define the binlong retention setting"
    anchor: "define-binlog-retention-setting"
    content: |
      {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="binlog-retention-hours" %}

  - title: "Locate RDS connection details in AWS"
    anchor: "locating-rds-database-details"
    content: |
      {% include shared/aws-connection-details.html %}

  - title: "Connect Stitch"
    anchor: "#connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html %}

      - title: "Define Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}