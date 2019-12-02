---
tap: "3plcentral"
version: "1.0"

name: "stock_details"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/stock_details.json"
description: "This table contains information about stock details."

replication-method: "Full Table"

api-method:
    name: "3PL Central REL documentation"
    doc-link: "http://api.3plcentral.com/rels/inventory/stockdetails"

attributes:
  - name: "receive_item_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "receive-item-id"

  - name: "available"
    type: "number"
    description: ""

  - name: "cost"
    type: "number"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "expiration_date"
    type: "date-time"
    description: ""

  - name: "inventory_unit_of_measure_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "sku"
        type: "string"
        description: ""

  - name: "is_on_hold"
    type: "boolean"
    description: ""

  - name: "item_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "item-id"
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

  - name: "on_hand"
    type: "number"
    description: ""

  - name: "pallet_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
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

  - name: "po_num"
    type: "string"
    description: ""

  - name: "qualifier"
    type: "string"
    description: ""

  - name: "quarantined"
    type: "boolean"
    description: ""
  
  - name: "received"
    type: "number"
    description: ""

  - name: "received_date"
    type: "date-time"
    description: ""

  - name: "receiver_id"
    type: "integer"
    description: ""
    foreign-key-id: "receiver-id"

  - name: "reference_num"
    type: "string"
    description: ""

  - name: "saved_elements"
    type: "null"
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

  - name: "trailer_number"
    type: "string"
    description: ""
---
