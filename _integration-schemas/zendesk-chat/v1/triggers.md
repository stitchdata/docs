---
tap: "zendesk-chat"
version: "1"
key: "trigger"

name: "triggers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/triggers.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
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

  - name: "id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---