---
tap: "square"
version: "1"
key: "role"

name: "roles"
doc-link: "https://developer.squareup.com/reference/square/employees-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/roles.json"
description: |
  The `{{ table.name }}` table contains information about employees' roles in {{ integration.display_name }}. 

  **Note**: This table can't be replicated if the **Connect to a sandbox environment** box is checked in the [integration's settings](#add-stitch-data-source) due to limits imposed by {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List employee roles (V1)"
  doc-link: "https://developer.squareup.com/reference/square/employees-api/v1-list-employee-roles"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The role ID."
    # foreign-key-id: "role-id"

  - name: "created_at"
    type: "date-time"
    description: ""
  
  - name: "is_owner"
    type: "boolean"
    description: ""

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

  - name: "updated_at"
    type: "date-time"
    description: ""
---