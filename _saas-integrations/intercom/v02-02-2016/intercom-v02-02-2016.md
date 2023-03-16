---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Intercom (v02-02-2016)
permalink: /integrations/saas/intercom/v02-02-2016
keywords: intercom, integration, schema, etl intercom, intercom etl, intercom schema
summary: "Connection instructions, replication info, and schema details for Stitch's Intercom integration."
layout: singer
input: false

key: "intercom-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "intercom"
display_name: "Intercom"
singer: false
status-url: "https://status.intercom.io/"

this-version: "02-02-2016"

api: |
  [{{ integration.display_name }} REST API (V1.0)](https://developers.intercom.com/intercom-api-reference/v1.0/reference){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

anchor-scheduling: true
cron-scheduling: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false


# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Intercom's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

replication-notes: true
attribution-window: "30 days"

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**Your Intercom App ID.** You can find your Intercom App ID by following [these instructions](https://docs.intercom.com/faqs-and-troubleshooting/getting-set-up/where-can-i-find-my-app-id)."

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Intercom App ID** field, enter your [Intercom App ID](https://docs.intercom.com/faqs-and-troubleshooting/getting-set-up/where-can-i-find-my-app-id).
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to Access Intercom"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to Intercom's website to complete the setup.

      {% include layout/inline_image.html type="right" file="integrations/intercom-access-request.png" alt="List of permissions requested by Stitch to access Intercom" max-width="400px" %}1. If you aren't already logged into Intercom, you'll be prompted to do so.
      2. Next, a screen requesting access to Intercom will display. **Note**: Stitch will only ever read your data.
      3. Click **Connect.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.


# -------------------------- #
#         Replication        #
# -------------------------- #

replication-sections:
  - title: "attribution window"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/intercom
---

{% assign integration = page %}
{% include misc/data-files.html %}