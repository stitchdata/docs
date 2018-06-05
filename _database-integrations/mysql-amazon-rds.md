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
    content: "[TODO]"
    substeps:
      - title: "Define the backup retention period"
        anchor: "define-backup-retention-period"
        content: |

      - title: "Configure the database parameter group"
        anchor: "configure-database-parameter-group"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds.html %}

  - title: "Create a Stitch database user"
    anchor: "db-user"
    content: |
      {% include note.html content="You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Locate RDS connection details in AWS"
    anchor: "locating-rds-database-details"
    content: |

      The majority of this info can be found on the Database Details page in the AWS Console.

      1. Navigate to the **RDS Dashboard.**
      2. Select the RDS instance you want to connect to Stitch.
      3. Click the **Instance Actions** menu and select **See Details**.
      4. On this page, you'll need to locate these fields:

         - **Endpoint**
         - **Port**

      Below is a screen cap of this page with the required fields highlighted:

      ![Amazon RDS Database Details page.]({{ site.baseurl }}/images/integrations/amazon-rds-details-page.png)

      Leave this page open for now - you'll need it to complete the setup in the next step.

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
