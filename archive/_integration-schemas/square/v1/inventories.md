---
tap: "square"
version: "1"
key: "inventory"

name: "inventories"
doc-link: "https://developer.squareup.com/reference/square/inventory-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/inventories.json"
description: |
  The `{{ table.name }}` table contains info about the current calculated stock count for a {{ integration.display_name }} location.

replication-method: "Full Table"
loading-behavior: "Append-Only"

api-method:
  name: "Retrieve inventory count (V2)"
  doc-link: "https://developer.squareup.com/reference/square/inventory-api/retrieve-inventory-count"

attributes:
  - name: "calculated_at"
    type: "date-time"
    description: ""

  - name: "catalog_object_id"
    type: "string"
    description: ""

  - name: "catalog_object_type"
    type: "string"
    description: ""

  - name: "location_id"
    type: "string"
    description: "The ID of the location associated with the inventory."
    foreign-key-id: "location-id"

  - name: "quantity"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""
---