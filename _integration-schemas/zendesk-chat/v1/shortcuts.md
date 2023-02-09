---
tap: "zendesk-chat"
version: "1"
key: "shortcut"

name: "shortcuts"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/shortcuts/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/shortcuts.json"
description: |
  The `{{ table.name }}` table contains info about shortcuts within yoru {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "get Shortcuts"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/shortcuts/"

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the shortcut."
    #foreign-key-id: "shortcut-id"

  - name: "departments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "id"
    type: "string"
    description: "The department ID."
    foreign-key-id: "department-id"

  - name: "message"
    type: "string"
    description: ""

  - name: "options"
    type: "string"
    description: ""

  - name: "scope"
    type: "string"
    description: ""

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
---