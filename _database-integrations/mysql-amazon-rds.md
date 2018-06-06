---
title: Amazon RDS MySQL
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-rds-mysql
summary: "Connect and replicate data from your Amazon RDS MysQL database using Stitch's MySQL integration."

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

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"
icon: /images/integrations/icons/amazon-rds.svg

versions: "n/a"
ssh: true
ssl: true
sync-views: true
whitelist:
  tables: true
  columns: true

setup-name: "MySQL"

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
          {% include integrations/databases/setup/binlog/amazon-rds.html %}

      - title: "Define the backup retention period"
        anchor: "define-backup-retention-period"
        content: |
          The backup retention period setting defines the number of days for which automated backups are retained. This ensures that data can still be replicated even if issues with Stitch arise.

          1. Navigate back to the **Instances** page by using the menu on the left side of the page.
          2. Select the instance you're connecting to Stitch.
          3. Click **Instance actions > Modify**.
          4. Scroll down to the **Backup** section.
          5. Set **Backup retention period** to `1 day`:

             ![A backup retention period setting of 1 day for an RDS instance in the AWS console]({{ site.baseurl }}/images/integrations/rds-binlog-backup-retention-period.png)

      - title: "Apply parameter changes and reboot the database"
        anchor: "apply-changes-reboot-database"
        content: |
          1. Scroll to the bottom of the page and click **Continue**.
          2. The next page will display a summary of the modifications made to the database.

             In the **Scheduling of Modifications** section, select the **Apply Immediately** option.
          3. Click **Modify DB Instance** to apply the changes.
          4. Navigate to the Instance Details page and locate the **Parameter group**. Initially, the Parameter group should say `applying`.

             When it changes to `pending-reboot`, you can reboot the database and apply the changes.
          5. Scroll up to the top of the page and locate the **Instance actions** menu.
          6. In this menu, click **Reboot**.
          7. On the next page, click **Reboot** to confirm you want to reboot the instance.

          Rebooting the instance will take a few minutes. When the status of the **parameter group** changes to `in-sync` and the **DB instance status** (located at the top of the Instance Details page) changes to `available`, the reboot will be complete:

          ![An "Available" DB instance status for an RDS instance in the AWS console]({{ site.baseurl }}/images/integrations/rds-binlog-db-instance-status.png)

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      {% include note.html content="You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Locate RDS connection details in AWS"
    anchor: "locating-rds-database-details"
    content: |

      Next, you'll retrieve the connection details required to complete the setup in Stitch. This info can be found on the Instance Details page in AWS.

      If you don't still have this page open, click **Instances** and then the instance you're connecting to Stitch.

      1. On the Instance Details page, scroll down to the **Connect** section.
      2. Locate the **Endpoint** and **Port** fields, which are highlighted in the image below:

         ![Amazon RDS Instance Details page with the Endport and Port fields highlighted]({{ site.baseurl }}/images/integrations/amazon-rds-details-page.png)

      Leave this page open for now - you'll need it to complete the setup in the next step.

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
