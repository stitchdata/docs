---
tap: "slack"
version: "1"
key: ""

name: "threads"
doc-link: "https://api.slack.com/docs/conversations-api"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/threads.json"
description: |
  The `{{ table.name }}` table contains information about conversation threads in your {{ integration.display_name }} team. This table will do a Full Table Replication for each parent message that is added.

replication-method: "Full Table"

api-method:
    name: "conversations.replies"
    doc-link: "https://api.slack.com/methods/conversations.replies"

attributes:
  - name: "channel_id"
    type: "string"
    primary-key: true
    description: "The channel ID."

  - name: "thread_ts"
    type: "string"
    primary-key: true
    description: "The conversation thread timestamp."
    #foreign-key-id: "thread-timestamp"

  - name: "ts"
    type: "date-time"
    description: "The conversation timestamp."
    foreign-key-id: "timestamp"
      
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
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "reply_users_count"
    type: "number"
    description: ""
  - name: "subscribed"
    type: "boolean"
    description: ""
  - name: "team"
    type: "string"
    description: ""
  - name: "text"
    type: "string"
    description: ""
  
  - name: "type"
    type: "string"
    description: ""
  - name: "user"
    type: "string"
    description: ""
---
