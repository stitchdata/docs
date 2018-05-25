---
title: MariaDB
keywords: mariadb, database integration, etl mariadb, mariadb etl
tags: [database_integrations]
permalink: /integrations/databases/mariadb
summary: "Connect and replicate data from your MariaDB database using Stitch's MariaDB integration."

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
sync-views: false
whitelist:
  tables: true
  columns: true

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
      Next, you'll configure your server to use binlog replication.

      Binlog replication is a method of replication that reads a database's binary log files. These files contain information about modifications made to data in a {{ integration.display_name }} instance. Binlog replication captures all inserts, updates, and deletes made to records, and is the most accurate and efficient method of replication.

      While Stitch recommends using binlog to replicate data, it isn't mandatory. Stitch offers additional [Replication Methods]({{ link.replication.rep-methods | prepend: site.baseurl }}) for {{ integration.display_name }} databases that don't require defining these settings.

      {% capture section-name %}
      mysqld
      {% endcapture %}

      {% capture server-instructions %}
      Log into your database server and locate the `my.cnf` file. This is usually located at `/etc/my.cnf`.

      Ensure the `my.cnf` file has the following lines in the `{{ section-name | strip }}` section.
      {% endcapture %}

      {% include integrations/templates/configure-server-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "db-user"
    content: |
      {% include note.html content="You must have the `CREATE USER` and `GRANT OPTION` privileges to complete this step." %} 

      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
