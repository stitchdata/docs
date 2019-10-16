---
tap: "mambu"
version: "1.0"

name: "custom_field_sets"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/custom_field_sets.json"
description: "This table contains information about Custom Field Sets."

replication-method: "Full Table"

api-method:
    name: "Custom Field Sets"
    doc-link: "https://api.mambu.com/?shell#customfieldsets"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "custom_fields"
    type: "null"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "index_in_list"
    type: "integer"
    description: ""

  - name: "last_modified_date"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "usage"
    type: "string"
    description: ""
---
