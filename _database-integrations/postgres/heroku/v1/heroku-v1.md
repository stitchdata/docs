---
title: Heroku (v1.0)
keywords: heroku, heroku-postgres, database integration, etl heroku, heroku etl
tags: [database_integrations]
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
icon: /images/integrations/icons/heroku.svg

## Stitch features

versions: "9.3+"
ssh: false
ssl: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

binlog-replication: false
view-replication: true

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

notice-first-line: "**Heroku as an input data source**"
notice-copy: |

  This article describes how to connect {{ integration.display_name }} **as an input data source.**

  If you want to connect a {{ integration.display_name }} instance as a **destination**, refer to the [Connecting a Self-Hosted {{ integration.display_name }} Destination guide]({{ link.destinations.setup.heroku-postgres | prepend: site.baseurl }}).

setup-steps:
  - title: "Retrieve Your Postgres Credentials from Heroku"
    anchor: "retrieve-postgres-credentials"
    content: |
      1. Log into your Heroku account.
      2. On the dashboard page, click the app that contains the database you want to connect to Stitch. This will open the app's Overview page.
      3. On this page, locate the **Installed add-ons** section.
      4. Click the database you want to connect to Stitch. This will open the database's Overview page.
      5. On this page, click the **Settings** tab.
      6. In the **Database Credentials** section, click the **View Credentials** button to display the connection details. You'll need the following to complete the setup:
         - Host
         - Database
         - User
         - Port
         - Password

      Leave this page open for now - you'll need it in the next step to complete the setup.

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}