---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Mixpanel (v1)
permalink: /integrations/saas/mixpanel
keywords: mixpanel, integration, schema, etl mixpanel, mixpanel etl, mixpanel schema
layout: singer
# input: false

key: "mixpanel-setup"


# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "mixpanel"
display_name: "Mixpanel"

singer: true
status-url: ""

tap-name: "Mixpanel"
repo-url: https://github.com/singer-io/tap-mixpanel

this-version: "1"

api: |
  [{{ integration.display_name }} Event Export API & Mixpanel Query API.](https://developer.mixpanel.com/docs/mixpanel-apis){:target="new"}


# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

api-type: "platform.mixpanel"

historical: "1 year"
frequency: "1 hour"
tier: "Free"

anchor-scheduling: true
cron-scheduling: true

extraction-logs: true
loading-reports: true

table-selection: true
column-selection: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false


# setup-name: ""

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Mixpanel's attribution windows. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during
## this time.

attribution-window: "5 days"
attribution-is-configurable: true


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Incompatibilities     #
# -------------------------- #

## uncomment section below if integration is compatible with any Stitch destinations
## if incompatible with multiple destinations, create a section for each destination

## incompatible:
  ## [redshift]: "always,sometimes,never"
  ## reason: "copy" 

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin privileges**. Your role in your {{ integration.display_name }} account must be admin in order to be able to retrieve your API secret.

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} project timezone and API secret"
    anchor: "retrieve-timezone-api-secret"
    content: |
      1. Login to your {{ integration.display_name }} account.
      2. In the dropdown menu in the upper left corner of the page, select the project you want to replicate data from.
      3. Hover over the **Settings** icon in the upper right corner. In the **PROJECT SETTINGS** portion of the dropdown menu, click on the link with the name of your project.
      4. Copy the **Project Timezone** and **API Secret**, and paste those values someplace safe to use for the next step.
  - title: "add integration"
    content: |
      4. In the **API Secret** field, paste the **API Secret** you retrieved from [Step 1](#retrieve-timezone-api-secret).
      5. In the **Attribution Window** field, enter the number of days you want your tables' attribution window to be. For more information on attribution windows, refer to the [Replication section](#attribution-windows-extraction).
      6. In the **Date Window Size** field, enter the number of days desired for a date looping window for the `exports`, `funnels`, and `revenues` tables.

         Date looping will return records whose `from_date` and `to_date` fall between the number of days in the defined window size.

         **Note**: If your project has large volumes of events, you may want to set the number of days to `14`, `7`, or even to `1` or `2` days.
      7. In the **Project Timezone** field, paste the **Project Timezone** you retrieved from [Step 1](#retrieve-timezone-api-secret).
      8. **Optional**: In the **Select Properties By Default**, enter `true` to capture new properties in the `events` and `engage` tables' records. If set to `false` or left blank, new properties will be ignored.

## Max start date: https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/sync.py#L151
  - anchor: "define-historical-sync"
    content: |
      {% capture step-content %}
      **Note**: {{ integration.display_name }} limits the number of days historical data may be accessed, depending on your {{ integration.display_name }} plan. If you select a Start Date greater than what your {{ integration.display_name }} account has access to, Stitch may encounter issues with {{ integration.display_name }}'s API.
      
      For example: If you have a Starter Free {{ integration.display_name }} plan, you have access to 90 days of historical data (as of 06/5/2020). If you select a Start Date greater than 90 days, {{ integration.display_name }}'s API may return an error.

      Additionally, the Start Date must be less than or equal to **365 days**. If a Start Date greater than 365 days is selected, Stitch will reset the Start Date to 365 days during Extraction.
      
      Refer to [{{ integration.display_name }}'s documentation](https://help.mixpanel.com/hc/en-us/articles/115004511246){:target="new"} for more info and to check your {{ integration.display_name }} account's historical data access limit.
      {% endcapture %}

      {% include integrations/saas/setup/historical-sync.html step-content=step-content %}
  - title: "replication frequency"
  - title: "track data" ## remove this if the integration doesn't support at least table selection


# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Attribution windows and data extraction"
    anchor: "attribution-windows-extraction"
    content: |
      {% include note.html type="single-line" content="The info in this section only applies to tables using Key-based Incremental Replication. Tables using Full Table Replication replicate fully during each replication job and don't use attribution windows." %}

      When Stitch runs a replication job for {{ integration.display_name }}, it will use the value of the **Attribution Window** setting to query for and extract data for tables using Key-based Incremental Replication. An attribution window is a period of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted.

      For example: If set to **5 days**, Stitch will replicate the past five days' worth of data for applicable tables every time a replication job runs. While Stitch replicates data in this way to account for updates to records made during the attribution window, it can have a [substantial impact on your overall row usage](#attribution-window-row-count-impact).

      In the sections below are examples of how attribution windows impact how Stitch extracts data during historical and ongoing replication jobs.

      {% include integrations/saas/ads-append-only-replication.html %}
      {% include integrations/saas/attribution-window-examples.html %}

    subsections:
      - title: "Attribution windows and row count impact"
        anchor: "attribution-window-row-count-impact"
        content: |
          Due to the Attribution Window, a high Replication Frequency may not be necessary. Because Stitch will replicate data from the past `N` days during every replication job, recent data will be re-replicated and count towards your row quota.

          To reduce your row usage and replicating redundant data, consider setting the integration to replicate less frequently. For example: every 12 or 24 hours.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/mixpanel


# Remove this if you don't need it:
# schema-sections:
#  - title: ""
#    anchor: ""
#    content: |
---
{% assign integration = page %}
{% include misc/data-files.html %}
