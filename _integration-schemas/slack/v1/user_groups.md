---
tap: "slack"
version: "1"
key: "user-group"

name: "user_groups"
doc-link: "https://api.slack.com/methods/usergroups.list"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/user_groups.json"
description: |
  The `{{ table.name }}` table contains info about user groups from your {{ integration.display_name }} team.

replication-method: "Full Table"

api-method:
  name: "usergroups.list"
  doc-link: "https://api.slack.com/methods/usergroups.list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user group ID."
    foreign-key-id: "group-id"

  - name: "created"
    type: "date-time"
    description: ""

  - name: "creator"
    type: "string"
    description: ""
  
  - name: "is_archived"
    type: "boolean"
    description: ""

  - name: "is_deleted"
    type: "boolean"
    description: ""

  - name: "is_group"
    type: "boolean"
    description: ""

  - name: "is_moved"
    type: "integer"
    description: ""

  - name: "is_mpim"
    type: "boolean"
    description: ""

  - name: "is_open"
    type: "boolean"
    description: ""

  - name: "is_pending_ext_shared"
    type: "boolean"
    description: ""

  - name: "is_read_only"
    type: "boolean"
    description: ""

  - name: "is_thread_only"
    type: "boolean"
    description: ""

  - name: "last_read"
    type: "date-time"
    description: ""

  - name: "members"
    type: "array"
    description: "The user IDs of members belonging to the user group."
    subattributes:
      - name: "value"
        type: "string"
        description: "The user ID."
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

  - name: "parent_group"
    type: "string"
    description: "The parent group ID."
    foreign-key-id: "group-id"

  - name: "priority"
    type: "number"
    description: ""

  - name: "purpose"
    type: "object"
    description: ""
    subattributes:
      - name: "creator"
        type: "string"
        description: "The user ID of the user who created the group."
        foreign-key-id: "user-id"

      - name: "last_set"
        type: "integer"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "topic"
    type: "object"
    description: ""
    subattributes:
      - name: "creator"
        type: "string"
        description: "The user ID of the user who created the group."
        foreign-key-id: "user-id"

      - name: "last_set"
        type: "integer"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "unread_count"
    type: "integer"
    description: ""

  - name: "unread_count_display"
    type: "integer"
    description: ""
---