---
tap: "zendesk"
version: "1.0"

name: "groups"
doc-link: https://developer.zendesk.com/rest_api/docs/core/groups
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/groups.json
description: |
  The `groups` table contains info about the groups in your Zendesk account. 

  **Note**: Retrieving group data requires Zendesk Admin or Agent permissions.

replication-method: "Key-based Incremental"

api-method:
  name: List Groups
  doc-link: https://developer.zendesk.com/rest_api/docs/core/groups#list-groups

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group ID."

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