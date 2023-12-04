---
tap: "looker"
version: "1"
key: "permission-set"

name: "permission_sets"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/permission_sets.json"
description: |
  The `{{ table.name }}` table contains info about the role permission sets in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all permission sets"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_permission_sets"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The permission set ID."
    foreign-key-id: "permission-set-id"

  - name: "all_access"
    type: "boolean"
    description: ""

  - name: "built_in"
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
        foreign-key-id: "permission-id"

  - name: "url"
    type: "string"
    description: ""
---