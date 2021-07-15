---
tap: "zendesk-chat"
version: "1"
key: "department"

name: "departments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/departments.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "description"
    type: "string"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "id"
    type: "integer"
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