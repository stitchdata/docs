---
tap: "slack"
version: "1"
key: ""

name: "channel_members"
doc-link: "https://api.slack.com/docs/conversations-api"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/channel_members.json"
description: |
  The `{{ table.name }}` table lists members of a channel in your {{ integration.display_name }} workspace. Channels are any channel-related information, such as conversations, channels and direct messages in your {{ integration.display_name }} workspace.

replication-method: "Full Table"

api-method:
    name: "conversation.members"
    doc-link: "https://api.slack.com/methods/conversations.members"

attributes:
  - name: "channel_id"
    type: "string"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"
  - name: "user_id" 
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id" 
---
