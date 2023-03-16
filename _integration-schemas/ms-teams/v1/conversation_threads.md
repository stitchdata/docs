---
tap: "ms-teams"
version: "1"
key: "conversation-thread"

name: "conversation_threads"
doc-link: "https://docs.microsoft.com/en-us/graph/api/conversation-list-threads?view=graph-rest-beta&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/conversation_threads.json"
description: |
  The `{{ table.name }}` table contains information about threads in a group conversation in your Microsoft account.

replication-method: "Key-based Incremental"

api-method:
  name: "List threads"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-threads?view=graph-rest-1.0&tabs=http"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The thread ID."
    foreign-key-id: "thread-id"

  - name: "last_delivered_date_time"
    type: "date-time"
    replication-key: true
    description: "The time the last message was delivered in the thread."

  - name: "conversation_id"
    type: "string"
    description: "The ID of the conversation associated with the thread."
    foreign-key-id: "conversation-id"

  - name: "group_id"
    type: "string"
    description: "The ID of the group associated with the thread."
    foreign-key-id: "group-id"

  - name: "has_attachments"
    type: "boolean"
    description: ""
  
  - name: "is_locked"
    type: "boolean"
    description: ""
  
  - name: "preview"
    type: "string"
    description: ""

  - name: "topic"
    type: "string"
    description: ""

  - name: "unique_senders"
    type: "string"
    description: ""
---