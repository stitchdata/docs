---
title: Shippo (v1.0)
permalink: /integrations/saas/shippo
keywords: shippo, integration, schema, etl shippo, shippo etl, shippo schema
summary: "Connection instructions and schema details for Stitch's Shippo integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "shippo"
display_name: "Shippo"

singer: true
repo-url: https://github.com/singer-io/tap-shippo

# this-version: "1.0"
# api-version: 2016-10-25

# -------------------------- #
#     Integration Details    #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: https://status.goshippo.com/

table-selection: false
column-selection: false

anchor-scheduling: false
extraction-logs: false
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "Retrieve your {{ integration.display_name }} API token"
    anchor: "retrieve-api-creds"
    content: |
      1. Sign into your {{ integration.display_name }} account.
      2. In the left nav tab, click **API**.
      3. Locate the **API LIve Token** field in the **Tokens** section:

         ![Shippo API token.]({{ site.baseurl }}/images/integrations/shippo-api-credentials.png)

         Leave this page open for now - you'll need it to complete the setup.
  - title: "add integration"
    content: |
      4. In the **{{ integration.display_name }} Token** field, paste your {{ integration.display_name }} API Live token.
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/shippo
---
{% assign integration = page %}
{% include misc/data-files.html %}