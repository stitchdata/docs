---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Harvest Forecast
permalink: /integrations/saas/harvest-forecast
tags: [saas_integrations]
keywords: harvest, forecast, integration, schema, etl harvest forecast, harvest forecast etl, harvest forecast schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "harvest-forecast"
display_name: "Harvest Forecast"
singer: true 
repo-url: https://github.com/singer-io/tap-harvest-forecast

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "60 minutes"
tier: "Free"
status-url: https://www.harveststatus.com/
icon: /images/integrations/icons/harvest-forecast.svg

table-selection: false
column-selection: false

extraction-logs: true
loading-reports: true
anchor-scheduling: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A Harvest account with access to Harvest Forecast**. Your Harvest ID will be used to authorize the integration using OAuth.

setup-steps:
  - title: "add integration"
    content: |
      4. Enter your Harvest Forecast account ID in the **Harvest Forecast Account ID** field. For example: If your Harvest Forecast account shows the URL as `forecastapp.com/123456/schedule/projects`, you'd enter `123456` in this field.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to Access Harvest Forecast"
    anchor: "grant-stitch-authorization"
    content: |
      Lastly, you'll be directed to Harvest's website to complete the setup.

      1. If not already logged into Harvest Forecast, enter your credentials and click **Sign In**.
      2. A screen asking for authorization to Forecast will display. **Note that Stitch will only ever read your data.**
      3. Click **Connect.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/harvest-forecast

---
{% assign integration = page %}
{% include misc/data-files.html %}