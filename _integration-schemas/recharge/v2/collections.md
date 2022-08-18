---
tap: "recharge"
version: "2"
key: ""

name: "collections"
doc-link: https://developer.rechargepayments.com/2021-11/collection_products
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/collections.json
description: |
  The `{{ table.name }}` table contains info about your collections.

replication-method: "Key-based Incremental"

api-method:
  name: "List collections"
  doc-link: "https://developer.rechargepayments.com/2021-11/collection_products"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The collection ID."
    foreign-key-id: "collection-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time when the collection was last updated."

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "sort_order"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---