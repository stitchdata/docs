---
tap: "chargify"
version: "1"
key: "coupon"

name: "coupons"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/coupons.json"
description: |
  The `{{ table.name }}` table contains info about coupons associated with a product family in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "Read coupons for a specific product family"
  doc-link: "https://reference.chargify.com/v1/coupons-editing/list-product-family-coupons"
  
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The coupon ID."
    # foreign-key-id: "coupon-id"

  - name: "allow_negative_balance"
    type: "boolean"
    description: ""

  - name: "amount_in_cents"
    type: "number"
    description: ""

  - name: "archived_at"
    type: "date-time"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "compounding_strategy"
    type: "string"
    description: ""

  - name: "conversion_limit"
    type: "number"
    description: ""

  - name: "coupon_restrictions"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "duration_interval"
    type: "integer"
    description: ""

  - name: "duration_interval_unit"
    type: "string"
    description: ""

  - name: "duration_period_count"
    type: "number"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "percentage"
    type: "number"
    description: ""

  - name: "product_family_id"
    type: "integer"
    description: ""
    foreign-key-id: "product-family-id"

  - name: "recurring"
    type: "boolean"
    description: ""

  - name: "stackable"
    type: "boolean"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---