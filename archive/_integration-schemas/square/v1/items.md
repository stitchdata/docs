---
tap: "square"
version: "1"
key: "item"

name: "items"
doc-link: "https://developer.squareup.com/reference/square/catalog-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/items.json"
description: |
  The `{{ table.name }}` table contains information about items for a given location in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "List catalog (`type: item`) (V2)"
  doc-link: "https://developer.squareup.com/reference/square/catalog-api/list-catalog"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The item ID."
    foreign-key-id: "item-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the item was last updated."
    replication-key: true  

  - name: "absent_at_location_ids"
    type: "array"
    description: "A list of locations where the item is unavailable."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the location where the item is unavailable."
        foreign-key-id: "location-id"
  
  - name: "is_deleted"
    type: "boolean"
    description: ""

  - name: "item_data"
    type: "object"
    description: ""
    subattributes:
      - name: "abbreviation"
        type: "string"
        description: ""

      - name: "available_electronically"
        type: "boolean"
        description: ""

      - name: "available_for_pickup"
        type: "boolean"
        description: ""

      - name: "available_online"
        type: "boolean"
        description: ""

      - name: "category_id"
        type: "string"
        description: ""
        foreign-key-id: "category-id"

      - name: "description"
        type: "string"
        description: ""

      - name: "item_options"
        type: "array"
        description: ""
        subattributes:
          - name: "item_option_id"
            type: "string"
            description: ""

      - name: "label_color"
        type: "string"
        description: ""

      - name: "modifier_list_info"
        type: "array"
        description: ""
        subattributes:
          - name: "enabled"
            type: "boolean"
            description: ""

          - name: "modifier_list_id"
            type: "string"
            description: ""
            foreign-key-id: "modifier-list-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "product_type"
        type: "string"
        description: ""

      - name: "skip_modifier_screen"
        type: "boolean"
        description: ""

      - name: "tax_ids"
        type: "array"
        description: "A list of taxes enabled for the item."
        subattributes:
          - name: "value"
            type: "string"
            description: "The ID of the tax enabled for the item."
            foreign-key-id: "tax-id"

      - name: "variations"
        type: "array"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""

          - name: "is_deleted"
            type: "boolean"
            description: ""

          - name: "item_variation_data"
            type: "object"
            description: ""
            subattributes:
              - name: "inventory_alert_type"
                type: "string"
                description: ""

              - name: "item_id"
                type: "string"
                description: "The item ID."
                foreign-key-id: "item-id"

              - name: "location_overrides"
                type: "array"
                description: ""
                subattributes:
                  - name: "inventory_alert_threshold"
                    type: "integer"
                    description: ""

                  - name: "inventory_alert_type"
                    type: "string"
                    description: ""

                  - name: "location_id"
                    type: "string"
                    description: "The location ID."
                    foreign-key-id: "location-id"

                  - name: "track_inventory"
                    type: "boolean"
                    description: ""

              - name: "name"
                type: "string"
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

              - name: "pricing_type"
                type: "string"
                description: ""

              - name: "sku"
                type: "string"
                description: ""

              - name: "track_inventory"
                type: "boolean"
                description: ""

              - name: "user_data"
                type: "string"
                description: ""

          - name: "present_at_all_locations"
            type: "boolean"
            description: ""

          - name: "present_at_location_ids"
            type: "array"
            description: "A list of locations where the item is available."
            subattributes:
              - name: "value"
                type: "string"
                description: "The ID of the location where the item is available."
                foreign-key-id: "location-id"

          - name: "type"
            type: "string"
            description: ""

          - name: "updated_at"
            type: "date-time"
            description: ""

          - name: "version"
            type: "integer"
            description: ""

      - name: "visibility"
        type: "string"
        description: ""

  - name: "present_at_all_locations"
    type: "boolean"
    description: ""

  - name: "present_at_location_ids"
    type: "array"
    description: "A list of locations where the item is available."
    subattributes:
      - name: "value"
        type: "string"
        description: "The location IDs where the items are available."
        foreign-key-id: "location-id"

  - name: "type"
    type: "string"
    description: ""

  - name: "version"
    type: "integer"
    description: ""
---