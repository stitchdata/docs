---
tap: "zendesk-chat"
version: "1"
key: "agent"

name: "agents"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/agents/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/agents.json"
description: |
  The `{{ table.name }}` table contains info about agents within your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "get Agents"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/agents/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The agent ID."
    foreign-key-id: "agent-id"

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "departments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: "The department ID."
        foreign-key-id: "department-id"

  - name: "display_name"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "enabled_departments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "last_login"
    type: "date-time"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "login_count"
    type: "integer"
    description: ""

  - name: "role_id"
    type: "integer"
    description: ""

  - name: "roles"
    type: "object"
    description: ""
    subattributes:
      - name: "administrator"
        type: "boolean"
        description: ""

      - name: "owner"
        type: "boolean"
        description: ""

  - name: "scope"
    type: "string"
    description: ""

  - name: "skills"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
---