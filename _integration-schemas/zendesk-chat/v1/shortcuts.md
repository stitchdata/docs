---
tap: "zendesk-chat"
version: "1"
key: "shortcut"

name: "shortcuts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/shortcuts.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "departments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "name"
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