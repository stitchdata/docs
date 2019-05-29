---
title: Amazon PostgreSQL RDS (v1.0)
keywords: amazon, amazon rds, rds, relational database services, database integration, etl rds, rds etl
permalink: /integrations/databases/amazon-rds-postgresql/v1
summary: "Connect and replicate data from your Amazon PostgreSQL RDS using Stitch's PostgreSQL integration."
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostges.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "postgresql-rds"
display_name: "PostgreSQL RDS"

singer: true
tap-name: "Postgres"
repo-url: "https://github.com/singer-io/tap-postgres"

hosting-type: "amazon"

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

versions: "9.3+; 9.4+ for binlog"
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

log-based-replication-minimum-version: "9.4"
log-based-replication-master-instance: true

log-based-replication-read-replica: false
log-based-replication-read-replica-reason: "PostgreSQL only supports logical replication on master instances."
log-based-replication-read-replica-doc-link: |
  {{ link.replication.log-based-incremental | prepend: site.baseurl | append: "#limitation-7--only-supports-master-instances-postgresql" }} 

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
        - View database details, which is required for retrieving the database's connection details
  - item: "**Permissions in PostgreSQL that allow you to create users.** This is required to create a database user for Stitch."
  - item: |
      **If using Log-based Incremental Replication**, you'll need:

      - **A database running PostgreSQL 9.4 or greater**. Earlier versions of PostgreSQL do not include logical replication functionality, which is required for Log-based Replication.
      - **The `rds_superuser` role in your {{ integration.display_name }} database, if you want to use Log-based Replication.** [This role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.Roles){:target="new"} is required to grant the `rds_replication` privilege to Stitch's database user.
      - **To connect to the master instance.** Log-based replication will only work on master instances due to a feature gap in PostgreSQL 10. [Based on their forums](https://commitfest.postgresql.org/12/788/){:target="new"}, PostgreSQL is working on adding support for using logical replication on a read replica to a future version.
  - item: |
      **If you're not using Log-based Incremental Replication**, you'll need:

      - **A database running PostgreSQL 9.3.x or greater.** PostgreSQL 9.3.x is the minimum version Stitch supports for PostgreSQL integrations.
      - **To verify if the database is a read replica, or follower**. While we always recommend connecting a replica over a production database, this also means you may need to verify some of its settings - specifically the `max_standby_streaming_delay` and `max_standby_archive_delay` settings - before connecting it to Stitch. We recommend setting these parameters to 8-12 hours for an initial replication job, and then decreasing them afterwards.


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

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#connect-stitch)." %}
      
      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      In this section:

      {% for substep in step.substeps %}
      - [Step 3.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Configure the database parameter group"
        anchor: "configure-database-parameter-group"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/postgresql-rds.html %}

      - title: "Define the backup retention period"
        anchor: "define-backup-retention-period"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="backup-retention-period" %}

      - title: "Apply parameter changes and reboot the database"
        anchor: "apply-changes-reboot-database"
        content: |
          {% include integrations/databases/setup/binlog/amazon-rds/define-database-settings.html content="reboot-the-instance" %}

      - title: "Create a replication slot"
        anchor: "create-replication-slot"
        content: |
          {% include integrations/databases/setup/binlog/postgres-replication-slot.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Locate the database connection details in AWS"
        anchor: "locating-rds-database-details"
        content: |
          {% include shared/connection-details/amazon.html type="connection-details" %}

      - title: "Define the database connection details in Stitch"
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

      - title: "Define Log-based Replication setting"
        anchor: "define-log-based-replication-setting"
        content: |
          {% include note.html type="single-line" content="**Note**: Skip this step if you're not planning to use Log-based Incremental Replication. [Click to skip ahead](#create-replication-schedule)." %}

          {% include integrations/databases/setup/binlog/log-based-replication-default-setting.html %}

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