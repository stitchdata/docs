---
title: Facebook Ads
permalink: /integrations/saas/facebook-ads
tags: [saas_integrations]
keywords: facebook ads, integration, schema, etl facebook ads, facebook ads etl
summary: "Connection instructions, replication info, and schema details for Stitch's Facebook Ads integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "facebook-ads"
display_name: "Facebook Ads"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: 

# this-version: 1.0

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true # Stitch-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
auth: "oauth"
status-url: "https://developers.facebook.com/status/"
icon: /images/integrations/icons/facebook-ads.svg
whitelist:
  tables: true
  columns: true

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
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Verify your access in Facebook Ads.** If the user who creates the integration has restricted permissions - meaning the user doesn't have access to all campaigns or ads - Stitch may encounter issues replicating data.

      Even if you only intend to sync certain pieces of data post-setup, the user completing the initial setup should still have full access.
  - item: |
      **Pause all ad-blocking software currently in use.** Because Facebook authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup.

setup-steps:
  - title: "add integration"
    substeps:
      - title: "Select an attribution window"
        anchor: "select-attribution-window"
        content: |
          An attribution window is the amount of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted.

          We recommend selecting the [same attribution window you use in Facebook Ads](https://www.facebook.com/business/help/458681590974355) to prevent discrepancies between Facebook's UI and data replicated by Stitch. For example: If the attribution window in Facebook Ads is **7 days**, you should define this setting as **7 days**.

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

          To help prevent overages or unnecessary re-replication, consider setting the integration to replicate less frequently. For example: every 12 or 24 hours.
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

---
{% assign integration = page %}
{% include misc/data-files.html %}