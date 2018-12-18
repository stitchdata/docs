---
title: MySQL
keywords: mysql, database integration, etl mysql, mysql etl
tags: [database_integrations]
permalink: /integrations/databases/mysql
summary: "Connect and replicate data from your MySQL database using Stitch's MySQL integration."
microsites:
  - title: "{{ page.display_name }} to Redshift"
    url: "http://mysql.toredshift.com/"
  - title: "{{ page.display_name }} to Postgres"
    url: "http://mysql.topostgres.com/"

show-in-menus: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mysql"
display_name: "MySQL"
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
icon: /images/integrations/icons/mysql.svg

versions: "n/a"
ssh: true
ssl: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: true
read-replica-binlog: true
view-replication: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://dev.mysql.com/doc/refman/8.0/en/create-user.html) is required to create a database user for Stitch."
  - item: "**The `GRANT OPTION` privilege in {{ integration.display_name }}.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option) is required to grant the necessary privileges to the Stitch database user."
  - item: "**The `SUPER` privilege in {{ integration.display_name }}.** If using binlog replication, the [`SUPER` privilege](https://dev.mysql.com/doc/refman/5.6/en/privileges-provided.html#priv_super) is required to define the appropriate server settings."


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Configure database server settings"
    anchor: "server-settings"
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