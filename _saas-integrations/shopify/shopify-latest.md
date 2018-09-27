---
title: Shopify
permalink: /integrations/saas/shopify
tags: [saas_integrations]
keywords: shopify, integration, schema, etl shopify, shopify etl, shopify schema
summary: "Connection instructions, replication info, and schema details for Stitch's Shopify integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "shopify"
display_name: "Shopify"
singer: false
author: "Stitch"
author-url: "https://www.stitchdata.com"
status-url: "https://status.shopify.com/"

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Free"
icon: /images/integrations/icons/shopify.svg

table-selection: false
column-selection: false

anchor-scheduling: false
extraction-logs: false
loading-reports: false

# -------------------------- #
#      Incompatiblities      #
# -------------------------- #

## incompatible:
##  bigquery: "sometimes"
##  reason: "Shopify sometimes sends records that contain multiple data types. BigQuery only allows `FLOAT` and `DOUBLE` data types in the same column; otherwise, the field will be rejected."

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Checkouts
  - name: "checkouts"
    doc-link: https://help.shopify.com/api/reference/abandoned_checkouts
    description: "info about abandoned checkouts. Abandoned checkouts are defined as checkouts where the customer has entered their billing and shipping information, but not completed the ordering process."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Checkout ID (<code>id</code>)
      - name: abandoned_checkout_url
      - name: billing_address__address1
      - name: billing_address__address2
      - name: billing_address__city
      - name: billing_address__company
      - name: billing_address__country
      - name: billing_address__firstname
      - name: billing_address__id
      - name: billing_address__lastname
      - name: billing_address__phone
      - name: billing_address__province
      - name: billing_address__zip
      - name: billing_address__name
      - name: billing_address__province_code
      - name: billing_address__country_code
      - name: billing_address__default
      - name: buyer_accepts_marketing
      - name: cancel_reason
      - name: cart_token
      - name: closed_at
      - name: completed_at
      - name: created_at
      - name: currency
      - name: customer__accepts_marketing
      - name: customer__created_at
      - name: customer__email
      - name: customer__first_name
      - name: customer__id
      - name: customer__last_name
      - name: customer__note
      - name: customer__orders_count
      - name: customer__state
      - name: customer__total_spent
      - name: customer__updated_at
      - name: customer__tags
      - name: discount_codes<code>*</code>
      - name: email
      - name: gateway
      - name: landing_site
      - name: line_items__fulfillment_service
      - name: line_items__grams
      - name: line_items__price
      - name: line_items__product_id
      - name: line_items__quantity
      - name: line_items__requires_shipping
      - name: line_items__sku
      - name: line_items__title
      - name: line_items__variant_id
      - name: line_items__variant_title
      - name: line_items__vendor
      - name: note
      - name: referring_site
      - name: shipping_address__address1
      - name: shipping_address__address2
      - name: shipping_address__city
      - name: shipping_address__company
      - name: shipping_address__country
      - name: shipping_address__firstname
      - name: shipping_address__latitude
      - name: shipping_address__longitude
      - name: shipping_address__lastname
      - name: shipping_address__phone
      - name: shipping_address__province
      - name: shipping_address__zip
      - name: shipping_address__name
      - name: shipping_address__province_code
      - name: shipping_address__country_code
      - name: shipping_lines<code>*</code>
      - name: source_name
      - name: subtotal_price
      - name: tax_lines<code>*</code>
      - name: taxes_included
      - name: token
      - name: total_discounts
      - name: total_line_items_price
      - name: total_price
      - name: total_tax
      - name: total_weight
      - name: updated_at

## Collects
  - name: "collects"
    doc-link: https://help.shopify.com/api/reference/collect
    description: "info about collects, which is the link between products and custom collections."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Collect ID (<code>id</code>)
      - name: collection_id
      - name: created_at
      - name: featured
      - name: position
      - name: product_id
      - name: sort_value
      - name: updated_at


## Custom Collections
  - name: "custom_collections"
    doc-link: https://help.shopify.com/api/reference/customcollection
    description: "info about your custom collections."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Custom Collection ID (<code>id</code>)
      - name: body_html
      - name: handle
      - name: image
      - name: published
      - name: published_at
      - name: published_scope
      - name: sort_order
      - name: template_suffix
      - name: title
      - name: updated_at


## Customers
  - name: "customers"
    doc-link: https://help.shopify.com/api/reference/customer
    description: "info about your shop's customers."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Customer ID (<code>id</code>)
      - name: accepts_marketing
      - name: addresses<code>*</code>
      - name: created_at
      - name: default_address<code>*</code>
      - name: email
      - name: first_name
      - name: multipass_identifier
      - name: last_name
      - name: last_order_id
      - name: last_order_name
      - name: note
      - name: orders_count
      - name: state
      - name: tags
      - name: tax_exempt
      - name: total_spent
      - name: updated_at
      - name: verified_email


