---
title: Mixpanel
permalink: /integrations/saas/mixpanel
keywords: mixpanel, integration, schema, etl mixpanel, mixpanel etl, mixpanel schema
tags: [saas_integrations]
summary: "Connection instructions, replication info, and schema details for Stitch's Mixpanel integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "mixpanel"
display_name: "Mixpanel"
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.mixpanel.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "7 days"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/mixpanel.svg
whitelist:
  tables: true
  columns: false

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## 2 out of 3 of Mixpanel's tables can only be
## queried by day. Details are in the Replication section, below.

replication-notes: true

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## incompatible:
##  bigquery: "sometimes"
##  reason: "Mixpanel sometimes sends records that contain multiple data types. BigQuery only allows `FLOAT` and `DOUBLE` data types in the same column; otherwise, the field will be rejected."

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
    nested-structures: false
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
    replication-method: "Incremental"
    primary-key: "event:time:distinct_id:_sdc_record_hash"
    nested-structures: true
    attributes:
      - name: distinct_id
      - name: event *
      - name: mp_country_code
      - name: mp_lib
      - name: mp_reserved_browser
      - name: mp_reserved_browser_version
      - name: mp_reserved_city
      - name: mp_reserved_current_url
      - name: mp_reserved_initial_referrer
      - name: mp_reserved_initial_referring_domain
      - name: mp_reserved_lib_version
      - name: mp_reserved_reserved_os
      - name: mp_reserved_region
      - name: mp_reserved_screen_height
      - name: mp_reserved_screen_width
      - name: time
      - name: _sdc_record_hash

## Funnels
  - name: "mixpanel_funnels"
    doc-link: https://mixpanel.com/help/reference/data-export-api#funnels
    description: "contains info about your Mixpanel funnels."
    notes: *replication
    replication-method: "Incremental"
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
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% capture sync-limit %}
{% include important.html content="**Historical Syncs & Mixpanel Limitations**<br>
Mixpanel limits the queryable time range for some of its endpoints to either **60 or 90 days** [to prevent poor loading times for their customers](https://mixpanel.com/help/questions/articles/why-do-the-dates-switch-and-show-only-two-or-three-months-of-data-at-a-time-in-certain-reports). We've found if the Start Date is greater than this, some Historical Syncs may not complete successfully.<br><br>

If you notice issues with the historical sync of a Mixpanel integration, check that the historical sync is set to start **no more than 60 days in the past**. Changing this setting can sometimes resolve the issue." %}
{% endcapture %}

{% contentfor setup %}
Connecting your Mixpanel data to Stitch is a five-step process:

1. [Retrieve your Mixpanel API credentials](#retrieve-mixpanel-api-creds)
2. [Add Mixpanel as a Stitch data source](#add-stitch-data-source)
3. [Define the Historical Sync](#define-historical-sync)
4. [Define the Replication Frequency](#define-rep-frequency)
5. [Select tables to sync](#syncing-data)

### Retrieve Your Mixpanel API Credentials {#retrieve-mixpanel-api-creds}

1. Sign into your Mixpanel account.
2. Click **Account**, which is located in the upper right portion of the screen.
3. In the modal that displays, click **Projects**. 

   Note that this window is different than the Project Settings window, which is accessed using the gear icon in the lower left corner. **The window you need is accessed only by clicking Account > Projects**.
4. Your API credentials will display:

   ![Mixpanel API credentials.]({{ site.baseurl}}/images/integrations/mixpanel-api-creds.png)

Leave this page open - you'll need it to complete the setup in Stitch.

{% include integrations/shared-setup/connection-setup.html %}
4. Paste your API credentials in the the **API Key** and **Secret** fields, respectively.

{% include integrations/saas/setup/historical-sync.html more-info=sync-limit %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/saas/setup/saas-syncing.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
Because of how Mixpanel's API is designed, two of the three tables in our Mixpanel integration - the `mixpanel_export` and `mixpanel_funnels` tables - **can only be queried by day.** This means that every time Stitch runs a replication job for a Mixpanel integration, **the past day's worth of data will be replicated for each of these tables.**

To prevent the re-replication of data that will count against your row count, we recommend setting the Replication Frequency to something less frequent.
{% endcontentfor %}
