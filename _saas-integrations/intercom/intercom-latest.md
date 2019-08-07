---
title: Intercom
permalink: /integrations/saas/intercom
keywords: intercom, integration, schema, etl intercom, intercom etl, intercom schema
summary: "Connection instructions, replication info, and schema details for Stitch's Intercom integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "intercom"
display_name: "Intercom"
singer: false
status-url: "https://status.intercom.io/"

api: |
  [{{ integration.display_name }} REST API (V1.0)](https://developers.intercom.com/intercom-api-reference/v1.0/reference){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"

table-selection: false
column-selection: false

anchor-scheduling: true
cron-scheduling: false

extraction-logs: false
loading-reports: true

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
  - title: "add integration"
    content: |
      4. In the **Intercom App ID** field, enter your [Intercom App ID](https://docs.intercom.com/faqs-and-troubleshooting/getting-set-up/where-can-i-find-my-app-id).
  - title: "historical sync"
  - title: "replication frequency"
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