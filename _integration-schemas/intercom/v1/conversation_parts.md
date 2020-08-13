---
tap: "intercom"
version: "1"

name: "conversation_parts"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#conversation-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/conversation_parts.json"
description: |
  The `{{ table.name }}` table lists parts of a conversation from the `conversations`table in your {{ integration.display_name }} account. The only conversation parts that will replicate in full will be the ones whose parent conversation in the `conversations` table have updated.

replication-method: "Full Table"

api-method:
    name: "retrieveAConversation"
    doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#retrieve-a-conversation"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation part ID."
    foreign-key-id: "part-id"

  - name: "assigned_to"
    type: "string"
    description: "The admin ID that the conversation part is assigned to."
    foreign-key-id: "admin-id"
  - name: "attachments"
    type: "null"
    description: ""
  - name: "author"
    type: "object"
    description: "A list of conversation authors."
    subattributes:
      - name: "id"
        type: "string"
        description: "The author ID. This could either be the user ID or admin ID."
      - name: "type"
        type: "string"
        description: ""
  - name: "body"
    type: "string"
    description: ""
  - name: "conversation_created_at"
    type: "date-time"
    description: ""

  - name: "conversation_id"
    type: "string"
    description: "The conversation ID."
    foreign-key-id: "conversation-id"

  - name: "conversation_total_parts"
    type: "integer"
    description: ""
  - name: "conversation_updated_at"
    type: "date-time"
    description: ""
  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "external_id"
    type: "string"
    description: ""
  
  - name: "notified_at"
    type: "date-time"
    description: ""
  - name: "part_type"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "updated_at"
    type: "date-time"
    description: ""
---
