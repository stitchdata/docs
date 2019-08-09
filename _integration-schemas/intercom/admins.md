---
tap: "intercom"
# version: "15-10-2015"

name: "admins"
doc-link: https://developers.intercom.io/docs/admins
description: |
  The `{{ table.name }}` table contains info about the admins and teams in your {{ integration.display_name }} account.

replication-method: "Full Table"
api-method:
  name: listAdmins
  doc-link: https://developers.intercom.io/docs/list-admins

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The admin or team ID."
    foreign-key-id: "admin-id"

  - name: "type"
    type: "string"
    description: "The admin type. This value will be either `admin` or `team`."

  - name: "name"
    type: "string"
    description: "The name of the admin or team."

  - name: "email"
    type: "string"
    description: "The email address of the admin. This will be `NULL` for teams."

  - name: "away_mode_enabled"
    type: "boolean"
    description: "Indicates if the admin is currently set in away mode."

  - name: "away_mode_reassign"
    type: "boolean"
    description: "Indicates if the admin is set to automatically reassign new conversations to the app's default inbox."

  - name: "team_ids"
    type: "array"
    description: "A list of the IDs of the teams the admin is a part of."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The ID of the team the admin is a part of."
---