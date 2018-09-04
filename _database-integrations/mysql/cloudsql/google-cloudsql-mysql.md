---
title: Google CloudSQL MySQL
keywords: google cloudsql, cloudsql, cloud sql, database integration, etl cloudsql, cloudsql etl, cloudsql mysql, cloudsql mysql etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-mysql
summary: "Connect and replicate data from your Google CloudSQL MySQL database using Stitch's Google CloudSQL MySQL integration."
show-in-menus: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "cloudsql-mysql"
display_name: "CloudSQL MySQL"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-mysql

# this-version:

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"
icon: /images/integrations/icons/google-cloudsql-mysql.svg

versions: "n/a"
ssh: false
ssl: false
sync-views: false
whitelist:
  tables: true
  columns: true

binlog-replication: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice: |
  This article only applies to **MySQL-based** CloudSQL databases.

  If you want to connect a **PostgreSQL-based** CloudSQL instance, use [these instructions]({{ link.integrations.database-integration | prepend: site.baseurl | replace: "INTEGRATION","google-cloudsql-postgresql" }}).

requirements-list:
  - item: "**The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://dev.mysql.com/doc/refman/8.0/en/create-user.html) is required to create a database user for Stitch."
  - item: "**The `GRANT OPTION` privilege in {{ integration.display_name }}.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option) is required to grant the necessary privileges to the Stitch database user."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

# https://cloud.google.com/sql/docs/mysql/configure-ip

  - title: "Configure database server settings"
    anchor: "server-settings"
    content: |

    substeps:
      - title: "Enable binary logging"
        anchor: "enable-binary-logging"
        content: |
          Next, you need to verify that binary logging is enabled for your {{ integration.display_name }} instance.

          {% include layout/inline_image.html type="right" file="integrations/cloudsql-enable-binary-logging.png" alt="" max-width="500px" %}
          1. On the **Instance details** page in Google Cloud Platform, click the **Edit** option at the top of the page.
          2. In the **Configuration options** section, open **Enable auto backups**.
          3. If unchecked, check the **Enable binary logging** option.
          4. Click **Save**.
      - title: "Define database parameters"
        anchor: "define-database-parameters"
        content: |
          {% include integrations/databases/setup/binlog/vanilla-mysql.html %}

  - title: "Create a Stitch database user"
    anchor: "db-user"
    content: |
      {% include note.html type="single-line" content="You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Retrieve server IDs"
    anchor: "server-id"
    content: |
      {% include integrations/databases/setup/binlog/mysql-server-id.html %}

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}