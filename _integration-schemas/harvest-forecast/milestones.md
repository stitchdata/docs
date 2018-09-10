---
tap: "harvest-forecast"
version: "1.0"

name: "milestones"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/milestones.json

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "date"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""

  - name: "updated_by_id"
    type: "integer"
    description: ""

  - name: "project_id"
    type: "integer"
    description: ""
---
