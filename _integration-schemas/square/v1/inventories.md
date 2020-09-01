---
tap: "square"
version: "1"
key: ""

name: "inventories"
doc-link: "https://developer.squareup.com/reference/square/inventory-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/inventories.json"
description: |
  The `{{ table.name }}` table contains information about your inventory changes in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "Retrieve inventory changes"
    doc-link: "https://developer.squareup.com/reference/square/inventory-api/retrieve-inventory-changes"

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
    description: "The location ID of the inventory."
    foreign-key-id: "location-id"
  - name: "quantity"
    type: "string"
    description: ""
  - name: "state"
    type: "string"
    description: ""
---
