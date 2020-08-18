---
tap: "slack"
version: "1"
key: ""

name: "users"
doc-link: "https://api.slack.com/methods/users.list"
singer-schema: "https://github.com/singer-io/tap-slack/blob/master/tap_slack/schemas/users.json"
description: |
  The `{{ table.name }}` table lists all users in your {{ integration.display_name }} team.

replication-method: "Key-based Incremental"

api-method:
    name: "users.list"
    doc-link: "https://api.slack.com/methods/users.list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "updated"
    type: "date-time"
    description: "The time the user was last updated."
    replication-key: true

  - name: "color"
    type: "string"
    description: ""
  - name: "deleted"
    type: "boolean"
    description: ""
  - name: "has_2fa"
    type: "boolean"
    description: ""
  
  - name: "is_admin"
    type: "boolean"
    description: ""
  - name: "is_app_user"
    type: "boolean"
    description: ""
  - name: "is_bot"
    type: "boolean"
    description: ""
  - name: "is_owner"
    type: "boolean"
    description: ""
  - name: "is_primary_owner"
    type: "boolean"
    description: ""
  - name: "is_restricted"
    type: "boolean"
    description: ""
  - name: "is_ultra_restricted"
    type: "boolean"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "real_name"
    type: "string"
    description: ""
  - name: "team_id"
    type: "string"
    description: ""
  - name: "tz"
    type: "string"
    description: ""
  - name: "tz_label"
    type: "string"
    description: ""
  - name: "tz_offset"
    type: "integer"
    description: ""
---
