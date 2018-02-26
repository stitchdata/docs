---
title: Amazon Aurora
keywords: amazon aurora, aurora, database integration, etl aurora, aurora etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-aurora
summary: "Connect and replicate data from your Amazon Aurora database using Stitch's Aurora integration."
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://mysql.topostgres.com/"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "aurora"
display_name: "Aurora"
singer: true
author: "Stitch"
author: "Stitch"
repo-url: https://github.com/singer-io/tap-mysql

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 3306
db-type: "mysql"
icon: /images/integrations/icons/amazon-aurora.svg

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