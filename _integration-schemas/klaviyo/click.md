---
tap: "klaviyo"
version: "1"

name: "click"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/click.json"
description: ""

replication-method: "Key-based Incremental"

replication key: "state"

api-method:
    name: ""
    doc-link: "https://www.klaviyo.com/docs/api/metrics"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The click ID."
    foreign-key-id: "click-id"
  
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
