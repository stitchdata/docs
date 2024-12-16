---
tap: "square"
version: "1"
key: "tax"

name: "taxes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/taxes.json"
description: |
  The `{{ table.name }}` table contains information about taxes enabled on your items in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "List catalog (`type: tax`) (V2)"
  doc-link: "https://developer.squareup.com/reference/square/catalog-api/list-catalog"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The tax ID."
    foreign-key-id: "tax-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the tax was last updated."
    replication-key: true  

  - name: "absent_at_location_ids"
    type: "array"
    description: "A list of locations where the tax is not applicable."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the location where the tax is not applicable."
        foreign-key-id: "location-id"
  
  - name: "is_deleted"
    type: "boolean"
    description: ""

  - name: "present_at_all_locations"
    type: "boolean"
    description: ""

  - name: "tax_data"
    type: "object"
    description: ""
    subattributes:
      - name: "applies_to_custom_amounts"
        type: "boolean"
        description: ""

      - name: "calculation_phase"
        type: "string"
        description: ""

      - name: "enabled"
        type: "boolean"
        description: ""

      - name: "inclusion_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "percentage"
        type: "string"
        description: ""

      - name: "tax_type_id"
        type: "string"
        description: ""

      - name: "tax_type_name"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""
  
  - name: "version"
    type: "integer"
    description: ""
---