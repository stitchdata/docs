---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: FullStory (v1.0)
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

# this-version: "1.0"

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

table-selection: false
column-selection: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A FullStory account with the Data Export Pack add-on**. The [Data Export Pack](https://help.fullstory.com/technical-questions/data-export) is a paid add-on for FullStory accounts that enables you to export raw event data.

      This add-on is required to replicate data using FullStory's Data Export REST API.

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API key"
    anchor: "retrieve-fullstory-api-key"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click the **user menu (three dots, upper right corner) > Settings**.
      3. Click **Integrations & API Keys** in the menu on the left side of the page.
      4. Click **API Key**:

         ![Retrieve your API key in FullStory]({{ site.baseurl }}/images/integrations/fullstory-api-key.png)
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

  - title: "Data loading and Append-Only Replication"
    anchor: "data-loading-append-only"
    content: |
      When Stitch loads the extracted data for {{ integration.display_name }} events into your destination, it will do so using Append-Only Replication. This is a type of Incremental Replication where existing rows aren't updated, but appended to the end of the table.

      For {{ integration.display_name }}, this means that every captured event is equal to a single row in the `events` table. Using this data, you can view a given user's event history and construct a timeline of their actions.

      #### Example: Create a user session timeline {#append-only-example}

      The table below contains what sample data might look like for a user who changes their address during a session:

      ![]({{ site.baseurl }}/images/integrations/fullstory-append-only-example.png)

      Using this data, we can put together the order of events for this user's session:

      1. The user clicks (`EventType: click`) the `Update Address` button on the page at `https://example.com/my-account`.
      2. Next, the user clicks in the `Street address` text field on the page at `https://example.com/update-address`.
      3. The user changes (`EventType: change`) the text in the `Street address` field to `1339 Chestnut Street` on the page at `https://example.com/update-address`.
      4. Lastly, the user clicks the `Save Changes` button on the page at `https://example.com/update-address`.
---
{% assign integration = page %}
{% include misc/data-files.html %}