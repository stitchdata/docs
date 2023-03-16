---
tap: "looker"
version: "1"
key: "role"

name: "roles"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/roles.json"
description: |
  The `{{ table.name }}` table contains info about the user roles in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all roles"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_roles"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The role ID."
    foreign-key-id: "role-id"

  - name: "model_set"
    type: "object"
    description: ""
    subattributes:
      - name: "all_access"
        type: "boolean"
        description: ""

      - name: "built_in"
        type: "boolean"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "model-set-id"

      - name: "models"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            foreign-key-id: "model-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "model_set_id"
    type: "string"
    description: ""
    foreign-key-id: "model-set-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "permission_set"
    type: "object"
    description: ""
    subattributes:
      - name: "all_access"
        type: "boolean"
        description: ""

      - name: "built_in"
        type: "boolean"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "permission-set-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "permissions"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            foreign-key-id: "permission-id"

      - name: "url"
        type: "string"
        description: ""

  - name: "permission_set_id"
    type: "string"
    description: ""
    foreign-key-id: "permission-set-id"

  - name: "url"
    type: "string"
    description: ""

  - name: "users_url"
    type: "string"
    description: ""
---