---
tap: "kustomer"
version: "1"
key: "conversations"

name: "conversations"
doc-link: "https://dev.kustomer.com/v1/conversations/"
singer-schema: "https://github.com/singer-io/tap-kustomer/blob/master/tap_kustomer/schemas/conversations.json"
description: |
  The `{{ table.name }}` table contains information about conversations in the {{ integration.display_name }} app.

replication-method: "Key-based Incremental"

api-method:
  name: "getConversations"
  doc-link: "https://dev.kustomer.com/v1/conversations/get-conversations"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation ID."
    #foreign-key-id: "conversation-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: ""

  - name: "assigned_teams"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "assigned_users"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "channels"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "created_at"
    type: "string"
    description: ""
  - name: "created_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "custom"
    type: "object"
    description: ""
    subattributes:
      - name: "auto_response_at"
        type: "string"
        description: ""
      - name: "brand_str"
        type: "string"
        description: ""
      - name: "business_area_str"
        type: "string"
        description: ""
      - name: "case_id_str"
        type: "string"
        description: ""
      - name: "close_out_tree"
        type: "string"
        description: ""
      - name: "contact_reason_tree"
        type: "string"
        description: ""
      - name: "desk_ticket_url"
        type: "string"
        description: ""
      - name: "issue_report_tree"
        type: "string"
        description: ""
      - name: "new_primary_menu_str"
        type: "string"
        description: ""
      - name: "order_number_id"
        type: "string"
        description: ""
      - name: "refund_status_str"
        type: "string"
        description: ""
      - name: "return_requested_str"
        type: "string"
        description: ""
      - name: "return_str"
        type: "string"
        description: ""
      - name: "rma_id_str"
        type: "string"
        description: ""
      - name: "serial_number_str"
        type: "string"
        description: ""
      - name: "shopify_order_str"
        type: "string"
        description: ""
      - name: "yale_call_reason_tree"
        type: "string"
        description: ""
      - name: "yale_connectivity_str"
        type: "string"
        description: ""
      - name: "yale_finish_str"
        type: "string"
        description: ""
      - name: "yale_model_str"
        type: "string"
        description: ""
      - name: "yale_notes_txt"
        type: "string"
        description: ""
      - name: "yale_resolution_str"
        type: "string"
        description: ""
      - name: "yale_serial_number_str"
        type: "string"
        description: ""
  - name: "customer"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "direction"
    type: "string"
    description: ""
  - name: "done_count"
    type: "integer"
    description: ""
  - name: "ended"
    type: "boolean"
    description: ""
  - name: "ended_at"
    type: "string"
    description: ""
  - name: "ended_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "ended_by_type"
    type: "string"
    description: ""
  - name: "ended_reason"
    type: "string"
    description: ""
  - name: "external_id"
    type: "string"
    description: ""
  - name: "first_done"
    type: "object"
    description: ""
    subattributes:
      - name: "assigned_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "assigned_users"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "created_by"
        type: "string"
        description: ""
      - name: "created_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "last_message_direction"
        type: "string"
        description: ""
      - name: "last_message_direction_type"
        type: "string"
        description: ""
      - name: "message_count"
        type: "integer"
        description: ""
      - name: "message_count_by_channel"
        type: "object"
        description: ""
        subattributes:
          - name: "email"
            type: "integer"
            description: ""
          - name: "sms"
            type: "integer"
            description: ""
          - name: "voice"
            type: "integer"
            description: ""
      - name: "note_count"
        type: "integer"
        description: ""
      - name: "outbound_message_count"
        type: "integer"
        description: ""
      - name: "outbound_message_count_by_channel"
        type: "object"
        description: ""
        subattributes:
          - name: "email"
            type: "integer"
            description: ""
          - name: "sms"
            type: "integer"
            description: ""
          - name: "voice"
            type: "integer"
            description: ""
      - name: "time"
        type: "integer"
        description: ""
  - name: "first_message_in"
    type: "object"
    description: ""
    subattributes:
      - name: "channel"
        type: "string"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "direction_type"
        type: "string"
        description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
  - name: "first_message_out"
    type: "object"
    description: ""
    subattributes:
      - name: "channel"
        type: "string"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "created_by"
        type: "string"
        description: ""
      - name: "created_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "direction_type"
        type: "string"
        description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
  - name: "first_response"
    type: "object"
    description: ""
    subattributes:
      - name: "assigned_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "assigned_users"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "created_by"
        type: "string"
        description: ""
      - name: "created_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "response_time"
        type: "integer"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
      - name: "time"
        type: "integer"
        description: ""
  - name: "first_response_since_last_done"
    type: "object"
    description: ""
    subattributes:
      - name: "assigned_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "assigned_users"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "created_by"
        type: "string"
        description: ""
      - name: "created_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "response_time"
        type: "integer"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
      - name: "time"
        type: "integer"
        description: ""
  
  - name: "imported_at"
    type: "string"
    description: ""
  - name: "last_activity_at"
    type: "string"
    description: ""
  - name: "last_done"
    type: "object"
    description: ""
    subattributes:
      - name: "assigned_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "assigned_users"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "created_by"
        type: "string"
        description: ""
      - name: "created_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "last_message_direction"
        type: "string"
        description: ""
      - name: "last_message_direction_type"
        type: "string"
        description: ""
      - name: "message_count"
        type: "integer"
        description: ""
      - name: "message_count_by_channel"
        type: "object"
        description: ""
        subattributes:
          - name: "email"
            type: "integer"
            description: ""
          - name: "sms"
            type: "integer"
            description: ""
          - name: "voice"
            type: "integer"
            description: ""
      - name: "note_count"
        type: "integer"
        description: ""
      - name: "outbound_message_count"
        type: "integer"
        description: ""
      - name: "outbound_message_count_by_channel"
        type: "object"
        description: ""
        subattributes:
          - name: "email"
            type: "integer"
            description: ""
          - name: "sms"
            type: "integer"
            description: ""
          - name: "voice"
            type: "integer"
            description: ""
      - name: "time"
        type: "integer"
        description: ""
  - name: "last_message_at"
    type: "string"
    description: ""
  - name: "last_message_direction"
    type: "string"
    description: ""
  - name: "last_message_in"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
  - name: "last_message_out"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
  - name: "last_message_unresponded_to"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
  - name: "last_message_unresponded_to_since_last_done"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "sent_at"
        type: "string"
        description: ""
  - name: "last_received_at"
    type: "string"
    description: ""
  - name: "last_response"
    type: "object"
    description: ""
    subattributes:
      - name: "assigned_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "assigned_users"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "created_at"
        type: "string"
        description: ""
      - name: "created_by"
        type: "string"
        description: ""
      - name: "created_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "time"
        type: "integer"
        description: ""
  - name: "links"
    type: "object"
    description: ""
    subattributes:
      - name: "self"
        type: "string"
        description: ""
  - name: "merged_target"
    type: "boolean"
    description: ""
  - name: "message_count"
    type: "integer"
    description: ""
  - name: "modified_at"
    type: "string"
    description: ""
  - name: "modified_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "note_count"
    type: "integer"
    description: ""
  - name: "org"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "outbound_message_count"
    type: "integer"
    description: ""
  - name: "preview"
    type: "string"
    description: ""
  - name: "priority"
    type: "integer"
    description: ""
  - name: "queue"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "reopen_count"
    type: "integer"
    description: ""
  - name: "rev"
    type: "integer"
    description: ""
  - name: "role_group_versions"
    type: "string"
    description: ""
  - name: "satisfaction"
    type: "string"
    description: ""
  - name: "satisfaction_level"
    type: "object"
    description: ""
    subattributes:
      - name: "sent_by_teams"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
  - name: "sla"
    type: "object"
    description: ""
    subattributes:
      - name: "breach"
        type: "object"
        description: ""
        subattributes:
          - name: "at"
            type: "string"
            description: ""
          - name: "metric"
            type: "string"
            description: ""
      - name: "breached"
        type: "boolean"
        description: ""
      - name: "matched_at"
        type: "string"
        description: ""
      - name: "metrics"
        type: "object"
        description: ""
        subattributes:
          - name: "first_response"
            type: "object"
            description: ""
            subattributes:
              - name: "breach_at"
                type: "string"
                description: ""
              - name: "satisfied_at"
                type: "string"
                description: ""
          - name: "longest_unresponded_message"
            type: "object"
            description: ""
            subattributes:
              - name: "breach_at"
                type: "string"
                description: ""
              - name: "satisfied_at"
                type: "string"
                description: ""
      - name: "status"
        type: "string"
        description: ""
      - name: "summary"
        type: "object"
        description: ""
        subattributes:
          - name: "first_breach_at"
            type: "string"
            description: ""
          - name: "satisfied_at"
            type: "string"
            description: ""
      - name: "version"
        type: "integer"
        description: ""
  - name: "sla_data"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "sla_version"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "snooze"
    type: "object"
    description: ""
    subattributes:
      - name: "status"
        type: "string"
        description: ""
      - name: "status_at"
        type: "string"
        description: ""
      - name: "time"
        type: "string"
        description: ""
  - name: "snooze_count"
    type: "integer"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "suggested_shortcuts"
    type: "string"
    description: ""
  - name: "suggested_tags"
    type: "string"
    description: ""
  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "total_done"
    type: "object"
    description: ""
    subattributes:
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "time"
        type: "integer"
        description: ""
  - name: "total_open"
    type: "object"
    description: ""
    subattributes:
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "business_time_since_last_done"
        type: "integer"
        description: ""
      - name: "time"
        type: "integer"
        description: ""
      - name: "time_since_last_done"
        type: "integer"
        description: ""
  - name: "total_snooze"
    type: "object"
    description: ""
    subattributes:
      - name: "business_time"
        type: "integer"
        description: ""
      - name: "time"
        type: "integer"
        description: ""
  - name: "type"
    type: "string"
    description: ""
---