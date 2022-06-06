---
tap: "shopify"
version: "1"

name: "inventory_levels"
doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/inventorylevel#top"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/inventory_levels.json"
description: |
  The `{{ table.name }}` table contains info about quantities of an inventory item for a location.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of inventory levels"
    doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/inventorylevel#get-inventory-levels"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "inventory_item_id"
    type: "integer"
    primary-key: true
    description: "The ID of the inventory item associated with the inventory level."

  - name: "location_id"
    type: "integer"
    primary-key: true
    description: "The ID of the location that the inventory level belongs to."

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","inventory level" | replace: "[ACTION]","modified" }}

  - name: "admin_graphql_api_id"
    type: "string"
    description: ""

  - name: "available"
    type: "integer"
    description: "The available quantity of an inventory item at the inventory level's associated location."
---