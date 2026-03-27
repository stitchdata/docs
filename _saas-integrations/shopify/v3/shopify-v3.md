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

  - title: "Define the historical replication start date"
    anchor: "define-historical-sync"
    content: |
      {% include integrations/saas/setup/historical-sync.html %}
  
  - title: "Create a replication schedule"
    anchor: "define-rep-frequency"
    content: |
      {% include integrations/shared-setup/replication-frequency.html %}

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
      7. In the **Configuration** tab, click **Admin API access scopes**.
      8. Select the following required scopes:

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

      9. Click **Save**.
      10. In the **API credentials** tab, under **Admin API access token**, click **Reveal token once**.
      11. You'll see your **Client ID** and **Client Secret**. Store these securely—you'll need them in the next step.

      {% include warning.html content="Your Client Secret will only be visible once after initial creation. Store it securely before navigating away." %}

      12. Click **Install app**.

  - title: "Authorize Stitch to access {{ integration.display_name }}"
    anchor: "grant-stitch-authorization"
    content: |
      Next, you'll enter your {{ integration.display_name }} credentials into Stitch. You'll use the credentials from the custom app you created in the previous step.

      **Choose the setup path that matches your situation:**

      - [For individual store owners](#for-individual-store-owners)
      - [For multiple stores in the same organization ({{ integration.display_name }} Plus)](#for-multiple-stores)
      - [For {{ integration.display_name }} Partners](#for-shopify-partners)

      #### For individual store owners {#for-individual-store-owners}

      **When to use this path:** You own a single {{ integration.display_name }} store and are connecting it directly to Stitch.

      1. In Stitch, enter the following information from your custom app:
         - **Shop:** Your store name without the domain. For example, if your store URL is `stitch-data.shopify.com`, enter `stitch-data`.
         - **Client ID:** Paste your Client ID from the custom app's **API credentials** section.
         - **Client Secret:** Paste your Client Secret from the custom app's **API credentials** section.
      2. Click {{ app.buttons.finish-int-setup }}.

      #### For multiple stores in the same organization ({{ integration.display_name }} Plus) {#for-multiple-stores}

      **When to use this path:** You have multiple {{ integration.display_name }} stores within your organization (Shopify Plus plan) and want to use a single app for all of them.

      **Important:** The app is organization-scoped. Stores outside your organization will require a separate app.

      1. Follow the steps in [Create a {{ integration.display_name }} custom app](#create-shopify-custom-app) to create a single app.
      2. In your {{ integration.display_name }} Admin Dashboard, go to **Settings** > **Apps and integrations** > **Develop apps**.
      3. For each store you want to connect:
         - Switch to that store's Admin Dashboard context (if not already there).
         - Note the store's handle (shop name).
      4. In Stitch, create a separate connection for each store, entering:
         - **Shop:** The store's handle (shop name).
         - **Client ID:** Paste your Client ID from the shared custom app.
         - **Client Secret:** Paste your Client Secret from the shared custom app.
      5. Click {{ app.buttons.finish-int-setup }} for each connection.

      #### For {{ integration.display_name }} Partners {#for-shopify-partners}

      **When to use this path:** You're a {{ integration.display_name }} Partner creating apps for your clients' stores, or you're a client of a partner agency.

      1. As a partner, create your custom app via [partners.shopify.com](https://partners.shopify.com){:target="new"} with **Custom distribution** selected.
      2. Generate an installation link for your client (the link expires after 7 days).
      3. The client accesses the installation link and installs the app to their store.
      4. Provide the client with the **Client ID** and **Client Secret** from the app's **API credentials** section.
      5. The client enters the following information in Stitch:
         - **Shop:** Their store handle (shop name).
         - **Client ID:** The Client ID provided by their partner.
         - **Client Secret:** The Client Secret provided by their partner.
      6. Click {{ app.buttons.finish-int-setup }}.

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
