---
tap: "ms-teams"
version: "1"
key: "channel-message-reply"

name: "channel_message_replies"
doc-link: "https://docs.microsoft.com/en-us/graph/api/channel-list-messagereplies?view=graph-rest-beta&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/channel_message_replies.json"
description: |
  The `{{ table.name }}` table contains information about message replies within a channel in one of your Microsoft teams.

replication-method: "Key-based Incremental"

api-method:
  name: "List channel message replies"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/channel-list-messagereplies?view=graph-rest-beta&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The message reply ID."
    #foreign-key-id: "reply-id"

  - name: "last_modified_date_time"
    type: "date-time"
    replication-key: true
    description: "The time the reply was last modified."

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
        anchor-id: 1
        subattributes:
          - name: "display_name"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: "The user ID."
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
            anchor-id: 2
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
        anchor-id: 12
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
            anchor-id: 4
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