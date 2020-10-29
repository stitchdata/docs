---
tap: "ms-teams"
version: "1"
key: "conversation-post"

name: "conversation_posts"
doc-link: "https://docs.microsoft.com/en-us/graph/api/conversationthread-list-posts?view=graph-rest-beta&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/conversation_posts.json"
description: |
  The `{{ table.name }}` table contains information about the posts within a conversation thread in your Microsoft account.

replication-method: "Key-based Incremental"

api-method:
  name: "List posts"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/conversationthread-list-posts?view=graph-rest-1.0&tabs=http"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The post ID."
    #foreign-key-id: "post-id"
  
  - name: "last_modified_date_time"
    type: "date-time"
    description: "The time the post was last modified."
    replication-key: true

  - name: "body"
    type: "object"
    description: ""
    subattributes:
      - name: "content"
        type: "string"
        description: ""

      - name: "content_type"
        type: "string"
        description: ""

  - name: "categories"
    type: "object"
    description: ""

  - name: "change_key"
    type: "string"
    description: ""

  - name: "conversation_id"
    type: "string"
    description: "The conversation ID."
    foreign-key-id: "conversation-id"

  - name: "created_date_time"
    type: "date-time"
    description: ""

  - name: "from"
    type: "object"
    description: ""
    subattributes:
      - name: "emailAddress"
        type: "object"
        description: ""
        subattributes:
          - name: "address"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

  - name: "has_attachments"
    type: "boolean"
    description: ""
  
  - name: "received_date_time"
    type: "date-time"
    description: ""

  - name: "sender"
    type: "object"
    description: ""
    subattributes:
      - name: "emailAddress"
        type: "object"
        description: ""
        subattributes:
          - name: "address"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

  - name: "thread_id"
    type: "string"
    description: "The ID of the conversation thread associated with the post."
    foreign-key-id: "thread-id"
---