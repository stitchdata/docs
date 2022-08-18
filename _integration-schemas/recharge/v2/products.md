---
tap: "recharge"
version: "2"
key: ""

name: "products"
doc-link: https://developer.rechargepayments.com/2021-11/products/products_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/products.json
description: |
  The `{{ table.name }}` table contains info about your products. This table uses the 2021-01 API version.

replication-method: "Key-based Incremental"

api-method:
  name: "List products"
  doc-link: "https://developer.rechargepayments.com/2021-11/products/products_list"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time the product was last updated."

  - name: "collection_id"
    type: "integer"
    description: ""
    foreign-key-id: "collection-id"

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "discount_amount"
    type: "number"
    description: ""

  - name: "discount_type"
    type: "string"
    description: ""

  - name: "handle"
    type: "string"
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


  - name: "product_id"
    type: "integer"
    description: ""

  - name: "shopify_product_id"
    type: "integer"
    description: ""
    foreign-key-id: "product-id"

  - name: "subscription_defaults"
    type: "object"
    description: ""
    subattributes:
      - name: "charge_interval_frequency"
        type: "integer"
        description: ""

      - name: "cutoff_day_of_month"
        type: "string"
        description: ""

      - name: "cutoff_day_of_week"
        type: "string"
        description: ""

      - name: "expire_after_specific_number_of_charges"
        type: "integer"
        description: ""

      - name: "handle"
        type: "string"
        description: ""

      - name: "number_charges_until_expiration"
        type: "integer"
        description: ""

      - name: "order_day_of_month"
        type: "string"
        description: ""

      - name: "order_day_of_week"
        type: "string"
        description: ""

      - name: "order_interval_frequency"
        type: "integer"
        description: ""

      - name: "order_interval_frequency_options"
        type: "array"
        description: ""
        subattributes:
        - name: "items"
          type: "string"
          description: ""

      - name: "order_interval_unit"
        type: "string"
        description: ""

      - name: "storefront_purchase_options"
        type: "string"
        description: ""

      - name: "modifiable_properties"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""


  - name: "title"
    type: "string"
    description: ""
---