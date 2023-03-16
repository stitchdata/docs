---
title: Harvest (v1)
permalink: /integrations/saas/harvest/v1
keywords: harvest, harvest integration, schema, etl harvest, harvest etl, harvest schema
summary: "Connection instructions, replication info, and schema details for Stitch's Harvest integration."
layout: singer
input: false

key: "harvest-setup"

# -------------------------- #
#         Tap Details        #
# -------------------------- #

name: "harvest"
display_name: "Harvest"
singer: true
repo-url: https://github.com/singer-io/tap-harvest

this-version: "1"

api: |
  [{{ integration.display_name }} REST API V1](https://help.getharvest.com/api-v1/){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: false

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: http://harveststatus.com/

table-selection: false
column-selection: false
select-all: false
select-all-reason: |
  As this integration doesn't support table or column selection, all available tables and columns are automatically replicated.

anchor-scheduling: true
cron-scheduling: false

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

requirements-list:
  - item: |
      **Verify your Harvest user's access.** Stitch will have the same permissions as the user setting up the integration. This means Stitch will only be able to access the same objects and data as the authorizing user.

      For example: if you're unable to access expenses in Harvest, Stitch will be unable to replicate expense data.

requirements-info: |
  Before diving into the setup process, verify that the user setting up the integration has access to all the objects - such as expenses - that you want to replicate.

  [Read more about Harvest permissions in their documentation](http://help.getharvest.com/harvest/team/overview/new-permissions/).

setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. Enter your Harvest account name in the **Account Name** field. For example: if your Harvest account URL is `stitch.harvestapp.com`, you'd enter `stitch` in this field.
  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

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
# Each table has a its own .md file in /_integration-schemas/harvest/<version>

---
{% assign integration = page %}
{% include misc/data-files.html %}
