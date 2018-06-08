---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: FullStory
permalink: /integrations/saas/fullstory
tags: [saas_integrations]
keywords: fullstory, integration, schema, etl fullstory, fullstory etl, fullstory schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "fullstory"
display_name: "FullStory"
singer: true 
repo-url: https://github.com/singer-io/tap-fullstory

# this-version: ""

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://fullstory.statuspage.io/
icon: /images/integrations/icons/fullstory.svg
whitelist:
  tables: false
  columns: false

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A FullStory account with the Data Export Pack add-on**. The [Data Export Pack](https://help.fullstory.com/technical-questions/data-export) is a paid add-on for FullStory accounts that enables you to export raw event data.

      This add-on is required to replicate data using FullStory's Data Export REST API.

requirements-info:

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API key"
    anchor: "retrieve-fullstory-api-key"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click the **user menu (three dots, upper right corner) > Settings**.
      3. Click **Integrations & API Keys** in the menu on the left side of the page.
      4. Click **API Key**:

         ![]({{ site.baseurl }}/images/integrations/fullstory-api-key.png)
      5. Your API key will display on the page. Copy the API key before closing the page.

  - title: "add integration"
    content: |
      4. In the **API Key** field, paste your {{ integration.display_name }} API key.

  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/fullstory

replication-sections:
  - title: "Data updates and FullStory data export bundles"
    anchor: "data-updates-fullstory-data-export-bundles"
    content: |
      FullStory data bundles event data together based on a time period setting you define. By default, a FullStory data bundle contains data about events that occurred during a 24 hour period.

      **Note**: FullStory makes event bundles available 24 hours the last event in the bundle occurs.

      For example: If your bundle period is set to 6 hours, a data export bundle for events that occur on June 1 between 12:00PM - 6:00PM will be available the following day, June 2, at 6:00PM.

      #### Impact on Stitch replication

      Because FullStory only makes event data available a full day after events have occurred, records for the current date will only ever be available the next day. Event data that is one day old is considered "up to date" for this integration.

      #### Configure 
---
{% assign integration = page %}
{% include misc/data-files.html %}