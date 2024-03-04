---
title: Shopify (v1)
permalink: /integrations/saas/shopify
keywords: shopify, integration, schema, etl shopify, shopify etl, shopify schema
summary: "Connection instructions, replication info, and schema details for Stitch's Shopify integration."
layout: singer

key: "shopify-setup"

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "shopify"
display_name: "Shopify"

singer: true
tap-name: "Shopify"
repo-url: https://github.com/singer-io/tap-shopify

this-version: "1"

api: |
  [{{ integration.display_name }} REST Admin API (v2024-01)](https://shopify.dev/docs/admin-api/rest/reference){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Standard"
status-url: "https://status.shopify.com/"

api-type: "platform.shopify"

anchor-scheduling: true
cron-scheduling: true

table-selection: true
column-selection: true

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

requirements-list:
  - item: |
      **Admin access in {{ integration.display_name }}**. This is required to allow Stitch to replicate data.

      **Note: If you're on a {{ integration.display_name }} Plus plan**, the permissions required may differ. Store owners can grant users permissions to export orders, draft orders, products, inventory, and customer data. In general, **view-level** permissions should be sufficient.
      
      Refer to the [{{ integration.display_name }} Staff permissions documentation](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions#store-owner-permissions){:target="new"} for more information.
  
setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}
      4. In the **Shopify Shop** field, enter the name of the shop you want to connect to Stitch. For example: If the shop URL was `stitch-data.shopify.com`, you'd enter `stitch-data` into this field. 

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      1. Next, you'll be prompted to sign into your {{ integration.display_name }} account. Enter your {{ integration.display_name }} credentials.
      2. Click **Log in**.
      3. After the authorization process is successfully completed, you'll be directed back to Stitch.
      4. Click {{ app.buttons.finish-int-setup }}.

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:  
  - title: "Replicating order refunds"
  - anchor: "order-refunds"
  - content: |
      To extract order refund data, Stitch queries every order in your account. If you have the `order_refunds` table selected for replication, the process can potentially be very slow depending on how many orders and refunds exist in your {{ integration.display_name }} account. As tables are extracted one at a time, this could cause extraction to not proceed for days at a time. To ensure timely replication of your other selected tables, consider creating a separate integration for only the `order_refunds` table.

      **Note**: Creating a separate integration for your `order_refunds` table may negatively affect your {{ integration.display_name }} API quota.
      

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

# Looking for the table schemas & info?
# Each table has a its own .md file in /_integration-schemas/shopify/v1
---
{% assign integration = page %}
{% include misc/data-files.html %}
