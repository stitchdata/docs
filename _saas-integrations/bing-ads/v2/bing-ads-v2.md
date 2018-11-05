---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Bing Ads
permalink: /integrations/saas/bing-ads
tags: [saas_integrations]
keywords: bing ads, integration, schema, etl bing ads, bing ads etl, bing ads schema
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "bing-ads"
display_name: "Bing Ads"
singer: true 
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-bing-ads

this-version: "2.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "24 hours"
tier: "Free"
auth: "oauth"
status-url: https://status.bingads.com/
icon: /images/integrations/icons/bing-ads.svg

table-selection: true
column-selection: true

anchor-scheduling: true
extraction-logs: true
loading-reports: true


# -------------------------- #
#        API Details         #
# -------------------------- #

enforces-api-limits: true

attribution-window: "30 days"

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **To pause all ad-blocking software currently in use.** Because Bing Ads authentication uses pop ups, you may encounter issues if ad blockers aren't disabled during the setup.
  - item: |
      **To have Viewer permissions to the profiles you want to connect.** These read-only permissions will ensure Stitch can read data from the profiles you select for replication. [Read more about Bing Ads user permissions here](https://help.bingads.microsoft.com/#apex/3/en/52037/3/en-US/#ext:none).

requirements-info:

setup-steps:
  - title: "add integration"
  - title: "historical sync"
    content: |
      {% capture retention-window-notice %}
      {{ integration.display_name }} retains reporting data for specified periods of time, which can impact the amount of historical data Stitch can replicate. Refer to the [Report retention windows and historical data](#retention-window-historical-data) section below for more info.
      {% endcapture %}

      {% include note.html first-line="**Note: Retention windows and historical data**" content=retention-window-notice %}
  - title: "replication frequency"
  - title: "Authorize Stitch and select {{ integration.display_name }} accounts"
    anchor: "auth-select-profiles"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/bing-ads-select-accounts.png" alt="Selecting Bing Ads accounts." max-width="400px" %}

      1. Next, you’ll be prompted to log into your Bing account and to approve Stitch’s access to your {{ integration.display_name }} data.
      2. Click **Authorize** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} account(s) you want to connect to Stitch.

         If you don't see the account(s) you want to connect, verify that you have completed the [setup requirements](#setup-requirements).
      4. When selecting accounts, keep the following in mind:

         - **Only one top-level manager account can be selected.** If you need to connect multiple top-level accounts, we recommend creating additional {{ integration.display_name }} integrations.
         - **Selecting a subaccount will also select the parent**, or top-level account. If you de-select the parent account, you will be unable to select any subaccounts.
         - **If multiple subaccounts are selected, data for all the selected subaccounts will map to the same table in your destination.** For example: If two subaccounts are selected and the `accounts` table is tracked, account data for both accounts will be replicated into the `accounts` table. This is applicable to every table selected in the next step.

       5. When finished selecting accounts, click **Check and Save**.
  - title: "track data"

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - title: "Report retention windows and historical data"
    anchor: "retention-window-historical-data"
    content: |
      {{ integration.display_name }} retains reporting data for specified periods of time. Depending on the type of report, the retention period can vary. For the majority of reports, however, Bing Ads will retain data for **36 months** from the current date.

      This retention window can impact the historical data Stitch can replicate from {{ integration.display_name }}. If you select a **Start Date** further in the past than the retention window allows, an error similar to the following will surface in the integration's [Extraction Logs]({{ link.replication.extraction-logs | prepend: site.baseurl }}) during the extraction phase:

      ```
      tap - Message = "The specified report time contains an invalid custom date range end. Please submit a report request with valid start and end dates for the custom date range."
      ```

      To resolve the error, select a **Start Date** within the retention window, which is typically **36 months**. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/guides/report-data-retention-time-periods?view=bingads-12){:target="_blank"} for more info and to check the retention periods for your reports.

  - title: "Table types and replication"
    anchor: "table-types-and-replication"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="table-types" %}
    subsections:
      - title: "Report Tables: Data extraction and Conversion Windows"
        anchor: "data-extraction-conversion-window"
        content: |
          {% include integrations/saas/ads-append-only-replication.html type="report-tables" %}

      - title: "Report Tables: Data loading and Append-Only Replication"
        anchor: "data-loading-append-only"
        content: |
          {% include integrations/saas/ads-append-only-replication.html type="data-loading" %}

      - title: "Report Tables: Query for the latest data"
        anchor: "query-for-the-latest-data"
        content: |
          {% include integrations/saas/ads-append-only-replication.html type="append-only-query" %}


# -------------------------- #
#        Schema Details      #
# -------------------------- #

schema-sections:
  - title: "Report Tables: Column selection and statistic aggregation"
    anchor: "column-selection-statistic-aggregation"
    content: |
      {% include integrations/saas/ads-columns-and-aggregation.html %}

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/bing-ads
---
{% assign integration = page %}
{% include misc/data-files.html %}