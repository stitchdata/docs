---
tap: "intercom"
version: "1"

name: "teams"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/teams.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The team ID."
    foreign-key-id: "team-id"

  - name: "admin_ids"
    type: "array"
    description: "A list of admin IDs."
    subattributes:
      - name: "id"
        type: "string"
        description: "The admin ID."
  
  - name: "name"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
---
