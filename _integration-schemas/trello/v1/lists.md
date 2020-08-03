---
tap: "trello"
version: "1"
key: "list"

name: "lists"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-lists-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/lists.json"
description: |
  The {{ table.name }} table contains info about lists on boards that the [authorizing user](#data-replication-board-membership) is a member of.

  **Note**: To replicate this table, the [boards](#boards) table must be set to replicate.

replication-method: "Full Table"

api-method:
    name: "Get lists on a board"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-lists-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "closed"
    type: "boolean"
    description: ""  

  - name: "idBoard"
    type: "string"
    description: ""
    foreign-key-id: "board-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "pos"
    type: "number"
    description: ""

  - name: "softLimit"
    type: "integer"
    description: ""

  - name: "subscribed"
    type: "boolean"
    description: ""
---