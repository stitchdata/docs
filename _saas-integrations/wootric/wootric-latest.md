---
title: Wootric (v1.0)
permalink: /integrations/saas/wootric
keywords: wootric, integration, schema, etl wootric, wootric etl, wootric schema
summary: "Connection instructions and schema details for Stitch's Wootric integration."
layout: singer

key: "wootric-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "wootric"
display_name: "Wootric"

singer: true
repo-url: https://github.com/singer-io/tap-wootric

this-version: "1.0"

api: |
  [{{ integration.display_name }} API](https://docs.wootric.com/api/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: 

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

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
