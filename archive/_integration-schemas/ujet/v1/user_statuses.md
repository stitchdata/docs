---
tap: "ujet"
version: "1"
key: "user-status"

name: "user_statuses"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ujet/blob/master/tap_ujet/schemas/user_statuses.json"
description: |
  The `{{ table.name }}` table contains info about user statuses.

replication-method: "Full Table"

api-method:
  name: "Get user statuses"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "user-status-id"

  - name: "color"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "wfm_id"
    type: "integer"
    description: ""
---