---
tap: "mailshake"
version: "1"
key: "team-member"

name: "team_members"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/team_members.json"
description: |
  The `{{ table.name }}` table contains info about the individual members of your team.

replication-method: "Key-based Incremental"

api-method:
  name: "List team members"
  doc-link: "https://api-docs.mailshake.com/?shell#List-Members"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "team-member-id"

  - name: "teamID"
    type: "integer"
    replication-key: true
    description: ""
    # foreign-key-id: "team-id"

  - name: "emailAddress"
    type: "string"
    description: ""

  - name: "first"
    type: "string"
    description: ""

  - name: "fullName"
    type: "string"
    description: ""

  - name: "isDisabled"
    type: "boolean"
    description: ""

  - name: "isTeamAdmin"
    type: "boolean"
    description: ""

  - name: "last"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "teamBlockedDate"
    type: "date-time"
    description: ""

  - name: "teamName"
    type: "boolean"
    description: ""
---