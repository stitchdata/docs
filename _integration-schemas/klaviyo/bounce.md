---
tap: "klaviyo"
version: "1"

name: "bounce"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/bounce.json"
description: ""

replication-method: "Key-based Incremental"

replication key: "since"

api-method:
    name: "Metrics API"
    doc-link: "https://www.klaviyo.com/docs/api/metrics"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The bounce ID."
#    foreign-key-id: "bounce-id"

  - name: "datetime"
    type: "string"
    description: ""
  
  - name: "event_name"
    type: "string"
    description: ""
  
  - name: "event_properties"
    type: "object"
    description: ""
  
  - name: "object"
    type: "string"
    description: ""
  
  - name: "person"
    type: "object"
    description: ""
    subattributes:
      - name: "email"
        type: "string"
        description: ""
  
  - name: "statistic_id"
    type: "string"
    description: ""
  
  - name: "timestamp"
    type: "integer"
    description: ""
  
  - name: "uuid"
    type: "string"
    description: ""
---
