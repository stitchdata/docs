---
title: MariaDB
keywords: mariadb, database integration, etl mariadb, mariadb etl
tags: [database_integrations]
permalink: /integrations/databases/mariadb
summary: "Connect and replicate data from your MariaDB database using Stitch's MariaDB integration."
show-in-menus: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mariadb"
display_name: "MariaDB"
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
icon: /images/integrations/icons/mariadb.svg

versions: "n/a"
ssh: true
ssl: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: true
view-replication: false

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**The `CREATE USER` or `INSERT` privilege (for the `mysql` database).** The [`CREATE USER` privilege](https://mariadb.com/kb/en/library/create-user/) is required to create a database user for Stitch."
  - item: "**The `GRANT OPTION` privilege in {{ integration.display_name }}.** The [`GRANT OPTION` privilege](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_grant-option), and is required to grant the necessary privileges to the Stitch database user. Additionally, you must have the privileges you'll grant to the Stitch user."
  - item: "**The `SUPER` privilege in {{ integration.display_name }}.** If using binlog replication, the [`SUPER` privilege](https://mariadb.com/kb/en/library/grant/#global-privileges) is required to define the appropriate server settings."

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
