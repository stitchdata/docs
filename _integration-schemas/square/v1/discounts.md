---
tap: "square"
version: "1"
key: ""

name: "discounts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/discounts.json"
description: |
  The `{{ table.name }}` table contains information about discounts for a given location in {{ integration.display_name }}. This table has been deprecated in {{ integration.display_name }}, effective November 20, 2019.

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The discount ID."
    foreign-key-id: 

  - name: "updated_at"
    type: "date-time"
    description: "The time the location was last updated."
      
  - name: "absent_at_location_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The location IDs were discounts don't apply."
        foreign-key-id: "location-id"
  - name: "discount_data"
    type: "object"
    description: ""
    subattributes:
      - name: "amount_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""
          - name: "currency"
            type: "string"
            description: ""
      - name: "application_method"
        type: "string"
        description: ""
      - name: "discount_type"
        type: "string"
        description: ""
      - name: "label_color"
        type: "string"
        description: ""
      - name: "modify_tax_basis"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "percentage"
        type: "string"
        description: ""
      - name: "pin_required"
        type: "boolean"
        description: ""
  
  - name: "is_deleted"
    type: "boolean"
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
