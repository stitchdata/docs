---
tap: "looker"
version: "1"
key: "permission"

name: "permissions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/permissions.json"
description: |
  The `{{ table.name }}` table contains info about the permissions listed in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all permissions"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_permissions"

attributes:
  - name: "permission"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "permission-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "parent"
    type: "string"
    description: ""
---