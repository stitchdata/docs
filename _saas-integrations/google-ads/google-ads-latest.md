---
title: Google Ads (v1)
permalink: /integrations/saas/google-ads
redirect_from: 
  - /integrations/saas/google-adwords-v1
  - /integrations/saas/google-adwords
tags: [saas_integrations]
keywords: google adwords, google ads, google adwords data, etl google adwords, google adwords etl, google adwords schema
summary: "Connection instructions, replication info, and schema details for Stitch's Google Ads integration."
layout: singer

key: "google-ads-setup"

microsites:
  - title: "{{ page.display_name }} to BigQuery"
    url: "http://adwords.tobigquery.com/"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "google-ads"
display_name: "Google Ads"
singer: true

tap-name: "Google AdWords"
repo-url: https://github.com/singer-io/tap-adwords

this-version: "1"

api-name: "Google AdWords API (v201809)"
api: |
  [Google AdWords API (v201809)](https://developers.google.com/adwords/api/docs/guides/start){:target='new'}

# -------------------------- #
#     Integration Details    #
# -------------------------- #

api-version: "v201809"

certified: true

historical: "30 days"
frequency: "24 hours"
tier: "Standard"
status-url: "https://www.google.com/appsstatus#hl=en&v=status"

api-type: "platform.adwords"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true
select-all: false
select-all-reason: |
  The API used by this integration ({{ integration.api-name }}) doesn't support selecting all fields due to compatibility rules.

extraction-logs: true
loading-reports: true

append-only-integration: false
append-only-tables: true
append-only-tables-description: "All Report tables"


## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Querying Details      #
# -------------------------- #

## Ads' default attribution window. Stitch queries for
## this number of days during each replication job to
## account for any updates to existing records made during 
## this time.

attribution-window: "30 days"

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

  **Note**: To use the AdWords API, an Ads account must be connected to a [My Client Center (MCC) account](#setup-requirements).


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: "**To pause any ad-blocking software**. Ad blockers can interfere with pop-ups, which are used in Google authorization and may prevent authorization from successfully completing."
  - item: "**Access to the {{ integration.display_name }} data you want to replicate**. Before beginning, verify that the user creating the integration has access to the reports you want to replicate."
  - item: |
      **To connect your Ads account to a My Client Center (MCC) account.** This will ensure your account has access to the AdWords API, thereby allowing Stitch to query for and extract data.

      An MCC account is an Ads account type that enables you to manage several Ads accounts under a single login. Think of manager accounts as trees: they can branch out to individual accounts or even other manager accounts. [Read more about MCC accounts here](https://support.google.com/adwords/answer/6139186).

      By default, regular advertiser accounts - that is, individual Ads accounts - don't have access to the AdWords API. To gain access, they must be linked to an MCC account. If you don't have an MCC account, [create one using these instructions](https://support.google.com/adwords/answer/7459399){:target="new"} and then link it to your Ads account [by following these steps](https://support.google.com/adwords/answer/7459601).

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch & Select {{ integration.display_name }} Profiles"
    anchor: "auth-select-ga-profiles"
    content: |
      {% include layout/inline_image.html type="right" file="integrations/select-adwords-profiles.png" alt="Selecting Google Ads profiles." max-width="400px" %}

      1. Next, you’ll be prompted to log into your Google account and to approve Stitch’s access to your Google Ads data. **Note: We will only ever read your data.**
      2. Click **Authorize** to continue.
      3. After your credentials are validated, you’ll be prompted to select the {{ integration.display_name }} profile(s) you want to connect to Stitch.

         If you don't see the profile(s) you want to connect, verify that you have completed the [setup requirements](#setup-requirements).
      4. When selecting profiles, keep the following in mind:

         - **You can select up to 400 profiles per Google Ads integration**. If you need to replicate data from more than 400 profiles, you should create additional {{ integration.display_name }} integrations in your Stitch account.
         - **Selecting a subprofile will also select the parent**, or top-level profile. If you de-select the top-level profile, you will be unable to select any subprofiles.
         - **If multiple profiles are selected, data for all the selected profiles will map to the same table in your destination.** For example: If two profiles are selected and the `accounts` table is tracked, account data for both profiles will be replicated into the `accounts` table. This is applicable to every table selected in the next step.

       5. When finished selecting profiles, click **Continue**.
  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}
    content: |
      {% capture column-compatibility %}
      Because of Google's compatibility rules, some columns (metrics and segments) can't be tracked together. As you select columns to track, incompatible fields will automatically be greyed out.

      You can create additional {{ integration.display_name }} integrations if you need to track incompatible columns. The resulting table names will still be the same (ex: `account_performance_report`) but the data will reside in different schemas in your data warehouse.
      {% endcapture %}

      {% include note.html first-line="**Column selection and Google compatibility rules**" content=column-compatibility %}

# -------------------------- #
#      Replication Info      #
# -------------------------- #

replication-sections:
  - content: |
      {% include integrations/saas/ads-append-only-replication.html type="table-types" %}

  - title: "Report tables: Data extraction and conversion windows"
    anchor: "data-extraction-conversion-window"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="report-tables" %}
      
  - title: "Report tables: Data loading and Append-Only Replication"
    anchor: "data-loading-append-only"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="data-loading" %}

  - title: "Report tables: Query for the latest data"
    anchor: "query-for-the-latest-data"
    content: |
      {% include integrations/saas/ads-append-only-replication.html type="append-only-query" %}


# -------------------------- #
#        Schema Details      #
# -------------------------- #

schema-sections:
  - title: "Report tables: Values for money fields"
    anchor: "values-for-money-fields"
    content: |
      When conducting analyses on Report tables, you might notice that values in money fields - like a `cost` field, for example - look higher than usual. This is because [Google Ads' API sends Stitch money data in micro currency units](https://developers.google.com/adwords/api/docs/guides/reporting#money_fields_in_reports). Micro amounts always refer to your account's local currency.

      For example: The value of $2.25USD will be recorded as `2250000`. To represent this value as `2.25` in a report, divide by one million: `2250000 / 1000000 = 2.25`.

  - title: "Report tables: Column selection and statistic aggregation"
    anchor: "column-selection-statistic-aggregation"
    content: |
      {% include integrations/saas/ads-columns-and-aggregation.html %}

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/google-adwords
---
{% assign integration = page %}
{% include misc/data-files.html %}