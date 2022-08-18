---
tap: "recharge"
version: "2"
key: ""

name: "subscriptions"
doc-link: https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/subscriptions.json
description: |
  The `{{ table.name }}` table contains info about subscriptions. Subscriptions are individual items that customers receive on a recurring basis.

replication-method: "Key-based Incremental"

api-method:
  name: "List subscriptions"
  doc-link: "https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the subscription."
    foreign-key-id: "subscription-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time the subscription was created."

  - name: "address_id"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "analytics_data"
    type: "object"
    description: ""
    subattributes:
      - name: "utm_params"
        type: "array"
        description: ""
        subattributes:
          - name: "utm_campaign"
            type: "string"
            description: ""

          - name: "utm_content"
            type: "string"
            description: ""

          - name: "utm_data_source"
            type: "string"
            description: ""

          - name: "utm_medium"
            type: "string"
            description: ""

          - name: "utm_source"
            type: "string"
            description: ""

          - name: "utm_term"
            type: "string"
            description: ""

          - name: "utm_timestamp"
            type: "string"
            description: ""

  - name: "cancellation_reason"
    type: "string"
    description: ""

  - name: "cancellation_reason_comments"
    type: "string"
    description: ""

  - name: "cancelled_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "charge_interval_frequency"
    type: "string"
    description: ""

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "expire_after_specific_number_of_charges"
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


  - name: "has_queued_charges"
    type: "boolean"
    description: ""

  - name: "is_prepaid"
    type: "boolean"
    description: ""

  - name: "is_skippable"
    type: "boolean"
    description: ""

  - name: "is_swappable"
    type: "boolean"
    description: ""

  - name: "max_retries_reached"
    type: "boolean"
    description: ""

  - name: "next_charge_scheduled_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "order_day_of_month"
    type: "string"
    description: ""

  - name: "order_day_of_week"
    type: "string"
    description: ""

  - name: "order_interval_frequency"
    type: "string"
    description: ""

  - name: "order_interval_unit"
    type: "string"
    description: ""

  - name: "presentment_currency"
    type: "string"
    description: ""

  - name: "price"
    type: "string"
    description: ""

  - name: "product_title"
    type: "string"
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

  - name: "recharge_product_id"
    type: "integer"
    description: ""

  - name: "shopify_product_id"
    type: "integer"
    description: ""
    foreign-key-id: "product-id"

  - name: "shopify_variant_id"
    type: "integer"
    description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "sku_override"
    type: "boolean"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "variant_title"
    type: "string"
    description: ""
---