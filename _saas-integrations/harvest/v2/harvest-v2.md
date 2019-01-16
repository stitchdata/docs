---
title: Harvest (v2.0)
permalink: /integrations/saas/harvest
tags: [saas_integrations]
keywords: harvest, harvest integration, schema, etl harvest, harvest etl, harvest schema
summary: "Connection instructions, replication info, and schema details for Stitch's Harvest integration."
layout: singer

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "harvest"
display_name: "Harvest"
singer: true
repo-url: https://github.com/singer-io/tap-harvest

this-version: "2.0"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: http://harveststatus.com/
icon: /images/integrations/icons/harvest.svg

table-selection: false
column-selection: false

extraction-logs: true
loading-reports: true
anchor-scheduling: true

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Verify your Harvest user's access.** Stitch will have the same permissions as the user setting up the integration. This means Stitch will only be able to access the same objects and data as the authorizing user.

      For example: if you're unable to access expenses in Harvest, Stitch will be unable to replicate expense data.

requirements-info: |
  Before diving into the setup process, verify that the user setting up the integration has access to all the objects - such as expenses - that you want to replicate.

  [Read more about Harvest permissions in their documentation](http://help.getharvest.com/harvest/team/overview/new-permissions/).

setup-steps:
  - title: "add integration"
    content: |
      4. Enter your Harvest account name in the **Account Name** field. For example: if your Harvest account URL is `stitch.harvestapp.com`, you'd enter `stitch` in this field.
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to Access Harvest"
    anchor: "grant-stitch-authorization"
    content: |
      Lastly, you'll be directed to Harvest's website to complete the setup.

      1. Enter your Harvest credentials and click **Create Integration**.
      2. A screen asking for authorization to Harvest will display. **Note that Stitch will only ever read your data.**
      3. Click **Connect.**
      4. After the authorization process successfully completes, you'll be redirected back to Stitch.
      5. Click {{ app.buttons.finish-int-setup }}.

# -------------------------- #
#        Table Schemas       #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/harvest

---
{% assign integration = page %}
{% include misc/data-files.html %}
