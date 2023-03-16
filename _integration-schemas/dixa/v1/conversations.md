---
tap: "dixa"
version: "1"
key: ""

name: "conversations"
doc-link: "https://docs.dixa.io/openapi/dixa-api/tag/Conversations/" 
singer-schema: "https://github.com/singer-io/tap-dixa/blob/main/tap_dixa/schemas/conversations.json"
description: |
  The `{{ table.name }}` table lists information about conversations in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get conversations"
  doc-link: "https://docs.dixa.io/openapi/dixa-api/tag/Conversations/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The conversation ID."
    foreign-key-id: "conversation-id"

  - name: "updated_at"
    type: "integer"
    replication-key: true
    description: "The date the conversation was last updated. Measured in seconds since the Unix epoch."  

  - name: "anonymized_at"
    type: "integer"
    description: ""

  - name: "assigned_at"
    type: "integer"
    description: ""

  - name: "assignee_email"
    type: "string"
    description: ""

  - name: "assignee_id"
    type: "string"
    description: ""

  - name: "assignee_name"
    type: "string"
    description: ""

  - name: "assignee_phone_number"
    type: "string"
    description: ""

  - name: "closed_at"
    type: "integer"
    description: ""

  - name: "conversation_wrapup_notes"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "created_at"
    type: "integer"
    description: ""

  - name: "custom_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
        subattributes:
          - name: "archived"
            type: "boolean"
            description: ""
            
          - name: "attribute_id"
            type: "string"
            description: ""
            
          - name: "data_type"
            type: "string"
            description: ""
            
          - name: "identifier"
            type: "string"
            description: ""
            
          - name: "value"
            type: "string"
            description: ""

  - name: "direction"
    type: "string"
    description: ""

  - name: "dixa_email_integration_id"
    type: "string"
    description: ""

  - name: "dixa_email_integration_sender_name"
    type: "string"
    description: ""

  - name: "facebook_page_id"
    type: "string"
    description: ""

  - name: "facebook_page_name"
    type: "string"
    description: ""

  - name: "forwarding_email"
    type: "string"
    description: ""

  - name: "from_provisioned_phone_number_id"
    type: "string"
    description: ""

  - name: "from_provisioned_phone_number_name"
    type: "string"
    description: ""

  - name: "handling_duration"
    type: "integer"
    description: ""

  - name: "initial_channel"
    type: "string"
    description: ""

  - name: "last_message_created_at"
    type: "integer"
    description: ""

  - name: "originating_country"
    type: "string"
    description: ""

  - name: "queue_id"
    type: "string"
    description: ""

  - name: "queue_name"
    type: "string"
    description: ""

  - name: "queued_at"
    type: "integer"
    description: ""

  - name: "rating_message"
    type: "string"
    description: ""

  - name: "rating_score"
    type: "integer"
    description: ""

  - name: "ratings"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
        subattributes:
          - name: "rating_language"
            type: "string"
            description: ""
          - name: "rating_modified_timestamp"
            type: "integer"
            description: ""
          - name: "rating_scheduled_timestamp"
            type: "integer"
            description: ""
          - name: "rating_created_timestamp"
            type: "integer"
            description: ""
          - name: "rating_offered_timestamp"
            type: "integer"
            description: ""
          - name: "rating_status"
            type: "string"
            description: ""
          - name: "rating_unscheduled_timestamp"
            type: "string"
            description: ""
          - name: "rating_score"
            type: "integer"
            description: ""
          - name: "rating_rated_timestamp"
            type: "integer"
            description: ""
          - name: "rating_scheduled_for_timestamp"
            type: "integer"
            description: ""
          - name: "rating_cancelled_timestamp"
            type: "string"
            description: ""
          - name: "rating_message"
            type: "string"
            description: ""
          - name: "rating_type"
            type: "string"
            description: ""


  - name: "requester_email"
    type: "string"
    description: ""

  - name: "requester_id"
    type: "string"
    description: ""

  - name: "requester_name"
    type: "string"
    description: ""

  - name: "requester_phone_number"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subject"
    type: "string"
    description: ""

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "tags_info"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
          - name: "name"
            type: "string"
            description: ""
          - name: "is_deactivated"
            type: "boolean"
            description: ""


  - name: "to_provisioned_phone_number_id"
    type: "string"
    description: ""

  - name: "to_provisioned_phone_number_name"
    type: "string"
    description: ""

  - name: "total_duration"
    type: "integer"
    description: ""

  - name: "transfer_time"
    type: "integer"
    description: ""

  - name: "transferee_name"
    type: "string"
    description: ""

  - name: "transferee_number"
    type: "string"
    description: ""

  - name: "updated_at_datestring"
    type: "integer"
    description: ""  

  - name: "widget_id"
    type: "string"
    description: ""

  - name: "widget_name"
    type: "string"
    description: ""
---