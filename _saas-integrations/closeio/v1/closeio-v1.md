---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Close.io
permalink: /integrations/saas/closeio
tags: [saas_integrations]
keywords: closeio, integration, schema, etl closeio, closeio etl, closeio schema
layout: singer
# input: false

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "closeio"
display_name: "Close.io"
singer: true
tap-name: "Close.io"
repo-url: https://github.com/singer-io/tap-closeio

this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Open Beta"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Paid"
status-url: "http://status.close.io/"
icon: /images/integrations/icons/closeio.svg

anchor-scheduling: true
extraction-logs: true
loading-reports: true

table-selection: false
column-selection: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Generate a Close.io API Key"
    anchor: "generate-closeio-api-key"
    content: |
      1. Sign into your Close.io account.
      2. Click the **user menu (your icon)** in the top right corner.
      3. Click **Settings**.
      4. In the Company menu (located under the **You** menu), click **Your API Keys**.
      5. In the Your API Keys section, click the **Generate New API Key** button.
      6. A new API Key will display. Keep this handy; you’ll need it in the next step.
  - title: "add integration"
    content: |
        4. In the **API Key** field, paste your API Key.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/closeio/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}