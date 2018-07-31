---
title: Microsoft Azure
keywords: microsoft azure, azure, database integration, etl azure, azure etl
tags: [database_integrations]
permalink: /integrations/databases/microsoft-azure
summary: "Connect and replicate data from your Microsoft Azure database using Stitch's Azure integration."
show-in-menus: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "azure"
display_name: "Azure"
author: "Stitch"
author-url: https://www.stitchdata.com

# this-version: 

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"
icon: /images/integrations/icons/microsoft-azure.svg

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
