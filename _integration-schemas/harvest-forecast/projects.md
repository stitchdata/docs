---
tap: "harvest-forecast"
version: "1.0"

name: "projects"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/projects.json

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "color"
    type: "string"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "start_date"
    type: "string"
    description: ""

  - name: "end_date"
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

  - name: "client_id"
    type: "integer"
    description: ""

  - name: "tags"
    type: "object"
    description: ""

    object-attributes: 
  - name: "tags"
    type: "string"
    description: ""

