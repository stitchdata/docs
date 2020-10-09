---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: FullStory (v1)
permalink: /integrations/saas/fullstory
keywords: fullstory, integration, schema, etl fullstory, fullstory etl, fullstory schema
summary: "Connection instructions, replication info, and schema details for Stitch's FullStory integration."
layout: singer

key: "fullstory-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "fullstory"
display_name: "FullStory"
singer: true 
repo-url: https://github.com/singer-io/tap-fullstory

this-version: "1"

api: |
  [{{ integration.display_name }} Data Export REST API](https://help.fullstory.com/develop-rest/data-export-api){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: https://fullstory.statuspage.io/

api-type: "platform.fullstory"

anchor-scheduling: true
cron-scheduling: true

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration relies on the Data Export pack add-on to replicate data through the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **A {{ integration.display_name }} account with the Data Export Pack add-on**. The [Data Export Pack](https://help.fullstory.com/technical-questions/data-export) is a paid add-on for {{ integration.display_name }} accounts that enables you to export raw event data.

      This add-on is required to replicate data using {{ integration.display_name }}'s Data Export REST API.

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

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **API Key** field, paste your {{ integration.display_name }} API key.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/fullstory

replication-sections:
  - title: "Data updates and FullStory data export bundles"
    anchor: "data-updates-fullstory-data-export-bundles"
    content: |
      {{ integration.display_name }} data bundles event data together based on a time period setting you define. By default, a {{ integration.display_name }} data bundle contains data about events that occurred during a 24 hour period.

      **Note**: {{ integration.display_name }} makes event bundles available 24 hours the last event in the bundle occurs.

      For example: If your bundle period is set to 6 hours, a data export bundle for events that occur on June 1 between 12:00PM - 6:00PM will be available the following day, June 2, at 6:00PM.

      #### Impact on Stitch replication

      Because {{ integration.display_name }} only makes event data available a full day after events have occurred, records for the current date will only ever be available the next day. Event data that is one day old is considered "up to date" for this integration.

  - title: "Loading data using Append-Only loading"
    anchor: "data-loading-append-only"
    content: |
      When Stitch loads the extracted data for {{ integration.display_name }} events into your destination, it will do so using Append-Only loading. This is a type of loading behavior where existing rows aren't updated, but appended to the end of the table. **Note**: Loading will be append-only even if the destination you're using supports Upsert loading.

      Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

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