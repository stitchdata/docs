---
title: Mixpanel
permalink: /integrations/saas/mixpanel
keywords: mixpanel, integration, schema, etl mixpanel, mixpanel etl, mixpanel schema
summary: "Connection instructions, replication info, and schema details for Stitch's Mixpanel integration."
layout: singer
old-schema-template: true

key: "mixpanel-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mixpanel"
display_name: "Mixpanel"
status-url: "https://status.mixpanel.com/"

this-version: "23-12-2015"

api: |
  [{{ integration.display_name }} Data Export API](https://mixpanel.com/help/reference/data-export-api#people-analytics){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "7 days"
frequency: "30 minutes"
tier: "Free"

anchor-scheduling: true
cron-scheduling: false

table-selection: true
column-selection: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: true
  lots-of-full-table: false

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## 2 out of 3 of Mixpanel's tables can only be
## queried by day. Details are in the Replication section, below.


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Engage
  - name: "mixpanel_engage"
    doc-link: https://mixpanel.com/help/reference/data-export-api#people-analytics
    description: "info from People Analytics, which will enable you to do user-level analysis. This data is only available to Mixpanel customers with a People Plan."
    notes: 
    replication-method: "Full Table"
    primary-key: "distinct_id"
    nested-structures: true
    attributes:
      - name: distinct_id
      - name: created
      - name: email
      - name: first_name
      - name: last_name
      - name: last_seen

## Exports
  - name: "mixpanel_export"
    doc-link: https://mixpanel.com/help/reference/exporting-raw-data#export-api-reference
    description: "raw event data."
    notes: &replication |
      ### Replication
      Because of how Mixpanel's API is designed, this table can only be queried by day. This means that every time Stitch runs a replication job for a Mixpanel integration, **the past day's worth of data will be replicated for this table.**
    replication-method: "Key-based Incremental"
    primary-key: "event:time:distinct_id:_rjm_record_hash"
    nested-structures: false
    attributes:
      - name: distinct_id
      - name: event
      - name: mp_country_code
      - name: mp_lib
      - name: mp_reserved_browser
      - name: mp_reserved_browser_version
      - name: mp_reserved_city
      - name: mp_reserved_current_url
      - name: mp_reserved_initial_referrer
      - name: mp_reserved_initial_referring_domain
      - name: mp_reserved_lib_version
      - name: mp_reserved_os
      - name: mp_reserved_region
      - name: mp_reserved_screen_height
      - name: mp_reserved_screen_width
      - name: time
      - name: _rjm_record_hash

## Funnels
  - name: "mixpanel_funnels"
    doc-link: https://mixpanel.com/help/reference/data-export-api#funnels
    description: "contains info about your Mixpanel funnels."
    notes: *replication
    replication-method: "Key-based Incremental"
    primary-key: "funnel_id:date"
    nested-structures: true
    attributes:
      - name: funnel_id
      - name: date
      - name: "steps<code>*</code>: count, step_conv_ratio, goal, overall_conv_ratio, avg_time, event"
      - name: analysis__completion
      - name: analysis__starting_amount
      - name: analysis__steps
      - name: analysis__worst


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API credentials"
    anchor: "retrieve-mixpanel-api-creds"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. Click **Account**, which is located in the upper right portion of the screen.
      3. In the modal that displays, click **Projects**. 

         **Note**: This window is different than the Project Settings window, which is accessed using the gear icon in the lower left corner. **The window you need can be accessed only by clicking Account > Projects**.
      4. Your API credentials will display:

         ![Mixpanel API credentials.]({{ site.baseurl}}/images/integrations/mixpanel-api-creds.png)

         Leave this page open - you'll need it to complete the setup in Stitch.
  - title: "add integration"
    content: |
      4. Paste your API credentials in the the **API Key** and **Secret** fields, respectively.
  - title: "Define the historical sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
      
      **Note**: {{ integration.display_name }} limits the number of days historical data may be accessed, depending on your {{ integration.display_name }} plan. If you select a Start Date greater than what your {{ integration.display_name }} account has access to, the {{ integration.display_name }} API will return an error and prevent Stitch from extracting data.
      
      For example: If you have a Starter Free {{ integration.display_name }} plan, you have access to 90 days of historical data (as of 04/28/2020). If you select a Start Date greater than 90 days, {{ integration.display_name }}'s API will prevent Stitch from extracting your data.
      
      Refer to [{{ integration.display_name }}'s documentation](https://help.mixpanel.com/hc/en-us/articles/115004511246){:target="new"} for more info and to check your {{ integration.display_name }} account's historical data access limit.
  - title: "replication frequency"
  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      Because of how Mixpanel's API is designed, two of the three tables in the {{ integration.display_name }} integration - the `mixpanel_export` and `mixpanel_funnels` tables - can only be queried by day. 

      This means that every time Stitch runs a replication job for a Mixpanel integration, the past day's worth of data will be replicated for each of these tables.

      To prevent the re-replication of data that will count against your row count, we recommend setting the Replication Frequency to something less frequent.
---
{% assign integration = page %}
{% include misc/data-files.html %}
