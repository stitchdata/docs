---
tap: "looker"
version: "1"
key: "role-group"

name: "role_groups"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/role_groups.json"
description: |
  The `{{ table.name }}` table contains info about the role groups in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get role groups"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_role_groups"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "role-group-id"

  - name: "can_add_to_content_metadata"
    type: "boolean"
    description: ""

  - name: "contains_current_user"
    type: "boolean"
    description: ""

  - name: "external_group_id"
    type: "string"
    description: ""

  - name: "externally_managed"
    type: "boolean"
    description: ""

  - name: "include_by_default"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "role_id"
    type: "string"
    description: ""
    foreign-key-id: "role-id"

  - name: "user_count"
    type: "integer"
    description: ""
---