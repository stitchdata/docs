---
tap: "looker"
version: "1"
key: "dashboard-filter"

name: "dashboard_filters"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboard_filters"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/dashboard_filters.json"
description: |
  The `{{ table.name }}` table contains information about all dashboard filters in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all dashboard filters"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboard_filters"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The dashboard filter ID."
    foreign-key-id: "dashboard-filter-id"

  - name: "allow_multiple_values"
    type: "boolean"
    description: ""

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "default_value"
    type: "string"
    description: ""

  - name: "dimension"
    type: "string"
    description: ""

  - name: "explore"
    type: "string"
    description: ""

  - name: "field"
    type: "object"
    description: ""
  
  - name: "listens_to_filters"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "model"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "required"
    type: "boolean"
    description: ""

  - name: "row"
    type: "integer"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "ui_config"
    type: "object"
    description: ""
---