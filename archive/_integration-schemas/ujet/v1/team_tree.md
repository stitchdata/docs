---
tap: "ujet"
version: "1"
key: "team-tree"

name: "team_tree"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/team_tree.json"
description: |
  The `{{ table.name }}` table contains info about team trees.

replication-method: "Full Table"

api-method:
  name: "Get team trees"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "team-tree-id"

  - name: "agents_count"
    type: "integer"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "position"
    type: "integer"
    description: ""
---
