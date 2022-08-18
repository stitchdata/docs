---
tap: "recharge"
version: "2"
key: ""

name: "onetimes"
doc-link: https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/onetimes.json
description: |
  The `{{ table.name }}` table contains info about one time products.

replication-method: "Key-based Incremental"

api-method:
  name: "List onetimes"
  doc-link: "https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the one time product."
    #foreign-key-id: "onetime-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time the one time product was last updated."

  - name: "address_id"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

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


  - name: "next_charge_scheduled_at"
    format: "date-time"
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
    foreign-key-id: "product-id"

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