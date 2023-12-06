---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "shopify"

version: "1"

foreign-keys:
  - id: "collects-id"
    table: "collects"
    attribute: "collects_id"
    all-foreign-keys:
      - table: "collects"
        join-on: "id"

  - id: "collection-id"
    table: "custom_collections"
    attribute: "collection_id"
    all-foreign-keys:
      - table: "collects"
      - table: "custom_collections"
        join-on: "id"

  - id: "customer-id"
    table: "customers"
    attribute: "customer_id"
    all-foreign-keys:
      - table: "abandoned_checkouts"
        subattribute: "customer__default_address"
        join-on: "customer_id"

      - table: "abandoned_checkouts"
        subattribute: "customer"
        join-on: "id"

      - table: "abandoned_checkouts"

      - table: "customers"
        join-on: "id"

      - table: "customers"
        subtable: "addresses"
        join-on: "id"

  - id: "metafield-id"
    table: "metafields"
    attribute: "metafield_id"
    all-foreign-keys:
      - table: "metafields"
        join-on: "id"

  - id: "order-id"
    table: "orders"
    attribute: "order_id"
    all-foreign-keys:
      - table: "abandoned_checkouts"
        subattribute: "customer"
        join-on: "last_order_id"

      - table: "customers"
        join-on: "last_order_id"

      - table: "order_refunds"

      - table: "orders"
        join-on: "id"

      - table: "orders"
        subtable: "refunds__order_adjustments"

      - table: "transactions"

  - id: "order-refund-id"
    table: "order_refunds"
    attribute: "refund_id"
    all-foreign-keys:
      - table: "order_refunds"
        join-on: "id"

      - table: "orders"
        subtable: "refunds"
        join-on: "id"

      - table: "orders"
        subtable: "refunds__order_adjustments"

  - id: "product-id"
    table: "product"
    attribute: "product_id"
    all-foreign-keys:
      - table: "abandoned_checkouts"
        subatable: "line_items"

      - table: "collects"

      - table: "order_refunds"
        subtable: "refund_line_items"
        subattribute: "line_item"

      - table: "orders"
        subtable: "fulfillments__line_items"

      - table: "orders"
        subtable: "refunds__refund_line_items"

      - table: "products"
        join-on: "id"

      - table: "products"
        subtable: "options"

  - id: "transaction-id"
    table: "transactions"
    attribute: "transaction_id"
    all-foreign-keys:
      - table: "transactions"
        join-on: "id"
      - table: "transactions"
        join-on: "parent_id"
---