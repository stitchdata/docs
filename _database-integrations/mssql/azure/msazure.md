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

## Stitch features

versions: "2000 through 2016"
ssh: true
ssl: true

## General replication features

anchor-scheduling: false
extraction-logs: false
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-read-replica: false

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


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

  - title: "Connect Stitch"
    anchor: "#connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html type="general" %}

      - title: "Define the SSH connection details"
        anchor: "ssh-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html type="ssh" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html type="ssl" %}

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}
