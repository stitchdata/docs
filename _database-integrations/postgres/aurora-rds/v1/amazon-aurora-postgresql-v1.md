---
title: Amazon Aurora (PostgreSQL) RDS
keywords: amazon aurora, aurora postgresql, postgres, database integration, etl aurora, aurora etl
tags: [database_integrations]
permalink: /integrations/databases/amazon-aurora-postgresql/v1
summary: "Connect and replicate data from your Amazon Aurora PostgreSQL RDS database using Stitch's PostgreSQL integration."
show-in-menus: true

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "aurora-postgresql-rds"
display_name: "Aurora PostgreSQL RDS"
singer: true

singer: true
tap-name: "Postgres"
repo-url: https://github.com/singer-io/tap-postgres

this-version: "1.0"

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

# Stitch features

versions: "9.3"
ssh: true
ssl: true

## General replication features

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
table-level-reset: true

## Replication methods

define-replication-methods: true

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-master-instance-reason: "Amazon doesn't currently support the wal2json plugin, which Stitch uses to perform Log-based Incremental replication."

log-based-replication-read-replica: false
log-based-replication-read-replica-reason: ""

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
  - item: |
      **Permissions in Amazon Web Services (AWS) that allow you to**:

        - Create/manage Security Groups, which is required to whitelist Stitch's IP addresses.
        - View database details, which is required for retrieving the database's connection details.
  - item: "**Permissions in PostgreSQL that allow you to create users.** This is required to create a database user for Stitch."
  - item: |
      **A database running PostgreSQL 9.3.x or greater.** PostgreSQL 9.3.x is the minimum version Stitch supports for PostgreSQL integrations.
  - item: |
      **To verify if the database is a read replica, or follower**. While we always recommend connecting a replica over a production database, this also means you may need to verify some of its settings - specifically the `max_standby_streaming_delay` and `max_standby_archive_delay` settings - before connecting it to Stitch. We recommend setting these parameters to 8-12 hours for an initial replication job, and then decreasing them afterwards.


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      Next, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Locate the database connection details in AWS"
    anchor: "locating-rds-database-details"
    content: |
      {% include shared/aws-connection-details.html %}

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

      - title: "Define Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          **Skip this section in Stitch.** As {{ integration.display_name }} doesn't currently support Log-based Incremental replication, you should skip this section when setting up the integration in Stitch.

      - title: "Create a replication schedule"
        anchor: "create-replication-schedule"
        content: |
          {% include integrations/shared-setup/replication-frequency.html %}

  - title: "sync data"


# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:
  - title: "Log-based Incremental Replication support"
    anchor: "log-based-incremental-replication-support"
    content: |
      Currently, Log-based Incremental Replication is not supported for {{ integration.display_name }} integrations in Stitch. Stitch's implementation of logical replication, which is used to perform Log-based Incremental Replication, relies on the wal2json plugin.

      [As wal2json is not currently supported by Amazon](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.Compare.html){:target="new"} for {{ integration.display_name }}, Log-based Incremental Replication is not available {{ integration.display_name }}-based PostgreSQL integrations.
---
{% assign integration = page %}
{% include misc/data-files.html %}