---
tap: "ms-teams"
version: "1"
key: "channel-message"

name: "channel_messages"
doc-link: "https://docs.microsoft.com/en-us/graph/api/chatmessage-delta?view=graph-rest-beta&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/channel_messages.json"
description: |
  The `{{ table.name }}` table contains information about messages in a channel, without replies, in your Microsoft account.

replication-method: "Key-based Incremental"

api-method:
  name: "chatMessages: delta"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/chatmessage-delta?view=graph-rest-beta&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The message ID."
    #foreign-key-id: "message-id"

  - name: "lastModified_date_time"
    type: "date-time"
    description: "The time the message was last updated."
    replication-key: true

  - name: "attachments"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""

      - name: "content_type"
        type: "string"
        description: ""

      - name: "content_url"
        type: "string"
        description: ""

      - name: "content"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "thumbnail_url"
        type: "string"
        description: ""

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

  - name: "channel_identity"
    type: "object"
    description: ""
    subattributes:
      - name: "channel_id"
        type: "string"
        description: "The channel ID."
        foreign-key-id: "channel-id"

      - name: "teamId"
        type: "string"
        description: ""

  - name: "chat_id"
    type: "string"
    description: ""

  - name: "created_date_time"
    type: "date-time"
    description: ""

  - name: "deleted_date_time"
    type: "date-time"
    description: ""

  - name: "etag"
    type: "string"
    description: ""

  - name: "from"
    type: "object"
    description: ""
    subattributes:
      - name: "application"
        type: "string"
        description: ""

      - name: "conversation"
        type: "string"
        description: ""

      - name: "device"
        type: "string"
        description: ""

      - name: "user"
        type: "object"
        description: ""
        subattributes:
          - name: "display_name"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "user_identity_type"
            type: "string"
            description: ""
  
  - name: "importance"
    type: "string"
    description: ""

  - name: "locale"
    type: "string"
    description: ""

  - name: "mentions"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "mention_text"
        type: "string"
        description: ""

      - name: "mentioned"
        type: "object"
        description: ""
        subattributes:
          - name: "application"
            type: "string"
            description: ""

          - name: "device"
            type: "string"
            description: ""

          - name: "conversation"
            type: "string"
            description: ""

          - name: "user"
            type: "object"
            description: ""
            subattributes: &user
              - name: "id"
                type: "string"
                description: ""
                foreign-key-id: "user-id"

              - name: "display_name"
                type: "string"
                description: ""

              - name: "user_identity_type"
                type: "string"
                description: ""

  - name: "message_type"
    type: "string"
    description: ""

  - name: "policy_violation"
    type: "string"
    description: ""

  - name: "reactions"
    type: "array"
    description: ""
    subattributes:
      - name: "reaction_type"
        type: "string"
        description: ""

      - name: "created_date_time"
        type: "date-time"
        description: ""

      - name: "user"
        type: "object"
        description: ""
        subattributes:
          - name: "application"
            type: "string"
            description: ""

          - name: "device"
            type: "string"
            description: ""

          - name: "conversation"
            type: "string"
            description: ""

          - name: "user"
            type: "object"
            description: ""
            subattributes: *user

  - name: "reply_to_id"
    type: "string"
    description: ""

  - name: "subject"
    type: "string"
    description: ""

  - name: "summary"
    type: "string"
    description: ""

  - name: "web_url"
    type: "string"
    description: ""
---