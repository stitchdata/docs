---
tap: "mambu"
version: "1.0"
name: "users"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/users.json"
description: "This table contains information about Users."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all users"
  doc-link: "https://api.mambu.com/?http#users-getall"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
#    foreign-key-id: "user-id"

  - name: "last_modified_date"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "access"
    type: "object"
    description: ""
    subattributes:
      - name: "administrator_access"
        type: "boolean"
        description: ""

      - name: "api_access"
        type: "boolean"
        description: ""

      - name: "can_manage_all_branches"
        type: "boolean"
        description: ""

      - name: "can_manage_entities_assigned_to_other_officers"
        type: "string"
        description: ""

      - name: "credit_officer_access"
        type: "boolean"
        description: ""

      - name: "mambu_access"
        type: "boolean"
        description: ""

      - name: "managed_branches"
        type: "array"
        description: ""
        subattributes:
          - name: "branch_key"
            type: "string"
            description: ""
            foreign-key-id: "branch-encoded-key"

      - name: "permissions"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "boolean"
            description: ""

      - name: "support_access"
        type: "boolean"
        description: ""

      - name: "teller_access"
        type: "boolean"
        description: ""

  - name: "assigned_branch_key"
    type: "string"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "custom_field_sets"
    type: "array"
    description: ""
    subattributes:
      - name: "custom_field_set_id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-set-id"

      - name: "custom_field_values"
        type: "array"
        description: ""
        subattributes:
          - name: "custom_field_id"
            type: "string"
            description: ""
            foreign-key-id: "custom-field-id"
          - name: "custom_field_value"
            type: "string"
            description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "home_phone"
    type: "string"
    description: ""

  - name: "language"
    type: "string"
    description: ""

  - name: "last_logged_in_date"
    type: "date-time"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "mobile_phone"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "two_factor_authentication"
    type: "boolean"
    description: ""

  - name: "user_state"
    type: "string"
    description: ""

  - name: "username"
    type: "string"
    description: ""
---