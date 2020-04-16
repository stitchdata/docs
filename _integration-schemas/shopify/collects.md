---
tap: "shopify"
version: "1"

name: "collects"https://shopify.dev/docs/admin-api/rest/reference/products/collect?api[version]=2019-07"
singer-schema: "https://git
doc-link: "hub.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/collects.json"
description: |
  The `{{ table.name }}` table contains info about collects, which are used to manage relationships between products and custom collections. For every product in a custom collection, there's a collect that tracks the ID of both the product and the custom collection.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve all collects for the shop"
    doc-link: "https://shopify.dev/docs/admin-api/rest/reference/products/collect?api[version]=2019-07"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The collect ID."
    # foreign-key-id: "collect-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","collect" | replace: "[ACTION]","last updated" }}

  - name: "collection_id"
    type: "integer"
    description: "The ID of the custom collection containing the product."
    foreign-key-id: "collection-id"

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","collect" | replace: "[ACTION]","created" }}

  - name: "featured"
    type: "boolean"
    description: "Indicates whether the collect is featured."

  - name: "position"
    type: "integer"
    description: "The position of the product in a manually sorted custom collection."

  - name: "product_id"
    type: "integer"
    description: "The ID of the product in the custom collection."
    foreign-key-id: "product-id"

  - name: "sort_value"
    type: "string"
    description: "The same value as `position`, but padded with leading zeroes to make it alphanumeric-sortable."
---