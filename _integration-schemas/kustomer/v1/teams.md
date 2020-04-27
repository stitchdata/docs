---
tap: "kustomer"
version: "1"

name: "teams"
doc-link: "https://dev.kustomer.com/v1/teams/"
singer-schema: "https://github.com/singer-io/tap-kustomer/blob/master/tap_kustomer/schemas/teams.json"
description: |
  The {{ table.name }} table contains information about teams in the {{ integration.display_name }} app.

replication-method: "Key-based Incremental"

api-method:
    name: "getTeams"
    doc-link: "https://dev.kustomer.com/v1/teams/get-team"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The team ID."
    #foreign-key-id: "team-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the team was last updated."
    replication-key: true

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "created_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "deleted_at"
    type: "string"
    description: ""

  - name: "deleted_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "icon"
    type: "string"
    description: ""

  - name: "links"
    type: "object"
    description: ""
    subattributes:
      - name: "self"
        type: "string"
        description: ""

  - name: "members"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "modified_at"
    type: "string"
    description: ""

  - name: "modified_by"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "org"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""

  - name: "role_groups"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""
---
