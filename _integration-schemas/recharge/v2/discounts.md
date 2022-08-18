---
tap: "recharge"
version: "2"
key: ""

name: "discounts"
doc-link: https://developer.rechargepayments.com/2021-11/discounts/discounts_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/discounts.json
description: |
  The `{{ table.name }}` table contains info about discounts.

replication-method: "Key-based Incremental"

api-method:
  name: "List discounts"
  doc-link: "https://developer.rechargepayments.com/2021-11/discounts/discounts_list"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The discount ID."
    foreign-key-id: "discount-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time the discount was created."

  - name: "applies_to"
    type: "object"
    description: ""
    subattributes:
      - name: "ids"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "integer"
            description: ""

      - name: "purchase_item_type"
        type: "string"
        description: ""

      - name: "resource"
        type: "string"
        description: ""


  - name: "applies_to_id"
    type: "integer"
    description: ""

  - name: "applies_to_product_type"
    type: "string"
    description: ""

  - name: "applies_to_resource"
    type: "string"
    description: ""

  - name: "channel_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "api"
        type: "object"
        description: ""
        subattributes:
          - name: "can_apply"
            type: "boolean"
            description: ""


      - name: "customer_portal"
        type: "object"
        description: ""
        subattributes:
          - name: "can_apply"
            type: "boolean"
            description: ""


      - name: "merchant_portal"
        type: "object"
        description: ""
        subattributes:
          - name: "can_apply"
            type: "boolean"
            description: ""


      - name: "checkout_page"
        type: "object"
        description: ""
        subattributes:
          - name: "can_apply"
            type: "boolean"
            description: ""



  - name: "code"
    type: "string"
    description: ""

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "duration"
    type: "string"
    description: ""

  - name: "duration_usage_limit"
    type: "integer"
    description: ""

  - name: "ends_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "external_discount_id"
    type: "object"
    description: ""
    subattributes:
      - name: "ecommerce"
        type: "string"
        description: ""


  - name: "first_time_customer_restriction"
    type: "boolean"
    description: ""

  - name: "once_per_customer"
    type: "boolean"
    description: ""

  - name: "prerequisite_subtotal_min"
    type: "string"
    description: ""

  - name: "starts_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "times_used"
    type: "integer"
    description: ""

  - name: "usage_limit"
    type: "integer"
    description: ""

  - name: "usage_limits"
    type: "object"
    description: ""
    subattributes:
      - name: "max_subsequent_redemptions"
        type: "integer"
        description: ""

      - name: "first_time_customer_restriction"
        type: "boolean"
        description: ""

      - name: "one_application_per_customer"
        type: "string"
        description: ""


  - name: "value"
    type: "string"
    description: ""

  - name: "value_type"
    type: "string"
    description: ""
---