---
title: Google CloudSQL MySQL
keywords: google cloudsql, cloudsql, cloud sql, database integration, etl cloudsql, cloudsql etl, cloudsql mysql, cloudsql mysql etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-mysql
summary: "Connect and replicate data from your Google CloudSQL MySQL database using Stitch's Google CloudSQL MySQL integration."

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

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice: |
  This article only applies to **MySQL-based** CloudSQL databases.

  If you want to connect a **PostgreSQL-based** CloudSQL instance, use [these instructions]({{ link.integrations.database-integration | prepend: site.baseurl | replace: "INTEGRATION","google-cloudsql-postgresql" }}).

requirements-list:
  - item: "**Permissions in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "create db user"

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}