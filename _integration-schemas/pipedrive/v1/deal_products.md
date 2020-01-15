---
tap: "pipedrive"
version: "1"
key: "deal-product"

name: "deal_products"
doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Deals"
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/deal_products.json"
description: |
  The `{{ table.name }}` table contains info about the products attached to deals.

replication-method: "Full Table"

api-method:
  name: "List products attached to a deal"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Deals/get_deals_id_products"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The deal product ID."
    #foreign-key-id: "deal-product-id"

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "string"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "deal_id"
    type: "integer"
    description: ""
    foreign-key-id: "deal-id"

  - name: "discount_percentage"
    type: "number"
    description: ""

  - name: "duration"
    type: "number"
    description: ""

  - name: "enabled_flag"
    type: "boolean"
    description: ""

  - name: "item_price"
    type: "number"
    description: ""

  - name: "last_edit"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "order_nr"
    type: "integer"
    description: ""

  - name: "product_id"
    type: "integer"
    description: ""
    foreign-key-id: "product-id"

  - name: "product_variation_id"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "quantity_formatted"
    type: "string"
    description: ""

  - name: "sum"
    type: "number"
    description: ""

  - name: "sum_formatted"
    type: "string"
    description: ""

  - name: "sum_no_discount"
    type: "number"
    description: ""
---