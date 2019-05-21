---
title: Wootric (v1.0)
permalink: /integrations/saas/wootric
keywords: wootric, integration, schema, etl wootric, wootric etl, wootric schema
summary: "Connection instructions and schema details for Stitch's Wootric integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "wootric"
display_name: "Wootric"

singer: true
repo-url: https://github.com/singer-io/tap-wootric

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Deprecated"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 

table-selection: false
column-selection: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #


setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API credentials"
    anchor: "retrieve-api-creds"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click the **user menu** in the top right corner, then **Settings**.
      3. Click **API** in the left nav tab.
      4. Your Client ID and Client Secret will display:

         ![Wootric API credentials.]({{ site.baseurl }}/images/integrations/wootric-api-credentials.png)

      Leave this page open for now - you'll need it to complete the setup in Stitch.
  - title: "add integration"
    content: |
      4. In the **Client ID** field, paste your {{ integration.display_name }} Client ID.
      5. In the **Client Secret** field, paste your {{ integration.display_name }} Client Secret.
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
