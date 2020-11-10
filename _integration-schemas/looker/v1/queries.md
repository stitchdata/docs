---
tap: "looker"
version: "1"
key: "query"

name: "queries"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/queries.json"
description: |
  The `{{ table.name }}` table contains info about the queries that exist in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get query"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/query#get_query"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The query ID."
    foreign-key-id: "query-id"

  - name: "client_id"
    type: "string"
    description: ""

  - name: "column_limit"
    type: "string"
    description: ""

  - name: "dynamic_fields"
    type: "string"
    description: ""

  - name: "expanded_share_url"
    type: "string"
    description: ""

  - name: "fields"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "fill_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "filter_config"
    type: "object"
    description: ""

  - name: "filter_expression"
    type: "string"
    description: ""

  - name: "filters"
    type: "object"
    description: ""

  - name: "has_table_calculations"
    type: "boolean"
    description: ""

  - name: "limit"
    type: "string"
    description: ""

  - name: "model"
    type: "string"
    description: ""

  - name: "pivots"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "query_timezone"
    type: "string"
    description: ""

  - name: "row_total"
    type: "string"
    description: ""

  - name: "runtime"
    type: "number"
    description: ""

  - name: "share_url"
    type: "string"
    description: ""

  - name: "slug"
    type: "string"
    description: ""

  - name: "sorts"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "subtotals"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "total"
    type: "boolean"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "view"
    type: "string"
    description: ""

  - name: "vis_config"
    type: "object"
    description: ""

  - name: "visible_ui_sections"
    type: "string"
    description: ""
---