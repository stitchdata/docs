---
title: Intercom
permalink: /integrations/saas/intercom
tags: [saas_integrations]
keywords: intercom, integration, schema, etl intercom, intercom etl, intercom schema
summary: "Connection instructions, replication info, and schema details for Stitch's Intercom integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "intercom"
display_name: "Intercom"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.intercom.io/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Premium"
icon: /images/integrations/icons/intercom.svg
whitelist:
  tables: false
  columns: false

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