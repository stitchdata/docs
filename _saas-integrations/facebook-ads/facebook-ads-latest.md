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

          While we generally recommend selecting the [same attribution window you use in Facebook Ads](https://www.facebook.com/business/help/458681590974355) to reduce discrepancies between Facebook's UI and data replicated by Stitch, we understand that clicks and views may have different attribution settings in Facebook.

          In this case, you should select the **greater** of the two. For example: If clicks have a window of 7 days and views have a window of 1 day, you should select **27 days** as the setting in Stitch. Then, during every replication job, Stitch will replicate **the past seven days' worth of data** to account for result attribution. This will ensure that records updated during the attribution period are correctly captured by Stitch.

          For more info, see the [Attribution windows and data extraction](#attribution-windows-data-extraction) section.
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
      {% include note.html content="The info in this section only applies to tables using Incremental Replication. Tables using Full Table Replication replicate fully during each replication job and don't use attribution windows." %}

      When Stitch runs a replication job for {{ integration.display_name }}, it will use the value of the **Attribution Window** setting to query for and extract data for Incremental tables. An attribution window is a period of time for attributing results to ads and the lookback period after those actions occur during which ad results are counted.

      For example: If set to **7 days**, Stitch will replicate the past seven days' worth of data every time a replication job runs. While Stitch replicates data in this way to account for updates to records made during the attribution window, it can have a [substantial impact on your overall row usage](#attribution-window-row-count-impact).

      In the sections below are examples of how attribution windows impact how Stitch extracts data during historical and ongoing replication jobs.

      <ul id="profileTabs" class="nav nav-tabs">
          <li class="active">
              <a href="#historical-replications" data-toggle="tab">Historical and full re-replications</a>
          </li>
          <li>
              <a href="#ongoing-replications" data-toggle="tab">Ongoing replications</a>
          </li>
      </ul>
      <div class="tab-content">
      <div role="tabpanel" class="tab-pane active" id="historical-replications">
      <p>For historical and full resyncs of {{ integration.display_name }} data, Stitch will query for and extract data newer than or equal to the date defined in the <strong>Start Date</strong> field in the Integration Settings page.</p>

      <p>The <a href="#define-historical-sync"><strong>Start Date</strong></a> defines the minimum date Stitch should query for when extracting historical data.</p>

      <p><strong>Example</strong><br>

      During the initial set up, the <strong>Start Date</strong> field is set to <code>07/03/2017</code>, or <code>2017-07-03 00:00:00</code>. In this example, Stitch will query for data that is newer than or equal to <code>2017-07-03 00:00:00</code>.</p>

      <p>If you were to write a SQL query using this date for the <code>ads</code> table, it might look like this:</p>

      {% highlight sql %}
        SELECT *
          FROM facebook_ads.ads
         WHERE updated_time >= '2017-07-03 00:00:00'   /* Replication Key column */
      ORDER BY updated_time
      {% endhighlight %}
      </div>

      <div role="tabpanel" class="tab-pane" id="ongoing-replications">
      <p>For ongoing replication jobs, Stitch will query for and extract data using the last saved maximum value in the table's Replication Key column and the <strong>Attribution Window</strong> setting.</p>

      <p><strong>Note:</strong> This applies to every replication job that takes place after the historical replication job.</p>

      <p><strong>Example</strong><br>

      The last maximum saved Replication Key value for the <code>ads</code> table is <code>2017-10-01 00:00:00</code>.</p>

      <p>To account for an attribution window of <strong>7 days</strong>, we'd subtract this from the last maximum saved Replication Key value. This would equal <code>2017-09-24 00:00:00</code>. In this case, Stitch would query for and extract data that is newer than or equal to <code>2017-09-24 00:00:00</code> and older than or equal to <code>2017-10-01 00:00:00</code>.</p>

      <p>If this were a SQL query, it might look like this:</p>

      {% highlight sql %}
        SELECT *
          FROM facebook_ads.ads
         WHERE updated_time >= '2017-09-24 00:00:00'
                                /* max Replication Key value - 7 day attribution window */
           AND updated_time <= '2017-10-01 00:00:00'
                                /* max Replication Key value from previous job */
      ORDER BY updated_time
      {% endhighlight %}
      </div>
      </div>

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