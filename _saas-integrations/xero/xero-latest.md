---
title: Xero
permalink: /integrations/saas/xero
tags: [saas_integrations]
keywords: xero, integration, schema, etl xero, xero etl, xero schema
summary: "Connection instructions and schema details for Stitch's Xero integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "xero"
display_name: "Xero"
singer: true
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.xero.com"

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "1 hour"
tier: "Premium"
icon: /images/integrations/icons/xero.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
    # content: |
      # starting with 4., add instructions for additional fields in UI
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "authorize-stitch"
    content: |
      Lastly, you'll be directed to Xero's website to complete the setup.

      1. Enter your Xero credentials and click **Login**.
      2. A screen asking for authorization to Xero will display. **Note that Stitch will only ever read your data.**
      3. From the dropdown menu, select the company you want to connect to Stitch.
      3. Click **Authorise.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

# -------------------------- #
#    Replication Details     #
# -------------------------- #

# replication-sections:
#   - title: ""
#     anchor: ""
#     content: |
#       Xero has a daily limit of 5,000 calls in a rolling 24 hour window, and will return a 503 Service Unvailable error if exceeded. This is on a per organization basis.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/xero

---
{% assign integration = page %}
{% include misc/data-files.html %}