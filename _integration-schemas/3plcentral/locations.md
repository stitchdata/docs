---
tap: "3plcentral"
version: "1.0"

name: "locations"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/locations.json"
description: "This table contains information about inventory facility locations."

replication-method: "Full Table"

api-method:
    name: "Get inventory locations"
    doc-link: "http://api.3plcentral.com/rels/inventory/locations"

attributes:
  - name: "location_id"
    type: "integer"
    primary-key: true
    description: "The location ID."
    foreign-key-id: "location-id"

  - name: "facility_id"
    type: "integer"
    primary-key: true
    description: "The facility ID."
    foreign-key-id: "facility-id"
      
  - name: "customer_identifier"
    type: "object"
    description: "Details about the customer associated with the location."
    subattributes:
      - name: "external_id"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: "The customer ID"
        foreign-key-id: "customer-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "description"
    type: "string"
    description: ""
  
  - name: "item_traits"
    type: "object"
    description: ""
    subattributes:
      - name: "expiration_date"
        type: "date-time"
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

      - name: "lot_number"
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
                subattributes: &facility-identifier
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

      - name: "qualifier"
        type: "string"
        description: ""

      - name: "serial_number"
        type: "string"
        description: ""
  
  - name: "location_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: "The location ID."
        foreign-key-id: "location-id"

      - name: "name_key"
        type: "object"
        description: ""
        anchor-id: 2
        subattributes:
          - name: "facility_identifier"
            type: "object"
            description: ""
            anchor-id: 2
            subattributes: *facility-identifier

          - name: "name"
            type: "string"
            description: ""

  - name: "location_type_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "on_hand"
    type: "number"
    description: ""
---