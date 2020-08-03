---
tap: "harvest"
version: "2"

name: "user_roles"
doc-link: https://help.getharvest.com/api-v2/users-api/users/users/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/user_roles.json
description: |
  The `{{ table.name }}` table contains a list of user ID and role ID pairs, enabling you to see the roles users are associated with.

  **Note**: This table is updated based on new and updated `users`. This means that when a user is updated, this table will also be updated.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"
  ## This is replicated as part of the parent table, users

api-method:
  name: 
  doc-link:

attributes:
  - name: "user_id"
    type: "integer"
    description: "The user ID."
    primary-key: true
    foreign-key-id: "user-id"

  - name: "role_id"
    type: "integer"
    description: "The role ID."
    primary-key: true
    foreign-key-id: "role-id"
---