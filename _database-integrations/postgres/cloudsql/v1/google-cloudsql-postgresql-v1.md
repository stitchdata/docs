---
title: Google CloudSQL PostgreSQL (v1)
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl, etl
tags: [database_integrations]
permalink: /integrations/databases/google-cloudsql-postgresql/v1
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."

key: "cloudsql-postgres-integration"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "cloudsql-postgres"
display_name: "Google CloudSQL PostgreSQL"

singer: true
tap-name: "Postgres"
repo-url: "https://github.com/singer-io/tap-postgres"

this-version: "1"

hosting-type: "google-cloudsql"

driver: |
  [Psycopg 2.7.4](http://initd.org/psycopg/docs/index.html){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

frequency: "1 hour"
tier: "Free"
port: 5432
db-type: "postgres"

## Stitch features
api-type: "platform.cloudsql_pg"
versions: "9.3+"
ssh: false
ssl: false

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true

log-based-replication-minimum-version: "n/a"

log-based-replication-master-instance: false
log-based-replication-master-instance-reason: "Google CloudSQL doesn't currently support logical replication."
log-based-replication-master-instance-doc-link: "https://groups.google.com/forum/#!topic/google-cloud-sql-discuss/md_7Rq3LgB0"

log-based-replication-read-replica: false
# log-based-replication-read-replica-reason: *not-supported
# log-based-replication-read-replica-reason: *not-supported-link

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
  - item: "**To be running PostgeSQL 9.3+ or greater**. PostgreSQL 9.3.x is the minimum version Stitch supports for PostgreSQL integrations."

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      In this step, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Locate the database connection details in Google"
        anchor: "locate-database-connection-details"
        content: |
          {% include shared/connection-details/google-cloudsql.html %}

      - title: "Define the database connection details in Stitch"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

      - title: "Save the integration"
        anchor: "save-integration"
        content: |
          {% include shared/database-connection-settings.html type="finish-up" %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/databases/setup/syncing.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}