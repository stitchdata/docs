---
tap: "recharge"
version: "2"
key: ""

name: "orders"
doc-link: https://developer.rechargepayments.com/2021-11/orders/orders_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/orders.json
description: |
  The `{{ table.name }}` table contains info about orders. Orders are created after a charge is successfully processed.

replication-method: "Key-based Incremental"

api-method:
  name: "List orders"
  doc-link: "https://developer.rechargepayments.com/2021-11/orders/orders_list"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The unique numeric identifier for the order."
    #foreign-key-id: "order-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date time at which the order was most recently updated."

  - name: "address_id"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "address_is_active"
    type: "integer"
    description: ""

  - name: "billing_address"
    type: "object"
    description: ""
    subattributes:
      - name: "address1"
        type: "string"
        description: ""

      - name: "address2"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "company"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "province"
        type: "string"
        description: ""

      - name: "zip"
        type: "string"
        description: ""

      - name: "country_code"
        type: "string"
        description: ""


  - name: "charge"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "external_transaction_id"
        type: "object"
        description: ""
        subattributes:
          - name: "payment_processor"
            type: "string"
            description: ""



  - name: "charge_id"
    type: "integer"
    description: ""
    foreign-key-id: "charge-id"

  - name: "charge_status"
    type: "string"
    description: ""

  - name: "client_details"
    type: "object"
    description: ""
    subattributes:
      - name: "browser_ip"
        type: "string"
        description: ""

      - name: "user_agent"
        type: "string"
        description: ""


  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customer"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "external_customer_id"
        type: "object"
        description: ""
        subattributes:
          - name: "ecommerce"
            type: "string"
            description: ""


      - name: "hash"
        type: "string"
        description: ""


  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "discount_codes"
    type: "array"
    description: ""
    subattributes:
      - name: "amount"
        type: "string"
        description: ""

      - name: "code"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "discounts"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "code"
        type: "string"
        description: ""

      - name: "value"
        type: "number"
        description: ""

      - name: "value_type"
        type: "string"
        description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "external_cart_token"
    type: "string"
    description: ""

  - name: "external_order_id"
    type: "object"
    description: ""
    subattributes:
      - name: "ecommerce"
        type: "string"
        description: ""


  - name: "external_order_number"
    type: "object"
    description: ""
    subattributes:
      - name: "ecommerce"
        type: "string"
        description: ""


  - name: "first_name"
    type: "string"
    description: ""

  - name: "hash"
    type: "string"
    description: ""

  - name: "is_prepaid"
    type: "boolean"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "line_items"
    type: "array"
    description: ""
    subattributes:
      - name: "grams"
        type: "integer"
        description: ""

      - name: "images"
        type: "object"
        description: ""
        subattributes:
          - name: "large"
            type: "string"
            description: ""

          - name: "medium"
            type: "string"
            description: ""

          - name: "original"
            type: "string"
            description: ""

          - name: "small"
            type: "string"
            description: ""

          - name: "sort_order"
            type: "integer"
            description: ""


      - name: "price"
        type: "number"
        description: ""

      - name: "properties"
        type: "array"
        description: ""
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""


      - name: "quantity"
        type: "integer"
        description: ""

      - name: "shopify_product_id"
        type: "string"
        description: ""
        foreign-key-id: "product-id"

      - name: "shopify_variant_id"
        type: "string"
        description: ""

      - name: "sku"
        type: "string"
        description: ""

      - name: "subscription_id"
        type: "integer"
        description: ""
        foreign-key-id: "subscription-id"

      - name: "title"
        type: "string"
        description: ""

      - name: "variant_title"
        type: "string"
        description: ""

      - name: "purchase_item_id"
        type: "integer"
        description: ""

      - name: "external_product_id"
        type: "object"
        description: ""
        subattributes:
          - name: "ecommerce"
            type: "string"
            description: ""


      - name: "external_variant_id"
        type: "object"
        description: ""
        subattributes:
          - name: "ecommerce"
            type: "string"
            description: ""


      - name: "handle"
        type: "string"
        description: ""

      - name: "sort_order"
        type: "integer"
        description: ""

      - name: "purchase_item_type"
        type: "string"
        description: ""

      - name: "tax_due"
        type: "string"
        description: ""

      - name: "tax_lines"
        type: "array"
        description: ""
        subattributes:
          - name: "price"
            type: "string"
            description: ""

          - name: "rate"
            type: "string"
            description: ""

          - name: "title"
            type: "string"
            description: ""


      - name: "taxable"
        type: "boolean"
        description: ""

      - name: "taxable_amount"
        type: "string"
        description: ""

      - name: "total_price"
        type: "string"
        description: ""

      - name: "unit_price"
        type: "string"
        description: ""

      - name: "unit_price_includes_tax"
        type: "boolean"
        description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "note_attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "order_attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "payment_processor"
    type: "string"
    description: ""

  - name: "processed_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "scheduled_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "shipped_date"
    format: "date-time"
    type: "string"
    description: ""

  - name: "shipping_address"
    type: "object"
    description: ""
    subattributes:
      - name: "address1"
        type: "string"
        description: ""

      - name: "address2"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "company"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "province"
        type: "string"
        description: ""

      - name: "zip"
        type: "string"
        description: ""

      - name: "country_code"
        type: "string"
        description: ""


  - name: "shipping_date"
    format: "date-time"
    type: "string"
    description: ""

  - name: "shipping_lines"
    type: "array"
    description: ""
    subattributes:
      - name: "code"
        type: "string"
        description: ""

      - name: "price"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""

      - name: "source"
        type: "string"
        description: ""

      - name: "taxable"
        type: "string"
        description: ""

      - name: "tax_lines"
        type: "array"
        description: ""
        subattributes:
          - name: "price"
            type: "string"
            description: ""

          - name: "rate"
            type: "string"
            description: ""

          - name: "title"
            type: "string"
            description: ""

  - name: "shopify_cart_token"
    type: "string"
    description: ""

  - name: "shopify_customer_id"
    type: "string"
    description: ""

  - name: "shopify_id"
    type: "string"
    description: ""

  - name: "shopify_order_id"
    type: "string"
    description: ""

  - name: "shopify_order_number"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subtotal_price"
    type: "string"
    description: ""

  - name: "tags"
    type: "string"
    description: ""

  - name: "tax_lines"
    type: "array"
    description: ""
    subattributes:
      - name: "code"
        type: "string"
        description: ""

      - name: "price"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""

      - name: "rate"
        type: "string"
        description: ""

  - name: "taxable"
    type: "boolean"
    description: ""

  - name: "total_discounts"
    type: "string"
    description: ""

  - name: "total_line_items_price"
    type: "number"
    description: ""

  - name: "total_price"
    type: "string"
    description: ""

  - name: "total_refunds"
    type: "string"
    description: ""

  - name: "total_tax"
    type: "string"
    description: ""

  - name: "total_weight"
    type: "integer"
    description: ""

  - name: "total_weight_grams"
    type: "integer"
    description: ""

  - name: "transaction_id"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---