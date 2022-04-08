---
title: Google CloudSQL PostgreSQL (HP) (v2)
keywords: postgresql, postgres, google cloudsql postgres, google cloudsql postgresql, database integration, etl postgres, etl cloudsql, cloudsql etl, postgres etl, postgresql etl, etl
permalink: /integrations/databases/google-cloudsql-postgresql/v2
summary: "Connect and replicate data from your Google CloudSQL PostgreSQL database using Stitch's Google CloudSQL PostgreSQL integration."

key: "cloudsql-postgres-integration"


# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "cloudsql-postgres"
display_name: "Google CloudSQL PostgreSQL"
singer: true

tap-name: "Postgres"


this-version: "2"

hosting-type: "google-cloudsql"

driver: |
  [](){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

frequency: "1 hour"
tier: "Standard"
port: 5432
db-type: "postgres"

## Stitch features
api-type: "platform.hp-cloudsql-pg"
override-api-type: true

versions: "9.3+; 9.4+ for binlog"
ssh: false
ssl: true

## General replication features

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true
select-all: "sometimes"
select-all-reason: "Log-based Incremental Replication must be enabled and set as the default Replication Method to use the Select All feature."

table-level-reset: true

## Replication methods

define-replication-methods: true
set-default-replication-method: true

log-based-replication-minimum-version: "9.4"
log-based-replication-master-instance: true
log-based-replication-master-instance-reason: "Google CloudSQL doesn't currently support logical replication."
log-based-replication-master-instance-doc-link: "https://groups.google.com/forum/#!topic/google-cloud-sql-discuss/md_7Rq3LgB0"

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

notice-first-line: "**Google CloudSQL PostgreSQL as an input data source**"
notice-copy: |

  This article describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting a Self-Hosted {{ integration.display_name }} Destination guide]({{ link.destinations.setup.cloudsql-postgres | prepend: site.baseurl }}).

requirements-list:
  - item: "**Permissions in Google Cloud that allow you to modify the database's connection settings.** This is required to whitelist Stitch's IP addresses."
  - item: "**Permissions in PostgreSQL that allow you to create users.** This is required to create a database user for Stitch."
  - item: |
      **If using Log-based Replication**, you'll need:

      - **A database running PostgreSQL 9.4 or greater** Earlier versions of PostgreSQL do not include logical replication functionality, which is required for Log-based Replication.
      - **The `cloudsqlsuperuser` role.** If using logical replication, this is required to create a logical replication slot for Stitch.
      - **To connect to the master instance.** Log-based replication will only work on master instances due to a feature gap in PostgreSQL 10. [Based on their forums](https://commitfest.postgresql.org/12/788/){:target="new"}, PostgreSQL is working on adding support for using logical replication on a read replica to a future version.
  - item: |
      **If you're not using Log-based Replication**, you'll need:

      - **A database running PostgreSQL 9.3.x or greater.** PostgreSQL 9.3.x is the minimum version Stitch supports for PostgreSQL integrations.
      - **To verify if the database is a read replica, or follower**. While we always recommend connecting a replica over a production database, this also means you may need to verify some of its settings - specifically the `max_standby_streaming_delay` and `max_standby_archive_delay` settings - before connecting it to Stitch. We recommend setting these parameters to 8-12 hours for an initial replication job, and then decreasing them afterwards.
  

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

setup-steps:
  - title: "Verify your Stitch account's data pipeline region"
    anchor: "verify-stitch-account-region"
    content: |
      {% include shared/whitelisting-ips/locate-region-ip-addresses.html first-step=true %}
      
  - title: "Configure database connection settings"
    anchor: "connect-settings"
    content: |
      {% include integrations/templates/configure-connection-settings.html %}

  - title: "Create a Stitch database user"
    anchor: "create-a-database-user"
    content: |
      In this step, you'll create a dedicated database user for Stitch. This will ensure Stitch is visible in any logs or audits, and allow you to maintain your privilege hierarchy.

      {% include integrations/templates/create-database-user-tabs.html %}

  - title: "Configure Log-based Incremental Replication"
    anchor: "configure-log-based-incremental-replication"
    content: |
      {% include note.html type="single-line" content="**Note**: [Skip this step](#connect-stitch) if you're not planning to use Log-based Incremental Replication." %}

      {% include integrations/databases/setup/binlog/configure-server-settings-intro.html %}

      In this section:

      {% for substep in step.substeps %}
      - [Step 4.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}
    substeps:
      - title: "Enable the logical replication setting"
        anchor: "enable-logical-replication-setting"
        content: |
          To use Log-based Replication for your {{ integration.display_name }} integration, you'll update the `cloudsql.logical_decoding` flag for your database to `on`. This enables the `wal2json` extension for your instance, which is what Stitch uses to perform Log-based Incremental Replication.

          You can set a database flag using the CloudSQL Console or gcloud. We're going to use the [Console Method](https://cloud.google.com/sql/docs/postgres/flags#console){:target="new"}.

          1. In the window where your Google Cloud Platform account is open, navigate to the page of the instance you're connecting.
          2. Click **Edit**.
          3. Scroll down to the **Flags** section.
          4. Click **Add Item**, choose `cloudsql.logical_decoding`, and set its value to `on`.
          5. Confirm the change on the **Overview** page.

      - title: "Restart the {{ integration.display_name }} instance"
        anchor: "restart-database-instance"
        content: |
          For the flag changes to take effect, you'll need to [restart your {{ integration.display_name }} instance](https://cloud.google.com/sql/docs/postgres/start-stop-restart-instance#restart){:target="new"}.

          1. On the instance page in Google Cloud Platform, click the **Restart** button in the bar at the top of the page.
          2. In the **Restart database instance** box, click **Restart**.

          After the instance has restarted, move onto the next step.

      - title: "Create a replication slot"
        anchor: "create-replication-slot"
        content: |
          {% include integrations/databases/setup/binlog/postgres-replication-slot.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

      {% for substep in step.substeps %}
      - [Step 5.{{ forloop.index }}: {{ substep.title | flatify }}](#{{ substep.anchor }})
      {% endfor %}

    substeps:
      - title: "Locate the database connection details in Google"
        anchor: "locate-database-connection-details"
        content: |
          {% include shared/connection-details/google-cloudsql.html %}

      - title: "Define the database connection details in Stitch"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

      - title: "Define the SSL connection details"
        anchor: "ssl-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="ssl" %}

          Addititionally, the instance shouldn't require SSL connections or you'll receive the following error in Stitch:

          ```shell
          {{ site.data.errors.extraction.databases[integration.db-type]raw-error.ssl-required-error | strip_newlines }}
          ```

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
      {% include integrations/shared-setup/data-selection/object-selection.html %}
---
{% assign integration = page %}
{% include misc/data-files.html %}