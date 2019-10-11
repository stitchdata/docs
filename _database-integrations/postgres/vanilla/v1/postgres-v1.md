---
title: PostgreSQL (v1.0)
keywords: postgresql, postgres, database integration, etl postgres, postgres etl, postgresql etl, etl
permalink: /integrations/databases/postgresql/v1
summary: "Connect and replicate data from your PostgreSQL database using Stitch's PostgreSQL integration."

microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostges.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "postgres"
display_name: "PostgreSQL"
singer: true

tap-name: "Postgres"
repo-url: "https://github.com/singer-io/tap-postgres"

hosting-type: "generic"

this-version: "1.0"

driver: |
  [Psycopg 2.7.4](http://initd.org/psycopg/docs/index.html){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "1 hour"
tier: "Free"
port: 5432
db-type: "postgres"

## Stitch features

versions: "9.3+; 9.4+ for binlog"
ssh: true
ssl: true

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
#    Supported Data Types    #
# -------------------------- #

## Some data type support & handling is specific to an integration's version.

## See _data/taps/data-types/postgres.yml

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

notice-first-line: "**PostgreSQL as an input data source**"
notice-copy: |

  This article describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting a Self-Hosted {{ integration.display_name }} Destination guide]({{ link.destinations.setup.self-hosted-postgres | prepend: site.baseurl }}).

requirements-list:
  - item: "**The `CREATEROLE` or `SUPERUSER` privilege.** Either permission is required to create a database user for Stitch."
  - item: |
      **If using Log-based Replication**, you'll need:

      - **A database running PostgreSQL 9.4 or greater** Earlier versions of PostgreSQL do not include logical replication functionality, which is required for Log-based Replication.
      - **The `SUPERUSER` privilege.** If using logical replication, this is required to define the appropriate server settings.
      - **To connect to the master instance.** Log-based replication will only work on master instances due to a feature gap in PostgreSQL 10. [Based on their forums](https://commitfest.postgresql.org/12/788/){:target="new"}, PostgreSQL is working on adding support for using logical replication on a read replica to a future version.
  - item: |
      **If you're not using Log-based Replication**, you'll need:

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
      - title: "Install the wal2json plugin"
        anchor: "install-wal2json-plugin"
        content: |
          To use Log-based Replication for your {{ integration.display_name }} integration, you must install the [wal2json](https://github.com/eulerto/wal2json){:target="new"} plugin. The wal2json plugin outputs JSON objects for logical decoding, which Stitch then uses to perform Log-based Replication.

          Steps for installing the plugin vary depending on your operating system. Instructions for each operating system type are in the wal2json's GitHub repository:

          - [Unix-based operating systems](https://github.com/eulerto/wal2json#unix-based-operating-systems)
          - [Windows](https://github.com/eulerto/wal2json#windows)

          After you've installed the plugin, you can move onto the next step.

      - title: "Edit the client authentication file"
        anchor: "edit-client-authentication-file"
        content: |
          {% capture record-lines %}
          {% for ip-address in ip-addresses %}host replication [stitch_username] {{ ip-address.ip | strip }} md5
          {% endfor %}
          {% endcapture %}

          {% assign all-record-lines = record-lines | strip %}

          Usually named `pg_hba.conf`, [this file controls how clients authenticate to the {{ integration.display_name }} database](https://www.postgresql.org/docs/9.4/static/auth-pg-hba-conf.html){:target="new"}. To ensure Stitch can read the output from the wal2json plugin, you'll need to add replication connection rules to this file. These rules translate to _"Allow the Stitch user from this IP address to perform replication on all the databases it has access to."_

          1. Log into your {{ integration.display_name }} server as a superuser.
          2. Locate the `pg_hba.conf` file, usually stored in the database cluster's data directory. You can also locate this file by checking the value of the `hba_file` server parameter.
          3. Add the following lines to `pg_hba.conf`:

             ```conf
             {{ all-record-lines }}
             ```

             A rule for each of Stitch's IP addresses must be added to `pg_hba.conf`. As Stitch can use any one of these IP addresses to connect during the extraction process, each of them must have their own replication connection rule.

      - title: "Edit the database configuration file"
        anchor: "configure-database-parameters"
        content: |
          {% include integrations/databases/setup/binlog/vanilla-postgres.html %}

      - title: "Restart the {{ integration.display_name }} service"
        anchor: "restart-database-service"
        content: |
          After you've finished [editing the pg_hba.conf file](#edit-client-authentication-file) and [configuring the database settings](#configure-database-parameters), restart your {{ integration.display_name }} service to ensure the changes take effect.

      - title: "Create a replication slot"
        anchor: "create-replication-slot"
        content: |
          {% include integrations/databases/setup/binlog/postgres-replication-slot.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
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

      - title: "Define the Log-based Replication setting"
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