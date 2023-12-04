---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "4"
key: "user"

name: "users"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/users.json"
description: |
  This table contains information about users.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get all users (v2.0)"
  doc-link: "https://api.mambu.com/?http#users-getall"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    # foreign-key-id: "user-id"

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
            foreign-key-id: "branch-key"

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
    foreign-key-id: "branch-key"

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "custom_fields"
    type: "array"
    description: "The `custom_fields` field will be an array of the raw custom field set json objects."
    subattributes:
      - name: "field_set_id"
        type: "string"
        foreign-key-id: "custom-field-set-id"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "custom-field-id"

      - name: "value"
        type: "string"
        description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""
    foreign-key-id: "user-key"

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