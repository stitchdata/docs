---
tap: "zendesk-chat"
version: "1"
key: "department"

name: "departments"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/departments/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/departments.json"
description: |
  The `{{ table.name }}` table contains info about departments within your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "get Departments"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/departments/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The department ID."
    foreign-key-id: "department-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "members"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "settings"
    type: "object"
    description: ""
---