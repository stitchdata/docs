---
title: Google CloudSQL PostgreSQL
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl, etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-postgresql
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "cloudsql-postgres"
display_name: "Google CloudSQL PostgreSQL"
author: "Stitch"
author-url: "https://www.stitchdata.com"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 5432
db-type: "postgres"
icon: /images/integrations/icons/google-cloudsql-postgresql.svg

versions: "9.3+"
ssh: false
ssl: false
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

  - title: "create db user"

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}


{% capture cloudsql %}
This article only applies to **Postgres-based** CloudSQL databases.<br><br>

If you want to connect a **MySQL-based** CloudSQL instance, use [these instructions]({{ link.integrations.database-integration | prepend: site.baseurl | replace: "INTEGRATION","google-cloudsql-mysql" }}).
{% endcapture %}

{% include important.html content=cloudsql %}