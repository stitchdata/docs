---
tap: "slack"
version: "1"
key: "message"

name: "messages"
doc-link: "https://api.slack.com/types/conversation"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/messages.json"
description: |
  The `{{ table.name }}` table contains the history of messages and events in conversations in your {{ integration.display_name }} workspace.

replication-method: "Key-based Incremental"

api-method:
  name: "conversations.history"
  doc-link: "https://api.slack.com/methods/conversations.history"

attributes:
  - name: "channel_id"
    type: "string"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "ts"
    type: "date-time"
    primary-key: true
    description: "The conversation timestamp."
    replication-key: true

  - name: "blocks"
    type: "array"
    description: ""
    subattributes:
      - name: "type"
        type: "string"
        description: ""

  - name: "bot_id"
    type: "string"
    description: ""

  - name: "bot_profile"
    type: "object"
    description: ""
    subattributes:
      - name: "app_id"
        type: "string"
        description: ""

      - name: "deleted"
        type: "boolean"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "team_id"
        type: "string"
        description: "The team ID."
        foreign-key-id: "team-id"
      - name: "updated"
        type: "date-time"
        description: ""

  - name: "client_msg_id"
    type: "string"
    description: ""

  - name: "display_as_bot"
    type: "boolean"
    description: ""

  - name: "file_id"
    type: "string"
    description: ""

  - name: "file_ids"
    type: "array"
    description: "The IDs of files associated with the conversation."
    subattributes:
      - name: "value"
        type: "string"
        description: "The file ID."
        foreign-key-id: "file-id"

  - name: "icons"
    type: "object"
    description: ""
    subattributes:
      - name: "emoji"
        type: "string"
        description: ""

  - name: "inviter"
    type: "string"
    description: ""

  - name: "is_delayed_message"
    type: "boolean"
    description: ""

  - name: "is_intro"
    type: "boolean"
    description: ""

  - name: "is_starred"
    type: "boolean"
    description: ""

  - name: "last_read"
    type: "date-time"
    description: ""

  - name: "latest_reply"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "old_name"
    type: "string"
    description: ""

  - name: "parent_user_id"
    type: "string"
    description: ""

  - name: "permalink"
    type: "uri"
    description: ""

  - name: "pinned_to"
    type: "array"
    description: "The channels the message is pinned to."
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "channel-id"

  - name: "purpose"
    type: "string"
    description: ""

  - name: "reactions"
    type: "array"
    description: ""
    subattributes:
      - name: "count"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "users"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: "The user-id"
            foreign-key-id: "user-id"

  - name: "reply_count"
    type: "integer"
    description: ""

  - name: "reply_users"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The user ID."
        foreign-key-id: "user-id"

  - name: "reply_users_count"
    type: "integer"
    description: ""

  - name: "source_team"
    type: "string"
    description: ""
    foreign-key-id: "team-id"

  - name: "subscribed"
    type: "boolean"
    description: ""

  - name: "subtype"
    type: "string"
    description: ""

  - name: "team"
    type: "string"
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "text"
    type: "string"
    description: ""

  - name: "thread_ts"
    type: "string"
    description: ""

  - name: "topic"
    type: "string"
    description: ""
  
  - name: "type"
    type: "string"
    description: ""

  - name: "unread_count"
    type: "integer"
    description: ""

  - name: "upload"
    type: "boolean"
    description: ""

  - name: "user"
    type: "string"
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "user_team"
    type: "string"
    description: "The user's team ID."
    foreign-key-id: "team-id"

  - name: "username"
    type: "string"
    description: ""
---