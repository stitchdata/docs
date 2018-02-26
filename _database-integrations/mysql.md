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
sync-views: true
whitelist:
  tables: true
  columns: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Permissions in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "create db user"

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}