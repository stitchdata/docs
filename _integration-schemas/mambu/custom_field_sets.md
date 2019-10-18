---
tap: "mambu"
version: "1.0"

name: "custom_field_sets"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/custom_field_sets.json"
description: "This table contains information about Custom Field Sets."

replication-method: "Full Table"

api-method:
    name: "Custom Field Sets"
    doc-link: "https://api.mambu.com/?shell#customfieldsets"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "custom-field-set-id"

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "custom_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "encoded_key"
        type: "string"
        description: ""
        # foreign-key-id: "custom-field-encoded-key"

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "data_type"
        type: "string"
        description: ""

      - name: "value_length"
        type: "string"
        description: ""

      - name: "is_default"
        type: "boolean"
        description: ""

      - name: "is_required"
        type: "boolean"
        description: ""

      - name: "index_in_list"
        type: "integer"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "unique"
        type: "boolean"
        description: ""

      - name: "view_rights"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "is_accessible_by_all_users"
            type: "boolean"
            description: ""

          - name: "roles"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""

      - name: "edit_rights"
        type: "object"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "is_accessible_by_all_users"
            type: "boolean"
            description: ""

          - name: "roles"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""

      - name: "amounts"
        type: "object"
        description: ""

      - name: "values"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "custom_field_product_settings"
        type: "array"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "link_type"
            type: "string"
            description: ""

          - name: "product_key"
            type: "string"
            description: ""

          - name: "is_default"
            type: "boolean"
            description: ""

          - name: "is_required"
            type: "boolean"
            description: ""

          - name: "custom_field_encoded_key"
            type: "string"
            description: ""

      - name: "custom_field_selection_options"
        type: "array"
        description: ""
        subattributes:
          - name: "encoded_key"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""

          - name: "score"
            type: "string"
            description: ""

          - name: "is_default"
            type: "string"
            description: ""

  - name: "encoded_key"
    type: "string"
    description: ""
    # foreign-key-id: "custom-field-set-encoded-key"

  - name: "index_in_list"
    type: "integer"
    description: ""

  - name: "last_modified_date"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "usage"
    type: "string"
    description: ""
---