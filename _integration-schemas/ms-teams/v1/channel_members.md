---
tap: "ms-teams"
version: "1"
key: "channel-member"

name: "channel_members"
doc-link: "https://docs.microsoft.com/en-us/graph/api/conversationmember-list?view=graph-rest-beta&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/channel_members.json"
description: |
  The `{{ table.name }}` table contains information about conversation members within a chat or channel in your Microsoft account.

replication-method: "Full Table"

api-method:
  name: "List conversation members"
  doc-link: "https://docs.microsoft.com/en-us/graph/api/conversationmember-list?view=graph-rest-beta&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The conversation member ID."
    #foreign-key-id: "conversation-members-id"

  - name: "channel_id"
    type: "string"
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "display_name"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "roles"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "user_id"
    type: "string"
    description: "The user ID."
    foreign-key-id: "user-id"
---
