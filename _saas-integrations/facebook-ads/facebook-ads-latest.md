---
title: Facebook Ads (v1.0)
permalink: /integrations/saas/facebook-ads
keywords: facebook ads, integration, schema, etl facebook ads, facebook ads etl
summary: "Connection instructions, replication info, and schema details for Stitch's Facebook Ads integration."
layout: singer

key: "facebook-ads-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "facebook-ads"
display_name: "Facebook Ads"
singer: true
repo-url: https://github.com/singer-io/tap-facebook

this-version: "1.0"

api: |
  [Facebook Marketing API](https://developers.facebook.com/docs/marketing-apis){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true # Stitch-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
auth: "oauth"
status-url: "https://developers.facebook.com/status/"

anchor-scheduling: true
cron-scheduling: false

table-selection: true
column-selection: true

extraction-logs: true
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

## FB's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during
## this time.

replication-notes: true
attribution-window: "28 days"
attribution-is-configurable: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates ad, campaign, and adcreative data using the {{ integration.api | flatify | strip }}.

  **Note**: This integration does not currently support replicating data for reviews, pages, etc.

  Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Verify your access in {{ integration.display_name }}.** If the user who creates the integration has restricted permissions - meaning the user doesn't have access to all campaigns or ads - Stitch may encounter issues replicating data.

      Even if you only intend to sync certain pieces of data post-setup, the user completing the initial setup should still have full access.
  - item: |
      **Pause all ad-blocking software currently in use.** Because Facebook authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup.

setup-steps:
  - title: "add integration"
    substeps:
      - title: "Select an attribution window"
        anchor: "select-attribution-window"
        content: |
          {% include misc/icons.html %}

          An attribution window is the amount of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted.

          We recommend selecting the [same attribution window you use in {{ integration.display_name }}](https://www.facebook.com/business/help/458681590974355){:target="new"} to prevent discrepancies between Facebook's UI and data replicated by Stitch. For example: If the attribution window in {{ integration.display_name }} is **7 days**, you should define this setting as **7 days**.

          Then, during every replication job, Stitch will replicate **the past seven days' worth of data** to account for result attribution. This will ensure that records updated during the attribution period are correctly captured by Stitch.

          For more info, see the [Attribution windows and data extraction](#attribution-windows-data-extraction) section.

          {% capture different-windows %}
          In this case, you should select the **greater** of the two. For example: If clicks have a window of 7 days and views have a window of 1 day, you should select **7 days** as the setting in Stitch. This will ensure that the values for clicks and views are correctly updated.
          {% endcapture %}

          {% include note.html first-line="**What if clicks and views have different windows in Facebook Ads?**" content=different-windows %}

      - title: "Include deleted data"
        anchor: "include-deleted-data"
        content: |
          Check the **Include data from deleted campaigns, ads, and adsets** box to have Stitch replicate data for these deleted objects.

          **Note**: Data for deleted campaigns, ads, and adsets will be included only in [**Core Object**](#schema) tables.

  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access Facebook Ads"
    anchor: "grant-stitch-authorization"
    content: |
      1. After clicking the **Authorize** button, a small pop-up window will display.

         You'll be taken through a series of steps to allow Stitch to access data from your Public Profile, Facebook Ads, and related stats. 
      2. Click **Okay** to advance through these steps.
      3. After you've finished authorizing Stitch, you'll be prompted to select the Facebook Ad Account you want to pull data from. Select the desired account by clicking the checkbox in the **Connect** column.

         If you don't see the profiles that you would expect to, verify your Facebook Ads permissions before reaching out to support.
      3. Click the **Save Connections** button.

      After your credentials are validated, you'll be directed back to Stitch (click the {{ app.buttons.finish-int-setup }} button to wrap things up) and the {{ app.page-names.int-details }} page will display.
  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Attribution windows and data extraction"
    anchor: "attribution-windows-data-extraction"
    content: |
      {% include note.html type="single-line" content="The info in this section only applies to tables using Incremental Replication. Tables using Full Table Replication replicate fully during each replication job and don't use attribution windows." %}

      When Stitch runs a replication job for {{ integration.display_name }}, it will use the value of the **Attribution Window** setting to query for and extract data for Incremental tables. An attribution window is a period of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted.

      For example: If set to **7 days**, Stitch will replicate the past seven days' worth of data every time a replication job runs. While Stitch replicates data in this way to account for updates to records made during the attribution window, it can have a [substantial impact on your overall row usage](#attribution-window-row-count-impact).

      In the sections below are examples of how attribution windows impact how Stitch extracts data during historical and ongoing replication jobs.

      {% include integrations/saas/ads-append-only-replication.html type="report-tables" %}

    subsections:
      - title: "Attribution windows and row count impact"
        anchor: "attribution-window-row-count-impact"
        content: |
          Due to the attribution window, a high Replication Frequency may not be necessary. Because Stitch will replicate data from the past `N` days during every replication job, recent data will be re-replicated and count towards your row quota.

          To reduce your row usage and replicating redundant data, consider setting the integration to replicate less frequently. For example: every 12 or 24 hours.
# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/facebook-ads

schema-sections:
  - content: |
      There are two types of tables in Stitch’s {{ integration.display_name }} integration: Core Object and Insights.

      - **Core Object** tables contain foundational data that's useful for analysis. These are the [`adcreative`](#adcreative), [`ads`](#ads), [`adsets`](#adsets), and [`campaigns`](#campaigns) tables. To learn more about how Facebook Ads data is structured, we recommend checking out their [API guide](https://developers.facebook.com/docs/marketing-api/buying-api).
      - **Insights** tables contain performance data for every campaign/adset/ad combination, segmented by day and demographics specific to each table. For example: The [`ads_insights_age_and_gender`](#ads_insights_age_and_gender) table is segmented by day, age, and gender.

# This is used in the schema sections to display values that have
# been deprecated for specific fields.

cost-per-action-type:
  description: |
    The kind of actions taken on the ad, Page, app, or event after your ad was served to someone, even if they didn't click on it.

    Action types include Page likes, app installs, conversions, event responses, and more.

  deprecated-common-october-2018: |
    - `app_custom_event_fb_mobile_add_to_cart` 
    - `app_custom_event_fb_mobile_add_to_wishlist`
    - `app_custom_event_fb_mobile_initiated_checkout`
    - `app_custom_event_fb_mobile_search`
    - `app_custom_event_fb_mobile_complete_registration`
    - `app_custom_event_fb_mobile_achievement_unlocked`
    - `app_custom_event_fb_mobile_add_payment_info`
    - `app_custom_event_fb_mobile_content_view`
    - `app_custom_event_fb_mobile_level_achieved`
    - `app_custom_event_fb_mobile_purchase`
    - `app_custom_event_fb_mobile_rate`
    - `app_custom_event_fb_mobile_spent_credits`
    - `app_custom_event_fb_mobile_tutorial_completion`

  deprecated-july-2018: |
    - `mention`
    - `tab_view`

  deprecated-october-2018: |
    {{ integration.cost-per-action-type.deprecated-common-october-2018 | flatify }}
    - `app_install`
    - `mobile_app_install`
    - `onsite_conversion.add_to_cart`
    - `onsite_conversion.view_content`

cost-per-unique-action-type:
  deprecated-july-2018: |
    - `app_custom_event`
    {{ integration.cost-per-action-type.deprecated-july-2018 | flatify }}

  deprecated-october-2018: |
    {{ integration.cost-per-action-type.deprecated-common-october-2018 | flatify }}
---
{% assign integration = page %}
{% include misc/data-files.html %}