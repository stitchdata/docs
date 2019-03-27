---
tap: "freshdesk"
# version:

name: "roles"
doc-link: https://developers.freshdesk.com/api/#roles
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/roles.json
description: |
  The `{{ table.name }}` table contains info about the various roles that can be assigned to team members in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
  name: "listAllRoles"
  doc-link: https://developers.freshdesk.com/api/#list_all_roles

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The role ID."
    foreign-key-id: "role-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the role was last updated."

  - name: "description"
    type: "string"
    description: "The description of the role."

  - name: "name"
    type: "string"
    description: "The name of the role."

  - name: "default"
    type: "boolean"
    description: "Indicates if the role is the default."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the role was first created."
---