---
tap: "ujet"
version: "1"
key: "team"

name: "teams"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/teams.json"
description: |
  The `{{ table.name }}` table contains info about teams.

replication-method: "Full Table"

api-method:
  name: "Get teams"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "team-id"

  - name: "agents_count"
    type: "integer"
    description: ""

  - name: "assignees"
    type: "array"
    description: ""
    subattributes:
      - name: "first_name"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "agent_number"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "agent-id"

      - name: "last_name"
        type: "string"
        description: ""

      - name: "avatar_url"
        type: "string"
        description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "null"
    description: ""

  - name: "position"
    type: "integer"
    description: ""
---