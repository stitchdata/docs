---
tap: "zendesk-chat"
version: "1"
key: "trigger"

name: "triggers"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/triggers/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/triggers.json"
description: |
  The `{{ table.name }}` table contains info about triggers within your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "get Triggers"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/triggers/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The trigger ID."
    #foreign-key-id: "trigger-id"

  - name: "definition"
    type: "object"
    description: ""
    subattributes:
      - name: "actions"
        type: "string"
        description: ""

      - name: "condition"
        type: "string"
        description: ""

      - name: "event"
        type: "string"
        description: ""

      - name: "version"
        type: "integer"
        description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---