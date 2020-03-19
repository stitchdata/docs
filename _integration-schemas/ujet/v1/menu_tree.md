---
tap: "ujet"
version: "1"
key: "menu-tree"

name: "menu_tree"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/menu_tree.json"
description: |
  The `{{ table.name }}` table contains info about menu trees.

replication-method: "Full Table"

api-method:
  name: "Get menu trees"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "menu-tree-id"

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