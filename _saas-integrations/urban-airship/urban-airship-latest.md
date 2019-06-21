---
title: Urban Airship (v1.0)
permalink: /integrations/saas/urban-airship
keywords: urban airship, integration, schema, etl urban airship, urban airship etl, urban airship schema
summary: "Connection instructions and schema details for Stitch's Urban Airship integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "urban-airship"
display_name: "Urban Airship"

singer: true
repo-url: https://github.com/singer-io/tap-urban-airship
status-url: https://twitter.com/urbanairship

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"

table-selection: false
column-selection: false

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To verify your {{ integration.display_name }} API access.** {{ integration.display_name }} limits API access based on their product plans, meaning some plans have access while others do not.

      If you create an {{ integration.display_name }} integration and Stitch displays a `401 Unauthorized` or `403 Forbidden` error, you may not have access to {{ integration.display_name }}'s API.

requirements-info: "We recommend reaching out to {{ integration.display_name }} support to confirm your API access level before beginning the setup in Stitch."

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} app credentials"
    anchor: "retrieve-app-creds"
    content: |
      {% include note.html content="**Connect Multiple Urban Airship Apps**<br>If you want to connect multiple Urban Airship apps to Stitch, you will need to create a separate Urban Airship integration for each app. App credentials are app-specific, meaning only a single app can be connected per Stitch integration." %}

      1. Sign into your {{ integration.display_name }} account.
      2. In the dashboard, open the app you want to connect to Stitch.
      3. If the Engage tab doesn't open, click **Engage** at the top to open it.
      4. Click the **gear icon** located near **Reports**, then select **APIs & Integrations**.
      5. The APIs & Integrations page will display.

      Leave this page open for now - you'll need it to complete the setup.

  - title: "add integration"
    content: |
      4. In the **App Key** field, paste your {{ integration.display_name }} App Key.
      5. In the **App Secret** field, paste your {{ integration.display_name }} App Secret.
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