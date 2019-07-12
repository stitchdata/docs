---
title: Referral SaaSquatch (v1.0)
permalink: /integrations/saas/referral-saasquatch
keywords: referral saasquatch, integration, schema, etl referral saasquatch, referral saasquatch etl, referral saasquatch schema
summary: "Connection instructions and schema details for Stitch's Referral SaaSquatch integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "referral-saasquatch"
display_name: "Referral SaaSquatch"

singer: true
repo-url: https://github.com/singer-io/tap-referral-saasquatch

# this-version: "1.0"

api: |
  [{{ integration.display_name }} REST API](https://docs.referralsaasquatch.com/api/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://twitter.com/getSaasquatch

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

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

  - title: "add integration"
    content: |
      4. In the **Tenant Alias** field, paste your Referral SaaSquatch Tenant Alias.
      5. In the **API Key** field, paste your Referral SaaSquatch API Key.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/referral-saasquatch
---
{% assign integration = page %}
{% include misc/data-files.html %}