---
tap: "zendesk"
version: "1"

name: "groups"
doc-link: https://developer.zendesk.com/rest_api/docs/support/groups
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/groups.json
description: |
  The `{{ table.name }}` table contains info about the groups in your {{ integration.display_name }} account. 

  **Note**: Retrieving group data requires {{ integration.display_name }} Admin or Agent permissions.

replication-method: "Key-based Incremental"

api-method:
  name: List groups
  doc-link: https://developer.zendesk.com/rest_api/docs/support/groups#list-groups

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the group was last updated."

  - name: "name"
    type: "string"
    description: "The name of the group."

  - name: "created_at"
    type: "date-time"
    description: "The time the group was created."

  - name: "deleted"
    type: "boolean"
    description: "If `true`, the group has been deleted."

  - name: "url"
    type: "string"
    description: "The API URL of the group."
---