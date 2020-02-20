---
tap: "klaviyo"
version: "1"

name: "subscribe_list"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/subscribe_list.json"
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
    description: "The subscribe ID."
#    foreign-key-id: "subscribe-id"
  
  - name: "datetime"
    type: "string"
    description: ""
  
  - name: "event_name"
    type: "string"
    description: ""
  
  - name: "event_properties"
    type: "object"
    description: ""
    subattributes:
      - name: "$event_id"
        type: "string"
        description: ""
      - name: "List"
        type: "string"
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
