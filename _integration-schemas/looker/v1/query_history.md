---
tap: "looker"
version: "1"
key: ""

name: "query_history"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/query_history.json"
description: |
  The `{{ table.name }}` table contains info about

  TODO: I DON'T GET THIS ONE?

replication-method: "Full Table"

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "dashboard_id"
    type: "string"
    description: ""

  - name: "dims_hash_key"
    type: "string"
    description: ""

  - name: "history_created_date"
    type: "string"
    description: ""

  - name: "history_query_run_count"
    type: "integer"
    description: ""

  - name: "history_total_runtime"
    type: "number"
    description: ""

  - name: "look_id"
    type: "string"
    description: ""

  - name: "query_id"
    type: "string"
    description: ""

  - name: "query_model"
    type: "string"
    description: ""

  - name: "query_view"
    type: "string"
    description: ""

  - name: "space_id"
    type: "string"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
---