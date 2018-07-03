---
title: Urban Airship
permalink: /integrations/saas/urban-airship
tags: [saas_integrations]
keywords: urban airship, integration, schema, etl urban airship, urban airship etl, urban airship schema
summary: "Connection instructions and schema details for Stitch's Urban Airship integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "urban_airship"
display_name: "Urban Airship"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-urban-airship
status-url: https://twitter.com/urbanairship

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/urban-airship.svg

## Features in Stitch

whitelist:
  tables: false
  columns: false
anchor-scheduling: true
cron-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To verify your Urban Airship API access.** Urban Airship limits API access based on their product plans, meaning some plans have access while others do not.

      If you create an Urban Airship integration and Stitch displays a `401 Unauthorized` or `403 Forbidden` error, you may not have access to Urban Airship's API.

requirements-info: "We recommend reaching out to Urban Airship support to confirm your API access level before beginning the setup in Stitch."

setup-steps:
  - title: "Retrieve Your Urban Airship App Credentials"
    anchor: "retrieve-app-creds"
    content: |
      {% include note.html content="**Connect Multiple Urban Airship Apps**<br>If you want to connect multiple Urban Airship apps to Stitch, you will need to create a separate Urban Airship integration for each app. App credentials are app-specific, meaning only a single app can be connected per Stitch integration." %}

      1. Sign into your Urban Airship account.
      2. In the dashboard, open the app you want to connect to Stitch.
      3. If the Engage tab doesn't open, click **Engage** at the top to open it.
      4. Click the **gear icon** located near **Reports**, then select **APIs & Integrations**.
      5. The APIs & Integrations page will display.

      Leave this page open for now - you'll need it to complete the setup.

  - title: "add integration"
    content: |
      4. In the **App Key** field, paste your Urban Airship App Key.
      5. In the **App Secret** field, paste your Urban Airship App Secret.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/urban-airship

---
{% assign integration = page %}
{% include misc/data-files.html %}