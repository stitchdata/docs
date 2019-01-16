---
title: Referral SaaSquatch (v1.0)
permalink: /integrations/saas/referral-saasquatch
tags: [saas_integrations]
keywords: referral saasquatch, integration, schema, etl referral saasquatch, referral saasquatch etl, referral saasquatch schema
summary: "Connection instructions and schema details for Stitch's Referral SaaSquatch integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "referral-saasquatch"
display_name: "Referral SaaSquatch"
singer: true
author: "Stitch"
author-url: https://www.stitchdata.com
repo-url: https://github.com/singer-io/tap-referral-saasquatch

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://twitter.com/getSaasquatch
icon: /images/integrations/icons/referral-saasquatch.svg

table-selection: false
column-selection: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve Your Referral SaaSquatch API Credentials"
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