---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "recharge"

version: "2"

foreign-keys:
  - id: "address-id"
    table: "addresses"
    attribute: "address_id"
    all-foreign-keys:
      - table: "addresses"
        join-on: "id"
      - table: "charges"
      - table: "onetimes"
      - table: "orders"
      - table: "subscriptions"

  - id: "charge-id"
    table: "charges"
    attribute: "charge_id"
    all-foreign-keys:
      - table: "charges"
        join-on: "id"
      - table: "orders"

  - id: "collection-id"
    table: "collections"
    attribute: "collection_id"
    all-foreign-keys:
      - table: "collections"
        join-on: "id"
      - table: "products"

  - id: "customer-id"
    table: "customers"
    attribute: "customer_id"
    all-foreign-keys:
      - table: "addresses"
      - table: "charges"
      - table: "customers"
        join-on: "id"
      - table: "onetimes"
      - table: "orders"
      - table: "subscriptions"

  - id: "discount-id"
    table: "discounts"
    attribute: "discount_id"
    all-foreign-keys:
      - table: "addresses"
      - table: "discounts"
        join-on: "id"

  - id: "onetime-id"
    table: "onetimes"
    attribute: "onetime_id"
    all-foreign-keys:
      - table: "onetimes"
        join-on: "id"

  - id: "order-id"
    table: "orders"
    attribute: "order_id"
    all-foreign-keys:
      - table: "orders"
        join-on: "id"

  - id: "product-id"
    table: "products"
    attribute: "product_id"
    all-foreign-keys:
      - table: "charges"
        subattribute: "line_items"
        join-on: "shopify_product_id"
      - table: "onetimes"
        join-on: "shopify_product_id"
      - table: "orders"
        subattribute: "line_items"
        join-on: "shopify_product_id"
      - table: "products"
        join-on: "id"
      - table: "subscriptions"

  - id: "subscription-id"
    table: "subscriptions"
    attribute: "subscription_id"
    all-foreign-keys:
      - table: "charges"
        subattribute: "line_items"
      - table: "orders"
        subattribute: "line_items"
      - table: "subscriptions"
        join-on: "id"
---