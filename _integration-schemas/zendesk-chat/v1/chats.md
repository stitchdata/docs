---
tap: "zendesk-chat"
version: "1"
key: "chat"

name: "chats"
doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/"
singer-schema: "https://github.com/singer-io/tap-zendesk-chat/blob/master/tap_zendesk_chat/schemas/chats.json"
description: |
  The `{{ table.name }}` table contains info about the chats within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "get Chats"
  doc-link: "https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The chat ID."
    #foreign-key-id: "chat-id"

  - name: "timestamp"
    type: "date-time"
    description: "The time the chat was created."
    replication-key: true

  - name: "agent_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The agent IDs."

  - name: "agent_names"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "comment"
    type: "string"
    description: ""

  - name: "conversions"
    type: "array"
    description: ""
    subattributes:
      - name: "attribution"
        type: "object"
        description: ""
        subattributes:
          - name: "agent_id"
            type: "integer"
            description: "The agent ID."
            foreign-key-id: "agent-id"

          - name: "agent_name"
            type: "string"
            description: ""

          - name: "chat_timestamp"
            type: "date-time"
            description: ""

          - name: "department_id"
            type: "integer"
            description: "The department ID."

          - name: "department_name"
            type: "string"
            description: ""

      - name: "goal_id"
        type: "integer"
        description: "The goal ID."
        foreign-key-id: "goal-id"

      - name: "goal_name"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "timestamp"
        type: "date-time"
        description: ""

  - name: "count"
    type: "object"
    description: ""
    subattributes:
      - name: "agent"
        type: "integer"
        description: ""

      - name: "total"
        type: "integer"
        description: ""

      - name: "visitor"
        type: "integer"
        description: ""

  - name: "department_id"
    type: "integer"
    description: "The department ID."
    foreign-key-id: "department-id"

  - name: "department_name"
    type: "string"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "end_timestamp"
    type: "date-time"
    description: ""

  - name: "history"
    type: "array"
    description: ""
    subattributes:
      - name: "channel"
        type: "string"
        description: ""

      - name: "conversion"
        type: "object"
        description: ""
        subattributes:
          - name: "attribution"
            type: "object"
            description: ""
            subattributes:
              - name: "agent_id"
                type: "integer"
                description: "The agent ID."
                foreign-key-id: "agent-id"

              - name: "agent_name"
                type: "string"
                description: ""

              - name: "chat_timestamp"
                type: "date-time"
                description: ""

              - name: "department_id"
                type: "integer"
                description: "The department ID."
                foreign-key-id: "department-id"

              - name: "department_name"
                type: "string"
                description: ""

          - name: "goal_id"
            type: "integer"
            description: "The goal ID."
            foreign-key-id: "goal-id"

          - name: "goal_name"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""

          - name: "timestamp"
            type: "date-time"
            description: ""

      - name: "department_id"
        type: "integer, string"
        description: "The department ID"
        foreign-key-id: "department-id"

      - name: "department_name"
        type: "string"
        description: ""

      - name: "msg"
        type: "string"
        description: ""

      - name: "msg_id"
        type: "integer, string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "new_rating"
        type: "string"
        description: ""

      - name: "new_tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "nick"
        type: "string"
        description: ""

      - name: "options"
        type: "string"
        description: ""

      - name: "prev_department_id"
        type: "integer, string"
        description: "The previous department ID."
        foreign-key-id: "department-id"

      - name: "rating"
        type: "string"
        description: ""

      - name: "skills_name"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "timestamp"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "missed"
    type: "boolean"
    description: ""

  - name: "rating"
    type: "string"
    description: ""

  - name: "referrer_search_engine"
    type: "string"
    description: ""

  - name: "referrer_search_terms"
    type: "string"
    description: ""

  - name: "response_time"
    type: "object"
    description: ""
    subattributes:
      - name: "avg"
        type: "integer, number"
        description: ""

      - name: "first"
        type: "integer"
        description: ""

      - name: "max"
        type: "integer"
        description: ""

  - name: "session"
    type: "object"
    description: ""

  - name: "started_by"
    type: "string"
    description: ""

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "triggered"
    type: "boolean"
    description: ""

  - name: "triggered_response"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "unread"
    type: "boolean, integer"
    description: ""

  - name: "visitor"
    type: "object"
    description: ""
    subattributes:
      - name: "email"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "notes"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

  - name: "webpath"
    type: "array"
    description: ""
    subattributes:
      - name: "from"
        type: "string"
        description: ""

      - name: "timestamp"
        type: "date-time"
        description: ""

      - name: "title"
        type: "string"
        description: ""

      - name: "to"
        type: "string"
        description: ""

  - name: "zendesk_ticket_id"
    type: "integer"
    description: ""
---