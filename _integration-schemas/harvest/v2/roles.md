---
tap: "harvest"
version: "2.0"

name: "roles"
doc-link: https://help.getharvest.com/api-v2/roles-api/roles/roles/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/roles.json
description: |
  The `{{ table.name }}` table contains info about the roles in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: List all roles
  doc-link: https://help.getharvest.com/api-v2/roles-api/roles/roles#list-all-roles

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The role ID."
    foreign-key-id: "role-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the role was last updated."

  - name: "name"
    type: "string"
    description: "The name of the role."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the role was created."
---