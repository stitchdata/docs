---
title: Heroku
keywords: heroku, heroku-postgres, database integration, etl heroku, heroku etl
tags: [database_integrations]
permalink: /integrations/databases/heroku
summary: "Connect and replicate data from your Heroku database using Stitch's Heroku integration."
microsites:
  - title: "{{ page.display_name }} to Postgres"
    url: "http://mysql.topostgres.com/"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "heroku"
display_name: "Heroku"
author: "Stitch"
author-url: "https://www.stitchdata.com"

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

versions: "n/a"
ssh: false
ssl: true
sync-views: true
whitelist:
  tables: true
  columns: true

binlog-replication: false

# -------------------------- #
#     Setup Instructions     #
# -------------------------- #

notice: |
  This article describes how to connect Heroku-Postgres <strong>as an input data source.</strong><br><br>

  If you want to connect Heroku-Postgres <strong>as a data warehouse,</strong> refer to the [Connecting a Heroku-Postgres Destination guide]({{ link.destinations.setup.heroku-postgres | prepend: site.baseurl }}).

setup-steps:
  - title: "Retrieve Your Postgres Credentials from Heroku"
    anchor: "retrieve-postgres-credentials"
    content: |
      If you haven’t logged into your Heroku app yet, do so now. After you’re logged in, do the following to retrieve your Heroku Postgres database credentials:

      1. In the main dashboard section of the Heroku app, locate the **Add-ons** section. Add-ons will list any Postgres databases currently added to your Heroku account.
      2. Click the name of the database you want to connect to Stitch.
      3. The credentials needed to connect to Stitch will display in the Connection Settings section. 
      4. To finish the setup, you’ll need the **Host, Database, User, Port**, and **Password**. Click **Show** to display the password.

      Here’s a look at the credentials page:

      ![Heroku database credentials page.]({{site.baseurl}}/images/integrations/heroku-credentials-page.png)

      Leave this open for now - you'll need it in the next step to complete the setup.

  - title: "connect stitch"

  - title: "replication frequency"

  - title: "sync data"
---
{% assign integration = page %}
{% include misc/data-files.html %}