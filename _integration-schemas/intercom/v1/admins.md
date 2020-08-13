---
tap: "intercom"
version: "1"

name: "admins"
doc-link: "https://developers.intercom.com/intercom-api-reference/reference#admin-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/admins.json"
description: |
  The `{{ table.name }}` table lists info about the admins in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "listAllAdmins"
    doc-link: "https://developers.intercom.com/intercom-api-reference/reference#list-admins"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The admin ID."
    foreign-key-id: "admin-id"

  - name: "admin_ids"
    type: "null"
    description: ""
  - name: "away_mode_enabled"
    type: "boolean"
    description: ""
  - name: "away_mode_reassign"
    type: "boolean"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  - name: "has_inbox_seat"
    type: "boolean"
    description: ""
  
  - name: "job_title"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "team_ids"
    type: "array"
    description: "A list of the of team IDs that the admin is part of."
    subattributes:
      - name: "value"
        type: "integer"
        description: "[DESCRIPTION]"
        foreign-key-id: "team-id"
  - name: "type"
    type: "string"
    description: ""
---
