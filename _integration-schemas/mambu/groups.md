---
tap: "mambu"
version: "1.0"

name: "groups"
doc-link: "https://api.mambu.com/?shell#welcome"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/groups.json"
description: "This table contains information about Groups."

replication-method: "Key-based Incremental"

api-method:
  name: "Get all groups"
  doc-link: "https://api.mambu.com/?http#groups-getall"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The group ID."
#   foreign-key-id: "group-id"

  - name: "last_modified_date"
    type: "date-time"
    description: "The date and time the group was last modified."
    replication-key: true

  - name: "addresses"
    type: "array"
    description: ""
    subattributes:
      - name: "country"
        type: "string"
        description: ""

      - name: "parent_key"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "latitude"
        type: "number"
        description: ""

      - name: "postcode"
        type: "string"
        description: ""

      - name: "index_in_list"
        type: "integer"
        description: ""

      - name: "encoded_key"
        type: "string"
        description: ""

      - name: "region"
        type: "string"
        description: ""

      - name: "line2"
        type: "string"
        description: ""

      - name: "line1"
        type: "string"
        description: ""

      - name: "longitude"
        type: "number"
        description: ""

  - name: "assigned_branch_key"
    type: "string"
    description: ""
    foreign-key-id: "branch-encoded-key"

  - name: "assigned_centre_key"
    type: "string"
    description: ""
    foreign-key-id: "centre-encoded-key"

  - name: "assigned_user_key"
    type: "string"
    description: ""
    foreign-key-id: "user-encoded-key"

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

  - name: "email_address"
    type: "string"
    description: ""

  - name: "encoded_key"
    type: "string"
    description: ""

  - name: "group_members"
    type: "array"
    description: ""
    subattributes:
      - name: "clientKey"
        type: "string"
        description: ""
        foreign-key-id: "client-encoded-key"

      - name: "roles"
        type: "array"
        description: ""
        subattributes:
          - name: "roleName"
            type: "string"
            description: ""

          - name: "encodedKey"
            type: "string"
            description: ""

          - name: "groupRoleNameKey"
            type: "string"
            description: ""

  - name: "group_name"
    type: "string"
    description: ""

  - name: "group_role_key"
    type: "string"
    description: ""

  - name: "home_phone"
    type: "string"
    description: ""

  - name: "loan_cycle"
    type: "string"
    description: ""

  - name: "migration_event_key"
    type: "string"
    description: ""

  - name: "mobile_phone"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "preferred_language"
    type: "string"
    description: ""
---