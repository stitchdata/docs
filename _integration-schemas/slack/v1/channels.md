---
tap: "slack"
version: "1"
key: "channel"

name: "channels"
doc-link: "https://api.slack.com/types/channel"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/channels.json"
description: |
  The `{{ table.name }}` table contains info about the channels in your {{ integration.display_name }} workspace. This includes conversations, channels, and direct messages.

  **Note**: Some types of channels - for example, private or archived channels - will be replicated only if the appropriate settings are configured in the integration's settings. Refer to the {{ integration.display_name }} [setup steps](#add-integration) for more info.

replication-method: "Full Table"

api-method:
  name: "conversations.list"
  doc-link: "https://api.slack.com/methods/conversations.list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "channel_id"
    type: "string"
    description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "creator"
    type: "string"
    description: "The ID of the user who created the channel."
    foreign-key-id: "user-id"
  
  - name: "is_archived"
    type: "boolean"
    description: ""

  - name: "is_channel"
    type: "boolean"
    description: ""

  - name: "is_ext_shared"
    type: "boolean"
    description: ""

  - name: "is_general"
    type: "boolean"
    description: ""

  - name: "is_group"
    type: "boolean"
    description: ""

  - name: "is_im"
    type: "boolean"
    description: ""

  - name: "is_member"
    type: "boolean"
    description: ""

  - name: "is_mpim"
    type: "boolean"
    description: ""

  - name: "is_org_shared"
    type: "boolean"
    description: ""

  - name: "is_pending_ext_shared"
    type: "boolean"
    description: ""

  - name: "is_private"
    type: "boolean"
    description: ""

  - name: "is_shared"
    type: "boolean"
    description: ""

  - name: "members"
    type: "array"
    description: "The channel members."
    subattributes:
      - name: "value"
        type: "string"
        description: "The channel member's user ID."
        foreign-key-id: "user-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "name_normalized"
    type: "string"
    description: ""

  - name: "num_members"
    type: "integer"
    description: ""

  - name: "parent_conversation"
    type: "string"
    description: ""

  - name: "pending_connected_team_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The team ID."
        foreign-key-id: "team-id"

  - name: "pending_shared"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "previous_names"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "purpose"
    type: "object"
    description: ""
    subattributes:
      - name: "creator"
        type: "string"
        description: ""

      - name: "last_set"
        type: "date-time"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "shared_team_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The team ID."
        foreign-key-id: "team-id"

  - name: "topic"
    type: "object"
    description: ""
    subattributes:
      - name: "creator"
        type: "string"
        description: ""

      - name: "last_set"
        type: "date-time"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "unlinked"
    type: "date-time"
    description: ""
---