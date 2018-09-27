---
title: Wootric
permalink: /integrations/saas/wootric
tags: [saas_integrations]
keywords: wootric, integration, schema, etl wootric, wootric etl, wootric schema
summary: "Connection instructions and schema details for Stitch's Wootric integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "wootric"
display_name: "Wootric"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-wootric

# this-version:

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Coming Soon"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 
icon: /images/integrations/icons/wootric.svg

table-selection: false
column-selection: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #


setup-steps:
  - title: "Retrieve Your Wootric API credentials"
    anchor: "retrieve-api-creds"
    content: |
      1. Sign into your Wootric account.
      2. Click the **user menu** in the top right corner, then **Settings**.
      3. Click **API** in the left nav tab.
      4. Your Client ID and Client Secret will display:

         ![Wootric API credentials.]({{ site.baseurl }}/images/integrations/wootric-api-credentials.png)

      Leave this page open for now - you'll need it to complete the setup in Stitch.
  - title: "add integration"
    content: |
      4. In the **Client ID** field, paste your Wootric Client ID.
      5. In the **Client Secret** field, paste your Wootric Client Secret.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/wootric

---
{% assign integration = page %}
{% include misc/data-files.html %}


