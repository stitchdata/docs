---
tap: "harvest"
version: "2.0"

name: "user_roles"
doc-link: https://help.getharvest.com/api-v2/roles-api/roles/roles/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/time_entry_external_reference.json
description: |
  The `{{ table.name }}` table contains a list of user ID and role ID pairs, enabling you to see the roles users are associated with.

replication-method: "Key-based Incremental"

api-method:
  name: 
  doc-link:

attributes:
  - name: "user_id"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "role_id"
    type: "integer"
    description: "The role ID."
    foreign-key-id: "role-id"
---