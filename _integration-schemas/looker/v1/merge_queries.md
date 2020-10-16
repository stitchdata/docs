---
tap: "looker"
version: "1"
key: "merge-query"

name: "merge_queries"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/merge_queries.json"
description: |
  The `{{ table.name }}` table contains info about the merge queries in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get merge query"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/query#get_merge_query"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The merge query ID."
    # foreign-key-id: "merge-query-id"

  - name: "column_limit"
    type: "string"
    description: ""

  - name: "dynamic_fields"
    type: "string"
    description: ""

  - name: "pivots"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "result_maker_id"
    type: "string"
    description: ""

  - name: "sorts"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "source_queries"
    type: "array"
    description: ""
    subattributes:
      - name: "merge_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "field_name"
            type: "string"
            description: ""

          - name: "source_field_name"
            type: "string"
            description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "query_id"
        type: "string"
        description: ""
        foreign-key-id: "query-id"

  - name: "total"
    type: "boolean"
    description: ""

  - name: "vis_config"
    type: "object"
    description: ""
---