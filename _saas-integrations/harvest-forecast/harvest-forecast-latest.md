---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Harvest Forecast (v1)
permalink: /integrations/saas/harvest-forecast
keywords: harvest, forecast, integration, schema, etl harvest forecast, harvest forecast etl, harvest forecast schema
summary: "Connection instructions, replication info, and schema details for Stitch's Harvest Forecast integration."
layout: singer

key: "harvest-forecast-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "harvest-forecast"
display_name: "Harvest Forecast"
singer: true 
repo-url: https://github.com/singer-io/tap-harvest-forecast

this-version: "1"

api: |
  [{{ integration.display_name }} Experimental API](https://help.getharvest.com/forecast/faqs/faq-list/api/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "60 minutes"
tier: "Standard"
status-url: https://www.harveststatus.com/

api-type: "platform.harvest-forecast"

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A Harvest account with access to Harvest Forecast**. Your Harvest ID will be used to authorize the integration using OAuth.

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. Enter your Harvest Forecast account ID in the **Harvest Forecast Account ID** field. For example: If your Harvest Forecast account shows the URL as `forecastapp.com/123456/schedule/projects`, you'd enter `123456` in this field.
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

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