---
tap: "ujet"
version: "1"
key: "menu"

name: "menus"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/menus.json"
description: |
  The `{{ table.name }}` table contains info about menus.

replication-method: "Key-based Incremental"

api-method:
  name: "Get menus"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "menu-id"

  - name: "agent_assignments"
    type: "array"
    description: ""
    subattributes:
      - name: "assignee"
        type: "object"
        description: ""
        subattributes:
          - name: "agent_number"
            type: "string"
            description: ""

          - name: "avatar_url"
            type: "uri"
            description: ""

          - name: "first_name"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "agent-id"

          - name: "last_name"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

      - name: "channel_type"
        type: "string"
        description: ""

      - name: "group_type"
        type: "string"
        description: ""

      - name: "lang"
        type: "string"
        description: ""

      - name: "queue_level"
        type: "string"
        description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "hidden"
    type: "boolean"
    description: ""

  - name: "menu_type"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "output_msg"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "position"
    type: "integer"
    description: ""

  - name: "team_assignments"
    type: "array"
    description: ""
    subattributes:
      - name: "queue_level"
        type: "string"
        description: ""

      - name: "group_type"
        type: "string"
        description: ""

      - name: "channel_type"
        type: "string"
        description: ""

      - name: "team"
        type: object
        description: ""
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "agents_count"
            type: "integer"
            description: ""

          - name: "parent_id"
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

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "team-id"

          - name: "position"
            type: "integer"
            description: ""

          - name: "deleted"
            type: "boolean"
            description: ""
---