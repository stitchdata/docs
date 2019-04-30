---
title: Google CloudSQL PostgreSQL (v15-10-2015)
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl, etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-postgresql/v15-10-2015
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."
input: false

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


## Stitch features

versions: "9.3+"
ssh: false
ssl: false

## General replication features

anchor-scheduling: false
cron-scheduling: false

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

notice-first-line: "**Google CloudSQL PostgreSQL as an input data source**"
notice-copy: |

  This article describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting a Self-Hosted {{ integration.display_name }} Destination guide]({{ link.destinations.setup.cloudsql-postgres | prepend: site.baseurl }}).

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

  - title: "Connect Stitch"
    anchor: "#connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include integrations/databases/setup/database-integration-settings.html type="general" %}

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