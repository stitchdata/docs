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

      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google AdWords data. **Note: We will only ever read your data.**
      2. Click **Authorize** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} profile(s) you want to connect to Stitch.

         If you don't see the profile(s) you want to connect, verify that you have completed the [setup requirements](#setup-requirements).
      4. When selecting profiles, keep the following in mind:

         - **You can select up to 400 profiles per Google AdWords integration**. If you need to replicate data from more than 400 profiles, you should create additional {{ integration.display_name }} integrations in your Stitch account.
         - **Selecting a subprofile will also select the parent**, or top-level profile. If you de-select the top-level profile, you will be unable to select any subprofiles.
         - **If multiple profiles are selected, data for all the selected profiles will map to the same table in your destination.** For example: If two profiles are selected and the `accounts` table is tracked, account data for both profiles will be replicated into the `accounts` table. This is applicable to every table selected in the next step.

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
# Each table has a its own .md file in /_integration-schemas/google-adwords

---
{% assign integration = page %}
{% include misc/data-files.html %}