---
tap: "ujet"
version: "1"
key: "call"

name: "calls"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/calls.json"
description: |
  The `{{ table.name }}` table contains info about calls.

replication-method: "Key-based Incremental"

api-method:
  name: "Get calls"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "call-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "agent_info"
    type: "object"
    description: ""
    subattributes:
      - name: "agent_number"
        type: "integer"
        description: ""

      - name: "avatar_url"
        type: "uri"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "agent-id"

      - name: "last_name"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "answer_type"
    type: "string"
    description: ""

  - name: "assigned_at"
    type: "date-time"
    description: ""

  - name: "call_duration"
    type: "integer"
    description: ""

  - name: "call_type"
    type: "string"
    description: ""

  - name: "connected_at"
    type: "date-time"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deflection"
    type: "string"
    description: ""

  - name: "deflection_details"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "call_id"
        type: "integer"
        description: ""

      - name: "transfer_id"
        type: "integer"
        description: ""

      - name: "from_menu_path"
        type: "object"
        description: ""
        subattributes: &menu-path
          - name: "items_count"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "materialized_path"
            type: "string"
            description: ""

  - name: "disconnected_by"
    type: "string"
    description: ""

  - name: "end_user"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "identifier"
        type: "string"
        description: ""

      - name: "out_contact_id"
        type: "string"
        description: ""

  - name: "ends_at"
    type: "date-time"
    description: ""

  - name: "fail_details"
    type: "string"
    description: ""

  - name: "fail_reason"
    type: "string"
    description: ""

  - name: "has_feedback"
    type: "boolean"
    description: ""

  - name: "hold_duration"
    type: "integer"
    description: ""

  - name: "lang"
    type: "string"
    description: ""

  - name: "menu_path"
    type: "object"
    description: ""
    subattributes: *menu-path

  - name: "offer_events"
    type: "array"
    description: ""
    subattributes:
      - name: "casting_time"
        type: "date-time"
        description: ""

      - name: "group"
        type: "string"
        description: ""

  - name: "offer_type"
    type: "string"
    description: ""

  - name: "out_ticket_id"
    type: "string"
    description: ""

  - name: "out_ticket_url"
    type: "uri"
    description: ""

  - name: "outbound_number"
    type: "string"
    description: ""

  - name: "participants"
    type: "array"
    description: ""
    subattributes:
      - name: "fail_reason"
        type: "string"
        description: ""

      - name: "ended_at"
        type: "date-time"
        description: ""

      - name: "hold_duration"
        type: "integer"
        description: ""

      - name: "connected_at"
        type: "date-time"
        description: ""

      - name: "user_id"
        type: "integer"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "call_duration"
        type: "integer"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "end_user_id"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "call_id"
        type: "integer"
        description: ""
        foreign-key-id: "call-id"

  - name: "photos"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "photo_type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "queued_at"
    type: "date-time"
    description: ""

  - name: "rating"
    type: "string"
    description: ""

  - name: "recording_url"
    type: "uri"
    description: ""

  - name: "scheduled_at"
    type: "date-time"
    description: ""

  - name: "selected_menu"
    type: "object"
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

  - name: "status"
    type: "string"
    description: ""

  - name: "support_number"
    type: "string"
    description: ""

  - name: "transfers"
    type: "array"
    description: ""
    subattributes:
      - name: "deflection"
        type: "string"
        description: ""

      - name: "from_agent"
        type: "object"
        description: ""
        subattributes: &agent
          - name: "first_name"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "agent_number"
            type: "integer"
            description: ""

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "agent-id"

          - name: "last_name"
            type: "string"
            description: ""

          - name: "avatar_url"
            type: "string"
            description: ""

      - name: "to_queue_priority_level"
        type: "string"
        description: ""

      - name: "fail_reason"
        type: "string"
        description: ""

      - name: "from_queue_priority_level"
        type: "todo"
        description: ""

      - name: "connected_at"
        type: "date-time"
        description: ""

      - name: "to_agent"
        type: "object"
        description: ""
        subattributes: *agent

      - name: "id"
        type: "integer"
        description: ""

      - name: "wait_duration"
        type: "integer"
        description: ""

      - name: "answer_type_path"
        type: "string"
        description: ""

      - name: "call_duration"
        type: "integer"
        description: ""

      - name: "from_menu_path"
        type: "object"
        description: ""
        subattriubtes: *menu-path

      - name: "status"
        type: "string"
        description: ""

      - name: "assigned_at"
        type: "date-time"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "to_menu_path"
        type: "string"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: ""

  - name: "verified"
    type: "boolean"
    description: ""

  - name: "videos"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "voicemail_reason"
    type: "string"
    description: ""

  - name: "voip_provider"
    type: "string"
    description: ""

  - name: "wait_duration"
    type: "integer"
    description: ""
---