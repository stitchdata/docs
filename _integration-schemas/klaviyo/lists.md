---
tap: "klaviyo"
version: "1.0"

name: "lists"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/lists.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: "https://www.klaviyo.com/docs/api/metrics"

attributes:
  - name: "created"
    type: "string"
    description: ""
  
  - name: "id"
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
