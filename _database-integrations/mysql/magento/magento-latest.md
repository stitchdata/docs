---
title: Magento
keywords: magento, database integration, etl magento, magento etl
tags: [database_integrations]
permalink: /integrations/databases/magento
summary: "Connect and replicate data from your Magento database using Stitch's Magento integration."
show-in-menus: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "magento"
display_name: "Magento"
setup-name: "MySQL"
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
icon: /images/integrations/icons/magento.svg

versions: "n/a"
ssh: true
ssl: false
sync-views: false
whitelist:
  tables: true
  columns: true

binlog-replication: false

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