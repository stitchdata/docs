---
tap: "zendesk-chat"
version: "1"
key: "goal"

name: "goals"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/goals/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/goals.json"
description: |
  The `{{ table.name }}` table contains info about URL-based goals set within your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "get Goals"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/goals/"

attributes:
  - name: "id"
    type: "integer"
    description: "The goal ID."
    foreign-key-id: "goal-id"

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