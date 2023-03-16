---
tap: "looker"
version: "1"
key: "datagroup"

name: "datagroups"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/datagroup#get_all_datagroups"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/datagroups.json"
description: |
  The `{{ table.name }}` table contains information about all datagroups in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all datagroups"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/datagroup#get_all_datagroups"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The datagroup ID."
    # foreign-key-id: "datagroup-id"

  - name: "created_at"
    type: "integer"
    description: ""

  - name: "model_name"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "stale_before"
    type: "integer"
    description: ""

  - name: "trigger_check_at"
    type: "integer"
    description: ""

  - name: "trigger_error"
    type: "string"
    description: ""

  - name: "trigger_value"
    type: "string"
    description: ""

  - name: "triggered_at"
    type: "integer"
    description: ""
---