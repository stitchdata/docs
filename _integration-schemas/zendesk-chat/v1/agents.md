---
tap: "zendesk-chat"
version: "1"
key: "agent"

name: "agents"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/agents.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "departments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

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

  - name: "id"
    type: "integer"
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