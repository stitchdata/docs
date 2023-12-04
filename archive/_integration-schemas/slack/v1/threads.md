---
tap: "slack"
version: "1"
key: "thread"

name: "threads"
doc-link: "https://api.slack.com/docs/conversations-api"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/threads.json"
description: |
  The `{{ table.name }}` table contains info about conversation threads in your {{ integration.display_name }} team. 

  **Note**: While this table uses Full Table, it's not truly replicated in full during each replication job. Each time a message in a thread is updated, the entire thread and all the messages it contains will be replicated in full. This means that while only updated threads are replicated, they are replicated in full whenever they're updated.

replication-method: "Full Table"

api-method:
  name: "conversations.replies"
  doc-link: "https://api.slack.com/methods/conversations.replies"

attributes:
  - name: "channel_id"
    type: "string"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "thread_ts"
    type: "string"
    primary-key: true
    description: "The conversation thread timestamp."

  - name: "ts"
    type: "date-time"
    description: "The conversation timestamp."
      
  - name: "blocks"
    type: "array"
    description: ""
    subattributes:
      - name: "type"
        type: "string"
        description: ""
  
  - name: "client_msg_id"
    type: "string"
    description: ""

  - name: "latest_reply"
    type: "string"
    description: ""

  - name: "reply_count"
    type: "integer"
    description: ""

  - name: "reply_users"
    type: "array"
    description: "The IDs of users who replied in the thread."
    subattributes:
      - name: "value"
        type: "string"
        description: "The user ID."
        foreign-key-id: "user-id"

  - name: "reply_users_count"
    type: "number"
    description: ""

  - name: "subscribed"
    type: "boolean"
    description: ""

  - name: "team"
    type: "string"
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "text"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user"
    type: "string"
    description: "The ID of the user who created the thread."
    foreign-key-id: "user-id"
---