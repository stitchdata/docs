---
tap: "zendesk-chat"
version: "1"
key: "goal"

name: "goals"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/goals.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "attribution_model"
    type: "string"
    description: ""

  - name: "attribution_period"
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

  - name: "settings"
    type: "object"
    description: ""
    subattributes:
      - name: "conditions"
        type: "array"
        description: ""
        subattributes:
          - name: "operator"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""
---