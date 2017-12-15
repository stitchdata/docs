---
title: Google AdWords
permalink: /integrations/saas/google-adwords
redirect_from: /integrations/saas/google-adwords-v1
tags: [saas_integrations]
keywords: google adwords, google adwords data, etl google adwords, google adwords etl, google adwords schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google AdWords integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "google-adwords"
display_name: "Google AdWords"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-adwords

# this-version: "1.0"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

api-version: "v201702"

status: "Released"
certified: true # Stitch-supported integration

historical: "30 days"
frequency: "24 hours"
tier: "Free"
status-url: "https://www.google.com/appsstatus#hl=en&v=status"
icon: /images/integrations/icons/google-adwords-new.svg
whitelist:
  tables: true
  columns: true

# -------------------------- #
#      Querying Details      #
# -------------------------- #

## AdWords's default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

replication-notes: true
attribution-window: "30 days"

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**To pause any ad-blocking software**. Ad blockers can interfere with pop-ups, which are used in Google authorization and may prevent authorization from successfully completing."
  - item: "**Access to the {{ integration.display_name }} data you want to replicate**. Before beginning, verify that the user creating the integration has access to the reports you want to replicate."
  - item: |
      **To connect your AdWords account to a My Client Center (MCC) account.** This will ensure your account has access to the AdWords API, thereby allowing Stitch to query for and extract data.

      An MCC account is an AdWords account type that enables you to manage several AdWords accounts under a single login. Think of manager accounts as trees: they can branch out to individual accounts or even other manager accounts. [Read more about MCC accounts here](https://support.google.com/adwords/answer/6139186).

      By default, regular advertiser accounts - that is, individual AdWords accounts - don't have access to the AdWords API. To gain access, they must be linked to an MCC account. If you don't have an MCC account, [create one using these instructions](https://support.google.com/adwords/answer/7459399) and then link it to your AdWords account [by following these steps](https://support.google.com/adwords/answer/7459601).

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch & Select {{ integration.display_name }} Profiles"
    anchor: "auth-select-ga-profiles"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/select-adwords-profiles.png" alt="Selecting Google AdWords profiles." max-width="400px" %}
      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google AdWords data. **Note that we will only ever read your data.**
      2. Click **Authorize** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} profile you want to connect to Stitch.
      4. When selecting profiles, keep the following in mind:

         - **You can select up to 400 profiles per Google AdWords integration**. If you need to sync data from more than 400 profiles, you should create additional {{ integration.display_name }} integrations in your Stitch account.
         - **Selecting a subprofile will also select the parent**, or top-level profile. If you de-select the top-level profile, you will be unable to sync any subprofiles.

       5. When finished selecting profiles, click **Continue**.
  - title: "track data"
    content: |
      {% capture column-compatibility %}
      **Column Selection & Google Compatibility Rules**<br>
      Because of Google's compatibility rules, some columns (metrics and segments) can't be tracked together. As you select columns to track, incompatible fields will automatically be greyed out.<br><br>

      You can create additional {{ integration.display_name }} integrations if you need to track incompatible columns. The resulting table names will still be the same (ex: `account_performance_report`) but the data will reside in different schemas in your data warehouse.
      {% endcapture %}

      {% include note.html content=column-compatibility %}

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      There are two types of tables in Stitch's {{ integration.display_name }} integration: Core Object and Report.

      - **Core Object** tables contain foundational data that's useful for analysis. These are the [`accounts`](#accounts), [`ad_groups`](#ad_groups), [`ads`](#ads), and [`campaigns`](#campaigns) tables. These tables are replicated using **Full Table Replication**.

      - **Report** tables are the various {{ integration.display_name }} reports. The replication process for these tables is a bit unlike that of other tables:
        - **Extraction**: Data is extracted using a conversion window. A conversion window is a period of time after a customer clicks an ad that a conversion (ex: a purchase) is recorded in {{ integration.display_name }}. Stitch currently uses a conversion window of **{{ integration.attribution-window }}**.

           This means that data from the past {{ integration.attribution-window }} will be replicated during every replication job.
        - **Loading**: Data is loaded into your data warehouse using Append-Only Replication.

      For **Report** tables, this means that:

      1. **Due to the conversion window, a high Replication Frequency may not be necessary.** Because Stitch will replicate data from the past {{ integration.attribution-window }} during every replication job, recent data will be re-replicated and count towards your row quota.

         To help prevent overages or unnecessary re-replication, consider setting the integration to sync less frequently. For example: every 12 or 24 hours.

      2. **Querying for the latest data in Report tables will require a different strategy than you might usually use**. Stitch will add a column named `{{ system-column.report-date-time }}` to Report tables to help you identify the most recent records in a table. [See the Query for the Latest Data section for more info and a sample query](#query-for-the-latest-data).

      Each part of the replication process for **Report** tables is explained below.

  - title: "Report Tables: Data Extraction & Conversion Windows"
    anchor: "data-extraction-conversion-window"
    content: |
      Every time Stitch runs a replication job for {{ integration.display_name }}, the last {{ integration.attribution-window }}' worth of data will be replicated for all [**Report** tables](#schema) currently being tracked. 

      Stitch replicates data in this way to account for updates made during the conversion window.

      #### Historical & Full Resyncs {#data-extraction-conversion-window--historical}

      For historical and full resyncs of **Report** tables, Stitch will query for and extract data newer than or equal to the date defined in the **Start Date** field in the Integration Settings page.

      The [**Start Date**](#define-historical-sync) defines the minimum date Stitch should query for when extracting historical data.

      ##### Example {#historical-sync-example}

      During the initial set up, the **Start Date** field is set to `07/03/2017`, or `2017-07-03 00:00:00`. In this example, Stitch will query for data that is newer than or equal to `2017-07-03 00:00:00`.

      If you were to write a SQL query using this date for the `ad_performance_report` table, it might look like this:

      ```sql
      SELECT *
      FROM ad_performance_report
      WHERE day >= '2017-07-03 00:00:00'              // day is the Replication Key column
      ORDER BY day
      ```

      #### Ongoing Syncs {#data-extraction-conversion-window--ongoing}

      For ongoing syncs of **Report** tables, Stitch will query for and extract data using the last saved maximum value in the table's Replication Key column and the conversion window of {{ integration.attribution-window }}.

      **Note:** This applies to every sync that takes place after the historical sync.

      ##### Example {#ongoing-sync-example}

      The last maximum saved Replication Key value for the `ad_performance_report` table is `2017-10-01 00:00:00`.

      Subtracting the conversion window of {{ integration.attribution-window }} would equal `2017-09-01 00:00:00`.

      In this example, Stitch will query for and extract data that is newer than or equal to `2017-09-01 00:00:00` and older than or equal to 2017-10-01 00:00:00.

      If this were a SQL query, it might look like this:

      ```sql
      SELECT *
      FROM ad_performance_report
      WHERE day <= '2017-10-01 00:00:00'       // max Replication Key value from previous sync
      AND day >= '2017-09-01 00:00:00'         // max Replication Key value - 30 day conversion window
      ORDER BY day
      ```

  - title: "Report Tables: Data Loading & Append-Only Replication"
    anchor: "data-loading-append-only"
    content: |
     When Stitch loads the extracted data into your data warehouse, it will do so using Append-Only Replication. This is a type of Incremental Replication where existing rows aren't updated, but appended to the end of the table. 

     Additionally, the number of rows loaded into the table during each sync is dependent on the combination of unique values in the dimension columns you track.

     ##### Example {#append-only-example}

     Let's say these columns are tracking in the `ad_performance_report` table:

     - `campaignId` (dimension) - This is the ID associated with a campaign. In this example, there are two campaigns: `929007494` and `929599581`
     - `device` (dimension) - The device type. There are two values for this example: `Computers` and `Tablets with full browsers`
     - `impressions` (metric) - The total number of impressions.

     Every time Stitch replicates and loads data, a row for each unique combination of the dimension columns will be appended to the end of the table:

     | {{ system-column.customer-id }} | {{ system-column.report-date-time }} | day | campaignId | device | impressions |
     |---------------------------------|--------------------------------------|------------|-----|--------|-------------|
     | 1585293495 | 2017-10-01 17:48:26.791 | 2017-09-10 00:00:00 | 929007494 | Computers                  | 61 |
     | 1585293495 | 2017-10-01 17:48:26.791 | 2017-09-10 00:00:00 | 929007494 | Tablets with full browsers | 15 |
     | 1585293495 | 2017-10-01 17:48:26.791 | 2017-09-10 00:00:00 | 929599581 | Computers                  | 37 |
     | 1585293495 | 2017-10-01 17:48:26.791 | 2017-09-10 00:00:00 | 929599581 | Tablets with full browsers | 9  |

  - title: "Report Tables: Query for the Latest Data"
    anchor: "query-for-the-latest-data"
    content: |
      If you want only the most recently replicated data for any {{ integration.display_name }} Report table, you can use the sample query below to account for the Append-Only Replication Stitch uses.

      This query uses two columns - which are automatically included for every Report table - to return the latest data:

      - `day` - The day that the record pertains to.
      - `{{ system-column.report-date-time }}` - The starting time of the Stitch job that extracted the record.

      ```sql
      SELECT *
      FROM (
             SELECT *,
                    RANK() OVER (PARTITION BY day
                                 ORDER BY {{ system-column.report-date-time }} DESC)
             FROM ad_performance_report
             ORDER BY day ASC
            ) AS latest
      WHERE latest.rank = 1
      ```

      In this query:

      1. [A subquery first uses a window function](https://chartio.com/resources/tutorials/using-window-functions/) to create a 'window' of data for each `day`,
      2. The values of the `{{ system-column.report-date-time }}` column are ranked within each window partition, and
      4. Then, in the outer query, only the rows with `{{ system-column.report-date-time }}` values ranked as `1` - which is equal to the maximum timestamp - are returned. 

      **Note**: You may need to adjust the above query to account for differences in SQL syntax and usage depending on what type of data warehouse you're using.


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-adwords

---
{% assign integration = page %}
{% include misc/data-files.html %}