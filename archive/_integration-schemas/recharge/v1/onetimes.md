---
tap: "recharge"
version: "1"
key: "onetime"

name: "onetimes"
doc-link: "https://developer.rechargepayments.com/#list-onetimes-alpha"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/onetimes.json"
description: |
  The `{{ table.name }}` table contains info about one time products.

replication-method: "Key-based Incremental"
api-method:
  name: "List onetimes"
  doc-link: "https://developer.rechargepayments.com/#list-onetimes-alpha"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the one time product."
    # foreign-key-id: "onetime-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the one time product was last updated."

  - name: "address_id"
    type: "integer"
    description: "The ID of the address the one time product is associated with."
    foreign-key-id: "address-id"

  - name: "created_at"
    type: "date-time"
    description: "The date and time the one time product was created."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer the one time product is associated with."
    foreign-key-id: "customer-id"

  - name: "next_charge_scheduled_at"
    type: "date-time"
    description: "The date of the one time product execution."

  - name: "price"
    type: "number"
    description: "The price of the item before discounts, taxes, or shipping have been applied."

  - name: "product_title"
    type: "string"
    description: "The name of the one time product in a shop's catalog."

  - name: "properties"
    type: "array"
    description: ""
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "quantity"
    type: "integer"
    description: "The number of items in the subscription."

  - name: "recharge_product_id"
    type: "integer"
    description: "The ID of the product in {{ integration.display_name }}."
    # foreign-key-id: "product-id"

  - name: "shopify_product_id"
    type: "integer"
    description: "The ID of the product in Shopify."
    foreign-key-id: "product-id"

  - name: "shopify_variant_id"
    type: "integer"
    description: "The ID of the product variant in Shopify."
    foreign-key-id: "variant-id"

  - name: "sku"
    type: "string"
    description: "A unique identifier of the item in the fulfillment."

  - name: "status"
    type: "string"
    description: "The status of the one time product."

  - name: "variant_title"
    type: "string"
    description: "The name of the variant in a shop’s catalog."
---