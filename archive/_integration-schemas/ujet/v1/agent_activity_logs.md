---
tap: "ujet"
version: "1"
key: "agent-activity-log"

name: "agent_activity_logs"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/agent_activity_logs.json"
description: |
  The `{{ table.name }}` table contains info about agent activity logs.

replication-method: "Key-based Incremental"

api-method:
  name: "Get agent activity logs"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "agent-activity-log-id"

  - name: "started_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "activity"
    type: "string"
    description: ""

  - name: "agent_id"
    type: "integer"
    description: ""
    foreign-key-id: "agent-id"

  - name: "call_id"
    type: "integer"
    description: ""
    foreign-key-id: "call-id"

  - name: "chat_id"
    type: "integer"
    description: ""
    foreign-key-id: "call-id"

  - name: "duration"
    type: "integer"
    description: ""

  - name: "ended_at"
    type: "date-time"
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

  - name: "whodunnit"
    type: "object"
    description: ""
    subattributes:
      - name: "agent_number"
        type: "string"
        description: ""

      - name: "avatar_url"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""
---