---
tap: "square"
version: "1"
key: "modifier-list"

name: "modifier_lists"
doc-link: "https://developer.squareup.com/reference/square/catalog-api/v1-list-modifier-lists"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/modifier_lists.json"
description: |
  The `{{ table.name }}` table contains information about modifier lists for a given location in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "List catalog (`type: modifier_list`) (V2)"
  doc-link: "https://developer.squareup.com/reference/square/catalog-api/list-catalog"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The modifier list ID."
    foreign-key-id: "modifier-list-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the modifier list was last updated."
    replication-key: true  

  - name: "absent_at_location_ids"
    type: "array"
    description: "A list of locations where the modifier list is unavailable."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the location where modifier list is unavailable."
        foreign-key-id: "location-id"
  
  - name: "is_deleted"
    type: "boolean"
    description: ""

  - name: "modifier_list_data"
    type: "object"
    description: ""
    subattributes:
      - name: "modifiers"
        type: "array"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""

          - name: "is_deleted"
            type: "boolean"
            description: ""

          - name: "modifier_data"
            type: "object"
            description: ""
            subattributes:
              - name: "modifier_list_id"
                type: "string"
                description: "The modifier list ID."
                foreign-key-id: "modifier-list-id"

              - name: "name"
                type: "string"
                description: ""

              - name: "on_by_default"
                type: "boolean"
                description: ""

              - name: "ordinal"
                type: "integer"
                description: ""

              - name: "price_money"
                type: "object"
                description: ""
                subattributes:
                  - name: "amount"
                    type: "integer"
                    description: ""

                  - name: "currency"
                    type: "string"
                    description: ""

          - name: "present_at_all_locations"
            type: "boolean"
            description: ""

          - name: "type"
            type: "string"
            description: ""

          - name: "updated_at"
            type: "date-time"
            description: ""

          - name: "version"
            type: "integer"
            description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "ordinal"
        type: "integer"
        description: ""

      - name: "selection_type"
        type: "string"
        description: ""

  - name: "present_at_all_locations"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: ""
  
  - name: "version"
    type: "integer"
    description: ""
---