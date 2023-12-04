---
tap: "ms-teams"
version: "1"
key: "conversation"

name: "conversations"
doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-conversations?view=graph-rest-beta&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/conversations.json"
description: |
  The `{{ table.name }}` table contains information about conversations within a group in your Microsoft account.

replication-method: "Key-based Incremental"

api-method:
  name: "List conversations"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-conversations?view=graph-rest-1.0&tabs=http"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation ID."
    #foreign-key-id: "conversation-id"

  - name: "last_delivered_date_time"
    type: "date-time"
    replication-key: true
    description: "The time a message was last delivered in a conversation."
      
  - name: "group_id"
    type: "string"
    description: "The ID of the group associated with the conversation."
    foreign-key-id: "group-id"

  - name: "has_attachments"
    type: "boolean"
    description: ""
 
  - name: "preview"
    type: "string"
    description: ""

  - name: "topic"
    type: "string"
    description: ""

  - name: "unique_senders"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
---