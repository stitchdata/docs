---
title: Amazon PostgreSQL RDS (v15-10-2015)
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-rds-postgresql/v15-10-2015
summary: "Connect and replicate data from your Amazon PostgreSQL RDS using Stitch's PostgreSQL integration."
input: false
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostges.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "postgresql-rds"
display_name: "PostgreSQL RDS"

this-version: "15-10-2015"

hosting-type: "amazon"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true
setup-name: "PostgreSQL"

frequency: "30 minutes"
tier: "Free"
port: 5432
db-type: "postgres"

## Stitch features

versions: "9.3+"
ssh: true
ssl: true

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

notice-first-line: "**PostgreSQL RDS as an input data source**"
notice-copy: |

  This article describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting an {{ integration.display_name }} Destination guide]({{ link.destinations.setup.postgres-rds | prepend: site.baseurl }}).

requirements-list:
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: "**Permissions in {{ integration.display_name }} that allow you to create/manage users.** This is required to create the Stitch database user."
  - item: |
      **To verify if the database is a read replica, or follower**. While we always recommend connecting a replica over a production database, this also means you may need to verify some of its settings - specifically the `standby` settings - before connecting it to Stitch.

      On occasion, [the default values for the `standby` settings can prevent Stitch from successfully completing queries]({{ link.troubleshooting.postgres-hot-standby | prepend: site.baseurl }}), resulting in slow, intermittent replication. This is usually only an issue during historical syncs or when replicating large amounts of data (ex: a large table using Full Table Replication).

      If you find that the `hot_standby` setting is `on`, proactively increasing the following settings from 30 seconds to 8-12 hours can help prevent this issue:

      - `max_standby_archive_delay`
      - `max_standby_streaming_delay`

      After the initial historical sync completes, you can typically decrease these settings again.

      For an official explanation of these settings, [check out the Postgres docs](https://www.postgresql.org/docs/9.0/static/runtime-config-wal.html#GUC-MAX-STANDBY-ARCHIVE-DELAY).

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
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Locate the database connection details in AWS"
        anchor: "locating-rds-database-details"
        content: |
          {% include shared/connection-details/amazon.html %}
          
      - title: "Define the database connection details"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSH connection details"
        anchor: "ssh-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssh" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" %}

  - title: "Create a replication schedule"
    anchor: "create-replication-schedule"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Select data to replicate"
    anchor: "sync-data"
    content: |
      {% include integrations/databases/setup/syncing.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}