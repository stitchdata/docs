---
tap: "trello"
version: "1"
key: ""

name: "lists"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-lists-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/lists.json"
description: |
  The {{ table.name }} table contains information about lists from your boards in your {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "Get Lists on a Board"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-lists-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The list ID."
    #foreign-key-id: "lists-id"

  - name: "closed"
    type: "boolean"
    description: ""  
  - name: "idBoard"
    type: "string"
    description: ""
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
