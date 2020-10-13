---
title: Referral SaaSquatch (v1)
permalink: /integrations/saas/referral-saasquatch
keywords: referral saasquatch, integration, schema, etl referral saasquatch, referral saasquatch etl, referral saasquatch schema
summary: "Connection instructions and schema details for Stitch's Referral SaaSquatch integration."
layout: singer

key: "referral-saasquatch-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "referral-saasquatch"
display_name: "Referral SaaSquatch"

singer: true
repo-url: https://github.com/singer-io/tap-referral-saasquatch

this-version: "1"

api: |
  [{{ integration.display_name }} REST API](https://docs.referralsaasquatch.com/api/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: https://twitter.com/getSaasquatch

api-type: "platform.referral-saasquatch"

anchor-scheduling: true
cron-scheduling: true

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

extraction-logs: true
loading-reports: true

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API credentials"
    anchor: "retrieve-api-credentials"
    content: |
      1. Sign into your Referral SaaSquatch account.
      2. In the **Setup** section of the left nav tab, click the **Install** option.
      3. In this page, locate the **Tenant Alias** and **API Key** fields.
      4. In the **API Key** field, click the **Click to Reveal** link to reveal your API Key.

      Leave this page open for now - you'll need it to complete the setup in Stitch.

  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Tenant Alias** field, paste your Referral SaaSquatch Tenant Alias.
      5. In the **API Key** field, paste your Referral SaaSquatch API Key.
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}


# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/referral-saasquatch
---
{% assign integration = page %}
{% include misc/data-files.html %}