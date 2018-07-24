---
title: Amazon MySQL RDS
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-mysql
summary: "Connect and replicate data from your Amazon RDS MySQL using Stitch's MySQL integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mysql-rds"
display_name: "MySQL RDS"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true
setup-name: "MySQL"

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"
icon: /images/integrations/icons/mysql-rds.svg

versions: "n/a"
ssh: true
ssl: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: true
view-replication: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
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
          {% include integrations/databases/setup/binlog/amazon-rds/mysql-rds.html %}

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
      {% include note.html content="You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Define the binlong retention setting"
    anchor: "define-binlog-retention-setting"
    content: |
      {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="binlog-retention-hours" %}

  - title: "Locate RDS connection details in AWS"
    anchor: "locating-rds-database-details"
    content: |
      {% include shared/aws-connection-details.html %}

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
