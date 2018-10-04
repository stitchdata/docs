---
# -------------------------- #
#      Page & Formatting     #
# -------------------------- #

title: Bing Ads
permalink: /integrations/saas/bing-ads/v1
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

this-version: "1.0"

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
  - title: "replication frequency"
  - title: "Authorize Stitch & Select {{ integration.display_name }} Accounts"
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
  - content: |
      {% include integrations/saas/ads-append-only-replication.html type="table-types" %}

  - title: "Report Tables: Data Extraction & Conversion Windows"
    anchor: "data-extraction-conversion-window"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="report-tables" %}

  - title: "Report Tables: Data Loading & Append-Only Replication"
    anchor: "data-loading-append-only"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="data-loading" %}

  - title: "Report Tables: Query for the Latest Data"
    anchor: "query-for-the-latest-data"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="append-only-query" %}


# -------------------------- #
#        Schema Details      #
# -------------------------- #

schema-sections:
  - title: "Report Tables: Column Selection and Statistic Aggregation"
    anchor: "column-selection-statistic-aggregation"
    content: |
      {% include integrations/saas/ads-columns-and-aggregation.html %}

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/bing-ads
---
{% assign integration = page %}
{% include misc/data-files.html %}