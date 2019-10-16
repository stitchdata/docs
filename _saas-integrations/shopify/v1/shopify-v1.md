---
title: Shopify (v1)
permalink: /integrations/saas/shopify
keywords: shopify, integration, schema, etl shopify, shopify etl, shopify schema
summary: "Connection instructions, replication info, and schema details for Stitch's Shopify integration."
layout: singer

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "shopify"
display_name: "Shopify"

singer: true
tap-name: "Shopify"
repo-url: https://github.com/singer-io/tap-shopify

this-version: "1.0"

api: |
  [{{ integration.display_name }} REST Admin API](https://help.shopify.com/en/api/reference){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
status-url: "https://status.shopify.com/"

table-selection: true
column-selection: true

anchor-scheduling: true
cron-scheduling: false

extraction-logs: true
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: true
  data-volume: false
  lots-of-full-table: false


# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.


# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

setup-steps:
  - title: "add integration"
    content: |
      4. In the **Shopify Shop** field, enter the name of the shop you want to connect to Stitch. For example: If the shop URL was `stitch-data.shopify.com`, you'd enter `stitch-data` into this field. 
  - title: "historical sync"
  - title: "replication frequency"
  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account. Enter your {{ integration.display_name }} credentials.
      2. Click **Log in**.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.
  - title: "track data"


# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/shopify/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}