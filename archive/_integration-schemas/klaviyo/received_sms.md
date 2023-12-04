---
tap: "klaviyo"
version: "1"
key: "received-sms"

name: "received_sms"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/received_sms.json"
description: |
  The `{{ table.name }}` table contains metrics related to `Received SMS` events.

replication-method: "Key-based Incremental"

api-method:
  name: "Get metrics info"
  doc-link: "https://www.klaviyo.com/docs/api/metrics"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""

  - name: "timestamp"
    type: "integer"
    replication-key: true
    description: ""

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
  
  - name: "statistic_id"
    type: "string"
    description: ""
  
  - name: "uuid"
    type: "string"
    description: ""
---