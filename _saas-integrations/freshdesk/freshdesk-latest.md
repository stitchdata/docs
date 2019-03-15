---
title: Freshdesk (v1.0)
permalink: /integrations/saas/freshdesk
keywords: freshdesk, integration, schema, etl freshdesk, freshdesk etl, freshdesk schema
summary: "Connection instructions and schema details for Stitch's Freshdesk integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "freshdesk"
display_name: "Freshdesk"

singer: true
repo-url: https://github.com/singer-io/tap-freshdesk

# this-version: "1.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false # Community-supported integration

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://updates.freshdesk.com/

table-selection: false
column-selection: false

anchor-scheduling: true
extraction-logs: true
loading-reports: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Administrator permissions in Freshdesk.** As Stitch will only be able to replicate data that the authorizing user access to, we recommend that someone with these permissions complete the setup. For example: if the authorizing user only has access to a handful of tickets, Stitch will only be able to access and replicate the data for those tickets.

      Having a Freshdesk administrator create the integration will ensure that Stitch is able to replicate all the data in your Freshdesk account.

setup-steps:
  - title: "Retrieve your Freshdesk API Key"
    anchor: "retrieve-api-credentials"
    content: |
      1. Sign into your Freshdesk account.
      2. Click the **user menu (your icon) > Profile Settings**.
      3. Your API Key will display under the **Change Password** section of your profile page.

      Leave this page open for now - you'll need it to wrap things up in Stitch.

  - title: "add integration"
  - title: "historical sync"
  - title: "replication frequency"

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/freshdesk

---
{% assign integration = page %}
{% include misc/data-files.html %}
