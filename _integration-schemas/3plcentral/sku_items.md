---
tap: "3plcentral"
version: "1.0"

name: "sku_items"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/sku_items.json"
description: "This table contains information about SKU items."

replication-method: "Key-based Incremental"

api-method:
    name: "Get SKU items"
    doc-link: "http://api.3plcentral.com/rels/customers/items"

attributes:
  - name: "item_id"
    type: "integer"
    primary-key: true
    description: "The item ID."
    foreign-key-id: "item-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The time the item was last modified."
    replication-key: true  

  - name: "account_ref"
    type: "string"
    description: ""

  - name: "classification_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "cost"
    type: "number"
    description: ""

  - name: "country_of_manufacture"
    type: "string"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "customer_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "external_d"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: "The customer ID."
        foreign-key-id: "customer-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "deactivated"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "description2"
    type: "string"
    description: ""

  - name: "harmonized_code"
    type: "string"
    description: ""

  - name: "inventory_category"
    type: "string"
    description: ""

  - name: "item"
    type: "array"
    description: ""
    subattributes:
      - name: "qualifier"
        type: "string"
        description: ""
  
  - name: "kit"
    type: "object"
    description: ""
    subattributes:
      - name: "components"
        type: "array"
        description: ""
        subattributes:
          - name: "item_identifier"
            type: "array"
            description:
            subattributes:
              - name: "sku"
                type: "string"
                description: ""

              - name: "id"
                type: "integer"
                description: ""
                foreign-key-id: "item-identifier"

      - name: "material_notes"
        type: "string"
        description: ""

  - name: "last_price_change"
    type: "date-time"
    description: ""

  - name: "nmfc"
    type: "string"
    description: ""

  - name: "options"
    type: "object"
    description: ""
    subattributes:
      - name: "auto_hold_on_receive"
        type: "integer"
        description: ""

      - name: "days_between_counts"
        type: "integer"
        description: ""

      - name: "directed_put_away"
        type: "object"
        description: ""
        subattributes:
          - name: "allow_mixed_item_storage"
            type: "boolean"
            description: ""

          - name: "allow_mixed_lot_storage"
            type: "boolean"
            description: ""

          - name: "force_into_preferred_location"
            type: "boolean"
            description: ""

          - name: "location_zones"
            type: "string"
            description: ""

          - name: "mixed_expiration_days_threshold"
            type: "boolean"
            description: ""

          - name: "over_alloc_location_zones"
            type: "string"
            description: ""

          - name: "pallet_location_zones"
            type: "string"
            description: ""

          - name: "preferred_location_identifier"
            type: "object"
            description: ""
            subattributes:
              - name: "id"
                type: "integer"
                description: ""
                foreign-key-id: "location-id"

              - name: "name_key"
                type: "object"
                description: ""
                subattributes:
                  - name: "facility_identifier"
                    type: "object"
                    description: ""
                    subattributes:
                      - name: "id"
                        type: "integer"
                        description: "The facility ID."
                        foreign-key-id: "facility-id"

                      - name: "name"
                        type: "string"
                        description: ""

                  - name: "name"
                    type: "string"
                    description: ""

      - name: "haz_mat"
        type: "object"
        description: ""
        subattributes:
          - name: "flag"
            type: "string"
            description: ""

          - name: "flash_point"
            type: "string"
            description: ""

          - name: "hazard_class"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""

          - name: "is_haz_mat"
            type: "boolean"
            description: ""

          - name: "label_code"
            type: "string"
            description: ""

          - name: "packing_group"
            type: "string"
            description: ""

          - name: "shipping_name"
            type: "string"
            description: ""

      - name: "inventory_unit"
        type: "object"
        description: ""
        subattributes:
          - name: "inventory_method"
            type: "integer"
            description: ""

          - name: "maximum_stock"
            type: "number"
            description: ""

          - name: "minimum_stock"
            type: "number"
            description: ""

          - name: "reorder_quantity"
            type: "number"
            description: ""

          - name: "unit_identifier"
            type: "object"
            description: ""
            subattributes:
              - name: "id"
                type: "integer"
                description: ""

              - name: "name"
                type: "string"
                description: ""

      - name: "package_unit"
        type: "object"
        description: ""
        subattributes:
          - name: "imperial"
            type: "object"
            description: ""
            subattributes:
              - name: "height"
                type: "number"
                description: ""

              - name: "length"
                type: "number"
                description: ""

              - name: "net_weight"
                type: "number"
                description: ""

              - name: "weight"
                type: "number"
                description: ""

              - name: "width"
                type: "number"
                description: ""

          - name: "metric"
            type: "object"
            description: ""
            subattributes:
              - name: "height"
                type: "number"
                description: ""

              - name: "length"
                type: "number"
                description: ""

              - name: "net_weight"
                type: "number"
                description: ""

              - name: "weight"
                type: "number"
                description: ""

              - name: "width"
                type: "number"
                description: ""

          - name: "unit_identifier"
            type: "object"
            description: ""
            subattributes:
              - name: "id"
                type: "integer"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "upc"
            type: "string"
            description: ""

      - name: "pallets"
        type: "object"
        description: ""
        subattributes:
          - name: "high"
            type: "number"
            description: ""

          - name: "imperial"
            type: "object"
            description: ""
            subattributes:
              - name: "height"
                type: "number"
                description: ""

              - name: "length"
                type: "number"
                description: ""

              - name: "weight"
                type: "number"
                description: ""

              - name: "width"
                type: "number"
                description: ""

          - name: "metric"
            type: "object"
            description: ""
            subattributes:
              - name: "height"
                type: "number"
                description: ""

              - name: "length"
                type: "number"
                description: ""

              - name: "weight"
                type: "number"
                description: ""

              - name: "width"
                type: "number"
                description: ""

          - name: "qyt"
            type: "number"
            description: ""

          - name: "tie"
            type: "number"
            description: ""

          - name: "type_identifier"
            type: "object"
            description: ""
            subattributes:
              - name: "id"
                type: "integer"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "upc"
            type: "string"
            description: ""

      - name: "secondary_unit"
        type: "object"
        description: ""
        subattributes:
          - name: "inventory_also"
            type: "boolean"
            description: ""

          - name: "inventory_units_per_unit"
            type: "number"
            description: ""

          - name: "unit_identifier"
            type: "object"
            description: ""
            subattributes:
              - name: "id"
                type: "integer"
                description: ""

              - name: "name"
                type: "string"
                description: ""

      - name: "track_by"
        type: "object"
        description: ""
        subattributes:
          - name: "auto_hold_expiration_days_threshold"
            type: "integer"
            description: ""

          - name: "outbound_mobile_serialization"
            type: "integer"
            description: ""

          - name: "track_cost"
            type: "integer"
            description: ""

          - name: "track_expiration_date"
            type: "integer"
            description: ""

          - name: "track_lot_number"
            type: "integer"
            description: ""

          - name: "track_serial_number"
            type: "integer"
            description: ""

  - name: "price"
    type: "number"
    description: ""

  - name: "qualifier_renamers"
    type: "array"
    description: ""
    subattributes:
      - name: "qualifier"
        type: "string"
        description: ""

      - name: "renames"
        type: "string"
        description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "temperature"
    type: "number"
    description: ""

  - name: "upc"
    type: "string"
    description: ""
---