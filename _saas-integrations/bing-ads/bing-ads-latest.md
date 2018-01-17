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

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
auth: "oauth"
status-url: https://status.bingads.com/
icon: /images/integrations/icons/bing-ads.svg
whitelist:
  tables: true
  columns: true


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

requirements-info:

setup-steps:
  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch & Select {{ integration.display_name }} Profiles"
    anchor: "auth-select-profiles"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/bing-ads-select-accounts.png" alt="Selecting Bing Ads accounts." max-width="400px" %}

      1. Next, you’ll be prompted to log into your Bing account and to approve Stitch’s access to your Bing Ads data. **Note: We will only ever read your data.**
      2. Click **Authorize** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} profile(s) you want to connect to Stitch.

         If you don't see the profile(s) you want to connect, verify that you have completed the [setup requirements](#setup-requirements).
      4. When selecting profiles, keep the following in mind:

         - **Selecting a subprofile will also select the parent**, or top-level profile. If you de-select the top-level profile, you will be unable to select any subprofiles.
         - **If multiple profiles are selected, data for all the selected profiles will map to the same table in your destination.** For example: If two profiles are selected and the `accounts` table is tracked, account data for both profiles will be replicated into the `accounts` table. This is applicable to every table selected in the next step.

       5. When finished selecting profiles, click **Check and Save**.
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