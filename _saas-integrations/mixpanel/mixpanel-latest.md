---
title: Mixpanel
permalink: /integrations/saas/mixpanel
keywords: mixpanel, integration, schema, etl mixpanel, mixpanel etl, mixpanel schema
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
status-url: "https://status.mixpanel.com/"

api: |
  [{{ integration.display_name }} Data Export API](https://mixpanel.com/help/reference/data-export-api#people-analytics){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
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

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## 2 out of 3 of Mixpanel's tables can only be
## queried by day. Details are in the Replication section, below.

replication-notes: true

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
---
{% assign integration = page %}
{% include misc/data-files.html %}

{% capture sync-limit %}

{% capture sync-limit-copy %}
Mixpanel limits the queryable time range for some of its endpoints to either **60 or 90 days** [to prevent poor loading times for their customers](https://mixpanel.com/help/questions/articles/why-do-the-dates-switch-and-show-only-two-or-three-months-of-data-at-a-time-in-certain-reports). We've found if the **Start Date** is greater than this, some historical replication may not complete successfully.

If you notice issues with the historical replication of a Mixpanel integration, check that the **Start Date** is set to **no more than 60 days in the past**. Changing this setting can sometimes resolve the issue.
{% endcapture %}

{% include important.html first-line="**Historical replication and Mixpanel limitations**" content=sync-limit-copy %}
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

{% include integrations/saas/setup/historical-sync.html step-content=sync-limit %}

{% include integrations/shared-setup/replication-frequency.html %}

{% include integrations/saas/setup/saas-syncing.html %}

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}



{% contentfor replication-notes %}
Because of how Mixpanel's API is designed, two of the three tables in our Mixpanel integration - the `mixpanel_export` and `mixpanel_funnels` tables - **can only be queried by day.** This means that every time Stitch runs a replication job for a Mixpanel integration, **the past day's worth of data will be replicated for each of these tables.**

To prevent the re-replication of data that will count against your row count, we recommend setting the Replication Frequency to something less frequent.
{% endcontentfor %}
