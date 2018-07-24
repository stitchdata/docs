---
title: PostgreSQL (v15-10-2015)
keywords: postgresql, postgres, database integration, etl postgres, postgres etl, postgresql etl, etl
tags: [database_integrations]
permalink: /integrations/databases/postgresql/v15-10-2015
summary: "Connect and replicate data from your PostgreSQL database using Stitch's PostgreSQL integration."
input: false

microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostges.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "postgres"
display_name: "PostgreSQL"
author: "Stitch"
author-url: "https://www.stitchdata.com"

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
icon: /images/integrations/icons/postgresql.svg

## Stitch features

versions: "9.3+"
ssh: true
ssl: true

anchor-scheduling: false
extraction-logs: false
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: false
view-replication: true

# -------------------------- #
#    Supported Data Types    #
# -------------------------- #

## Some data type support & handling is specific to an integration's version.

## See _data/taps/data-types/postgres.yml

# -------------------------- #
#      Setup Requirements    #
# -------------------------- #

requirements-list:
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
  - title: "whitelist stitch ips"

  - title: "retrieve public key"

  - title: "create linux user"

  - title: "create db user"

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% capture postgres-dw %}This article describes how to connect PostgreSQL <strong>as an input data source.</strong>
<br><br>
If you want to connect a PostgreSQL instance <strong>as a data warehouse,</strong> refer to the [Connecting a Self-Hosted PostgreSQL Destination article]({{ link.destinations.setup.self-hosted-postgres | prepend: site.baseurl }}).
{% endcapture %}
{% include important.html content=postgres-dw %}
