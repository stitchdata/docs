---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Campaign Monitor (v1)
permalink: /integrations/saas/campaign-monitor
keywords: campaign monitor, integration, schema, etl campaign monitor, campaign monitor etl, campaign monitor schema
summary: "Connection instructions, replication info, and schema details for Stitch's Campaign Monitor integration."
layout: singer
# input: false

key: "campaign-monitor-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "campaign-monitor"
display_name: "Campaign Monitor"

singer: true 
repo-url: https://github.com/singer-io/tap-campaign-monitor

this-version: "1"

api: |
  [{{ integration.display_name }} API](https://www.campaignmonitor.com/api/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://status.campaignmonitor.com/"

api-type: "platform.campaign-monitor"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API credentials"
    anchor: "retrieve-api-credentials"
    content: |
      1. Sign into your [{{ integration.display_name }} account](https://login.createsend.com/){:target="new"}.
      2. Click the user menu (your avatar), located in the top right corner.
      3. Click **Account settings**.
      4. On the Account Settings page, click **API keys**.
      5. Locate your **Client ID**.

      Keep this page open - you'll need it to complete the next step.
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Campaign Monitor Client ID** field, paste your {{ integration.display_name }} client ID.
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account.
      2. Follow the prompts to complete the authorization process.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/campaign-monitor
---
{% assign integration = page %}
{% include misc/data-files.html %}