## Metafields
  - name: "metafields"
    doc-link: https://help.shopify.com/api/reference/metafield
    description: "metadata for shop and order resources."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Metafield ID (<code>id</code>)
      - name: created_at
      - name: description
      - name: key
      - name: namespace
      - name: owner_id
      - name: owner_resource
      - name: value
      - name: value_type
      - name: updated_at


## Order Refunds
  - name: "order_refunds"
    doc-link: https://help.shopify.com/api/reference/refund/
    description: "info about refunds applied to transactions."
    notes: 
    replication-method: "Full Table"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Order Refund ID (<code>id</code>)
      - name: created_at
      - name: note
      - name: restock
      - name: refund_line_items<code>*</code>
      - name: transactions<code>*</code>
      - name: user_id


## Orders
  - name: "orders"
    doc-link: https://help.shopify.com/api/reference/order
    description: "information about your shop's completed orders."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Order ID (<code>id</code>)
      - name: billing_address<code>*</code>
      - name: browser_ip
      - name: buyer_accepts_marketing
      - name: cancel_reason
      - name: cancelled_at
      - name: cart_token
      - name: client_details__accept_language
      - name: client_details__browser_height
      - name: client_details__browser_ip
      - name: client_details__browser_width
      - name: client_details__session_hash
      - name: client_details__user_agent
      - name: closed_at
      - name: created_at
      - name: currency
      - name: customer__accepts_marketing
      - name: customer__created_at
      - name: customer__email
      - name: customer__first_name
      - name: customer__id
      - name: customer__last_name
      - name: customer__note
      - name: customer__orders_count
      - name: customer__state
      - name: customer__total_spent
      - name: customer__updated_at
      - name: customer__tags
      - name: discount_codes<code>*</code>
      - name: email
      - name: financial_status
      - name: fulfillments<code>*</code>
      - name: fulfillment_status
      - name: tags<code>*</code>
      - name: gateway
      - name: landing_site
      - name: line_items<code>*</code>
      - name: location_id
      - name: name
      - name: note
      - name: note_attributes<code>*</code>
      - name: number
      - name: order_number
      - name: payment_gateway_names
      - name: processed_at
      - name: processing_method
      - name: referring_site
      - name: refunds
      - name: shipping_address<code>*</code>
      - name: shipping_lines<code>*</code>
      - name: source_name
      - name: subtotal_price
      - name: tax_lines<code>*</code>
      - name: taxes_included
      - name: token
      - name: total_discounts
      - name: total_line_items_price
      - name: total_price
      - name: total_tax
      - name: total_weight
      - name: updated_at
      - name: user_id
      - name: order_status_url


## Products
  - name: "products"
    doc-link: https://help.shopify.com/api/reference/product
    description: "info about the products for sale in your shop."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Product ID (<code>id</code>)
      - name: body_html
      - name: created_at
      - name: handle
      - name: images<code>*</code>
      - name: options<code>*</code>
      - name: product_type
      - name: published_at
      - name: published_scope
      - name: tags<code>*</code>
      - name: template_suffix
      - name: title
      - name: metafields_global_title_tag
      - name: metafields_global_description_tag
      - name: updated_at
      - name: variants<code>*</code>
      - name: vendor


## Transactions
  - name: "transactions"
    doc-link: https://help.shopify.com/api/reference/transaction
    description: "info about transactions, which are created for every order that results in money exchange. This includes authorizations, sales, captures, voids, and refunds."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Transaction ID (<code>id</code>)
      - name: amount
      - name: authorization
      - name: created_at
      - name: device_id
      - name: gateway
      - name: source_name
      - name: payment_details
      - name: kind
      - name: order_id
      - name: receipt
      - name: error_code
      - name: status
      - name: test
      - name: user_id
      - name: currency
---
{% assign integration = page %}
{% include misc/data-files.html %}



{% contentfor setup %}
Connecting your Shopify data to Stitch is a four-step process:

1. [Add Shopify as a Stitch data source](#add-stitch-data-source)
2. [Define the Historical Sync](#define-historical-sync)
3. [Define the Replication Frequency](#define-rep-frequency)
4. [Authorizing Stitch to access Shopify](#authorize-stitch)

{% include integrations/shared-setup/connection-setup.html %}
4. In the **Shop Name** field, enter the name of your shop. For example, if your store was `stitch.shopify.com`, `stitch`would be entered in this field.

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorizing Stitch to Access Shopify {#authorize-stitch}

Lastly, you'll be directed to Shopify's website to complete the setup.

1. Enter your Shopify credentials and click **Login**.
2. A screen asking for authorization to Shopify will display. **Note that Stitch will only ever read your data.**
3. Click **Install App.**
4. After the authorization process successfully completes, you'll be redirected back to Stitch.
5. Click {{ app.buttons.finish-int-setup }}.

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}
