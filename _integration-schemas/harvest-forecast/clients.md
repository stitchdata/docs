---
tap: "harvest-forecast"
version: "1.0"

name: "clients"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/clients.json

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "harvest_id"
    type: "integer"
    description: ""

  - name: "archived"
    type: "boolean"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""

  - name: "updated_by_id"
    type: "integer"
    description: ""
---
