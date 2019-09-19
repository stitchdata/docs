---
tap: "klaviyo"
version: "1.0"

name: "global_exclusions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/global_exclusions.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: "https://www.klaviyo.com/docs/api/metrics"

attributes:
  - name: "email"
    type: "string"
    description: ""
  
  - name: "object"
    type: "string"
    description: ""
  
  - name: "reason"
    type: "string"
    description: ""
  
  - name: "timestamp"
    type: "string"
    description: ""
---
