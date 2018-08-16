---
title: Microsoft SQL Server
keywords: microsoft sql server, sql server, mssql, database integration, etl mssql, mssql etl, sql server etl
tags: [database_integrations]
permalink: /integrations/databases/microsoft-sql-server
summary: "Connect and replicate data from your Microsoft SQL Server database using Stitch's MSSQL integration."
show-in-menus: true

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mssql"
display_name: "MSSQL"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 1433
db-type: "mssql"
icon: /images/integrations/icons/mssql.svg

versions: "n/a"
ssh: false
ssl: true
sync-views: true
whitelist:
  tables: true
  columns: true

binlog-replication: false

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Permissions in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: |
      A server that:
      
      - Uses case-insensitive collation. [More info about collation can be found here in Microsoft's documentation](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support#Collation_Defn).
      - Allows connections over TCP/IP
      - Allows mixed mode authentication

requirements-info: "**Make sure your server is set up properly before continuing**. If you need some help figuring out your hosting details, we recommend looping in a member of your engineering team."

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

---

## Troubleshooting {#troubleshooting}

### Connection issues and collation

If you're experiencing connection issues and have verified that the database user has the correct permissions, check your server's collation setting.

Connecting MSSQL to Stitch successfully requires that your server use **case-insensitive** collation.

### Data discrepancies and database user language settings

If you're missing data, check that the database user's language setting is set to `us_english`. Using a different setting can cause problems with replication, including issues with properly identifying new and updated data.