---
tap: "ujet"
version: "1"
key: "agent"

name: "agents"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/agents.json"
description: |
  The `{{ table.name }}` table contains info about agents.

replication-method: "Key-based Incremental"

api-method:
  name: "Get agents"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "agent-id"

  - name: "status_updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "agent_number"
    type: "string"
    description: ""

  - name: "avatar_url"
    type: "string"
    description: ""

  - name: "call_count"
    type: "integer"
    description: ""

  - name: "channels"
    type: "array"
    description: ""
    subattributes:
      - name: "deleted"
        type: "boolean"
        description: ""

      - name: "hidden"
        type: "boolean"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "menu_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "output_msg"
        type: "string"
        description: ""

      - name: "parent_id"
        type: "integer"
        description: ""

      - name: "position"
        type: "integer"
        description: ""

  - name: "chat_count"
    type: "integer"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "crm_authenticated"
    type: "boolean"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "last_login_time"
    type: "date-time"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "location"
    type: "string"
    description: ""

  - name: "middle_name"
    type: "string"
    description: ""

  - name: "online"
    type: "boolean"
    description: ""

  - name: "roles"
    type: "array"
    description: ""
    subattriubtes:
      - name: "value"
        type: "string"
        description: ""

  - name: "status"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "wfm_id"
        type: "integer"
        description: ""

  - name: "teams"
    type: "array"
    description: ""
    subattributes:
      - name: "agents_count"
        type: "integer"
        description: ""

      - name: "deleted"
        type: "boolean"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "team-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "parent_id"
        type: "integer"
        description: ""

      - name: "position"
        type: "integer"
        description: ""

  - name: "wrap_up"
    type: "boolean"
    description: ""
---