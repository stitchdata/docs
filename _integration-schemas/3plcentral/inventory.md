---
tap: "3plcentral"
version: "1.0"

name: "inventory"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/inventory.json"
description: "This table contains information about inventory."

replication-method: "Full Table"

api-method:
    name: "3PL Central REL documentaion"
    doc-link: "http://api.3plcentral.com/rels/inventory/inventory"

attributes:
  - name: "receive_item_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "receive-item-id"

  - name: "available_qty"
    type: "number"
    description: ""

  - name: "cost"
    type: "number"
    description: ""

  - name: "customer_identifier"
    type: "object"
    description: ""
    foreign-key-id: "customer-id"

    subattributes:
      - name: "external_d"
        type: "string"
        description: ""
      - name: "id"
        type: "integer"
        description: ""
      - name: "name"
        type: "string"
        description: ""

  - name: "expiration_date"
    type: "date-time"
    description: ""

  - name: "facility_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "facility-id"
      - name: "name"
        type: "string"
        description: ""

  - name: "inventory_unit_of_measure_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "name"
        type: "string"
        description: ""

  - name: "inventory_units_per_secondary_unity"
    type: "number"
    description: ""

  - name: "item_description"
    type: "string"
    description: ""

  - name: "item_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "item-identifier"
      - name: "sku"
        type: "string"
        description: ""

  - name: "location_identifier"
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
                description: ""
              - name: "name"
                type: "string"
                description: ""
          - name: "name"
            type: "string"
            description: ""

  - name: "lot_number"
    type: "string"
    description: ""

  - name: "on_hand_qty"
    type: "number"
    description: ""

  - name: "on_hold"
    type: "boolean"
    description: ""

  - name: "on_hold_date"
    type: "date-time"
    description: ""

  - name: "on_hold_qty"
    type: "number"
    description: ""

  - name: "on_hold_reason"
    type: "string"
    description: ""

  - name: "on_hold_user_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "name"
        type: "string"
        description: ""

  - name: "pallet_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "pallet-id"  
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
                description: ""
              - name: "name"
                type: "string"
                description: ""
          - name: "name"
            type: "string"
            description: ""

  - name: "qualifier"
    type: "string"
    description: ""

  - name: "quarantined"
    type: "boolean"
    description: ""

  - name: "receive_qty"
    type: "number"
    description: ""

  - name: "received_date"
    type: "date-time"
    description: ""

  - name: "receiver_id"
    type: "integer"
    description: ""

  - name: "secondary_available_qty"
    type: "number"
    description: ""

  - name: "secondary_on_hand_qty"
    type: "number"
    description: ""

  - name: "secondary_on_hold_qty"
    type: "number"
    description: ""

  - name: "secondary_received_qty"
    type: "number"
    description: ""

  - name: "secondary_unit_of_measure_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "name"
        type: "string"
        description: ""
  
  - name: "serial_number"
    type: "string"
    description: ""
  
  - name: "supplier_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "supplier-id"
      - name: "name"
        type: "string"
        description: ""
  
  - name: "weight_imperial"
    type: "number"
    description: ""
  - name: "weight_imperial_available"
    type: "number"
    description: ""
  - name: "weight_imperial_on_hand"
    type: "number"
    description: ""
  - name: "weight_metric"
    type: "number"
    description: ""
  - name: "weight_metric_available"
    type: "number"
    description: ""
  - name: "weight_metric_on_hand"
    type: "number"
    description: ""
---
