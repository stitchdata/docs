---
title: Shopify (v3)
permalink: /integrations/saas/shopify/v3
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

this-version: "3"

api: |
  [{{ integration.display_name }} GraphQL Admin API (v2025-01)](https://shopify.dev/docs/api/admin-graphql/2025-01){:target="new"}

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

  #### {{ integration.display_name }} is now powered by GraphQL
  We've enhanced the Stitch's {{ integration.display_name }} integration by replacing REST Admin API by the {{ integration.display_name }} GraphQL API.
  This provides:
  - More structured and complete data 
  - Better performance and scalability
  - Access to new fields that are unavailable in REST

  #### What has changed?
  The data structure has been reorganized for consistency and clarity. Some fields may look different or appear in new locations. Also, a few fields are deprecated from the {{ integration.display_name }} side.

  If you need help, you can compare the structures. Refer to {{ integration.display_name }} documentation:
  - [REST Admin API](https://shopify.dev/docs/api/admin-rest){:target="new"}
  - [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql){:target="new"}

  Check out our updated {{ integration.display_name }} docs for stream-level details and examples.

# -------------------------- #
#      Setup Instructions    #
# -------------------------- #

requirements-list:
  - item: |
      **Admin access in {{ integration.display_name }}**. This is required to create and manage custom apps.

      **Note: If you're on a {{ integration.display_name }} Plus plan**, the permissions required may differ. Store owners can grant users permissions to manage apps and custom integrations. In general, **app management** permissions should be sufficient.
      
      Refer to the [{{ integration.display_name }} Staff permissions documentation](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions#store-owner-permissions){:target="new"} for more information.
  - item: |
      **Access to {{ integration.display_name }} Developer Dashboard** with app management permissions. You'll use this to create a custom app and generate credentials.
  - item: |
      **Note:** Access tokens refresh automatically every 24 hours and are managed server-side by Stitch. You don't need to manually refresh your credentials.
  
setup-steps:
  - title: "Add {{ integration.display_name }} as a Stitch data source"
    anchor: "add-stitch-data-source"
    content: |
      {% include integrations/shared-setup/connection-setup.html %}

  - title: "Create a {{ integration.display_name }} custom app"
    anchor: "create-shopify-custom-app"
    content: |
      A custom app allows you to securely generate credentials that Stitch will use to authenticate and replicate data from your {{ integration.display_name }} store.
      
      **To create a custom app:**

      1. Log into your [{{ integration.display_name }} Admin Dashboard](https://admin.shopify.com){:target="new"}.
      2. In the sidebar, go to **Settings** > **Apps and integrations**.
      3. Click **Develop apps** (or **App and sales channel settings** if using Shopify Plus).
      4. Click **Create an app**.
      5. Enter a name for your app (for example: `Stitch`).
      6. Click **Create app**.
      
      The app is created. Do not install it. You need to request some {{ integration.display_name }} access first. See the next step.

  - title: "Request access from Shopify"
    anchor: "request-access-from-shopify"
    content: |
      To access certain {{ integration.display_name }} API scopes, you must request access from {{ integration.display_name }} before installing your custom app. The following scopes require explicit approval:

      ##### `read_all_orders` scope

      By default, you only have access to the last 60 days of orders. To access all historical orders, you must request the `read_all_orders` scope in the {{ integration.display_name }} Partners dashboard.

      **To request the `read_all_orders` scope:**

      1. Go to the [{{ integration.display_name }} Partners dashboard](https://partners.shopify.com/){:target="new"}.
      2. Navigate to **Apps** and select your app.
      3. Open the **API access requests** section.
      4. In the **Read all orders** section, click **Request access**.
      5. In the access request justification, specify that the app needs full read-only access to historical orders for long-term analytics, reconciliation, and reporting.
      6. Submit the request and wait for {{ integration.display_name }} approval.

      After {{ integration.display_name }} approves the request, you can add the `read_all_orders` scope to your app scope list. If the app was already installed before this permission was granted, you must uninstall and reinstall the app for the new scope to take effect.

      ##### `read_users` scope

      To use the `read_users` scope, one of the following conditions must be true:

      - The app must be a finance embedded app.
      - The app must be installed on a {{ integration.display_name }} Plus or Advanced store.

      Contact {{ integration.display_name }} Support to enable this scope if required.

  - title: "Install the {{ integration.display_name }} custom app"
    anchor: "install-shopify-custom-app"
    content: |
      Follow this step only if you've created the app and requested access from {{ integration.display_name }}. See the previous steps.

      1. Go to the [{{ integration.display_name }} Partners dashboard](https://partners.shopify.com/){:target="new"}.
      2. In the **Configuration** tab, click **Admin API access scopes**.
      3. Select or copy-paste the following required scopes:
          `read_orders`,`read_all_orders`,`read_customers`,`read_products`,`read_checkouts`,`read_inventory`,`read_locations`,
          `read_assigned_fulfillment_orders`,`read_merchant_managed_fulfillment_orders`,`read_third_party_fulfillment_orders`.

         | Scope | Purpose |
         |-------|---------|
         | `read_orders` | Replicate order data |
         | `read_all_orders` | Replicate historical order data |
         | `read_customers` | Replicate customer information |
         | `read_products` | Replicate product catalog |
         | `read_checkouts` | Replicate checkout data |
         | `read_inventory` | Replicate inventory levels |
         | `read_locations` | Replicate store locations |
         | `read_assigned_fulfillment_orders` | Replicate assigned fulfillment orders |
         | `read_merchant_managed_fulfillment_orders` | Replicate merchant-managed fulfillment orders |
         | `read_third_party_fulfillment_orders` | Replicate third-party fulfillment orders |

      4. Click **Save**.
      5. In the **API credentials** tab, under **Admin API access token**, click **Reveal token once**. You'll see your **Client ID** and **Client Secret**.
      6. Store these credentials securely. You need them in the next step. Your Client Secret will only be visible once after initial creation. Store it securely before navigating away.
      7. Click **Install app**.

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

  - title: "Set objects to replicate"
    anchor: "setting-data-to-replicate"
    content: |
      {% include integrations/shared-setup/data-selection/object-selection.html %}

# -------------------------- #
#     Replication Details    #
# -------------------------- #

replication-sections:  
  - title: "Replicating order refunds"
    anchor: "order-refunds"
    content: |
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
