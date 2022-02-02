---
tap: "klaviyo"
version: "1"
key: "list"

name: "lists"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/lists.json"
description: |
  The {{ table.name }} table contains info about the lists in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get lists"
  doc-link: "https://apidocs.klaviyo.com/reference/lists-segments#get-lists"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The list ID."

  - name: "created"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
  
  - name: "object"
    type: "string"
    description: ""
  
  - name: "person_count"
    type: "integer"
    description: ""
  
  - name: "type"
    type: "string"
    description: ""
  
  - name: "updated"
    type: "string"
    description: ""
---