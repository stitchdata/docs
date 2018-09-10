---
tap: "harvest-forecast"
version: "1.0"

name: "assignments"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/assignments.json

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "string"
    description: ""

  - name: "end_date"
    type: "string"
    description: ""

  - name: "allocation"
    type: "integer"
    description: ""

  - name: "notes"
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

  - name: "person_id"
    type: "integer"
    description: ""

  - name: "placeholder_id"
    type: "integer"
    description: ""

  - name: "repeated_assignment_set_id"
    type: "integer"
    description: ""

  - name: "active_on_days_off"
    type: "boolean"
    description: ""
---
