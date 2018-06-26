---
title: Google CloudSQL PostgreSQL (v15-10-2015)
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl, etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-postgresql/v15-10-2015
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "cloudsql-postgres"
display_name: "Google CloudSQL PostgreSQL"

this-version: "15-10-2015"

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
binlog: false
whitelist:
  tables: true
  columns: true

anchor-scheduling: false
extraction-logs: false
loading-reports: true

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: "**Permissions in PostgreSQL that allow you to create users.** This is required to create a database user for Stitch."
  - item: "**To be running PostgeSQL 9.3+ or greater**."
  - item: |
      **To verify if the database is a read replica, or follower**. While we always recommend connecting a replica over a production database, this also means you may need to verify some of its settings - specifically the `standby` settings - before connecting it to Stitch.

      Info about these settings can be found in the [Configure the database parameter group](#configure-database-parameter-group) section.

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "Locate database connection details"
    anchor: "locate-database-connection-details"
    content: |
      In this step, you'll locate the {{ integration.display_name }}'s IP address in the Google Cloud Platform console. This will be used to complete the setup in Stitch.

      {% include shared/google-cloud-platform/locate-database-details.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

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