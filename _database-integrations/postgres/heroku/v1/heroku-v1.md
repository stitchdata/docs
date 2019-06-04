---
title: Heroku (v1.0)
keywords: heroku, heroku-postgres, database integration, etl heroku, heroku etl
permalink: /integrations/databases/heroku/v1
summary: "Connect and replicate data from your Heroku database using Stitch's Heroku integration."
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://postgres.topostgres.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "heroku"
display_name: "Heroku"

singer: true
tap-name: "Postgres"
repo-url: "https://github.com/singer-io/tap-postgres"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

frequency: "30 minutes"
tier: "Free"
port: 5432
db-type: "postgres"

## Stitch features

versions: "9.3+"
ssh: false
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

log-based-replication-minimum-version: "n/a"
log-based-replication-master-instance: false
log-based-replication-master-instance-reason: &not-supported "Heroku doesn't currently support logical replication."

log-based-replication-read-replica: false
log-based-replication-read-replica-reason: *not-supported

## Other Replication Methods

key-based-incremental-replication: true
full-table-replication: true

view-replication: true


# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

notice-first-line: "**Heroku as an input data source**"
notice-copy: |

  This article describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting a {{ integration.display_name }} Destination guide]({{ link.destinations.setup.heroku-postgres | prepend: site.baseurl }}).

setup-steps:
  - title: "Locate the database connection details in {{ integration.display_name }}"
    anchor: "retrieve-postgres-credentials"
    content: |
      {% include shared/connection-details/heroku.html %}

  - title: "Connect Stitch"
    anchor: "connect-stitch"
    content: |
      In this step, you'll complete the setup by entering the database's connection details and defining replication settings in Stitch.

    substeps:
      - title: "Define the database connection details in Stitch"
        anchor: "define-connection-details"
        content: |
          {% include shared/database-connection-settings.html type="general" %}

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