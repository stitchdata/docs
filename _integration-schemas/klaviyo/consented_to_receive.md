---
tap: "klaviyo"
version: "1"
key: "consented-to-receive"

name: "consented_to_receive"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/consented_to_receive.json"
description: |
  The `{{ table.name }}` table contains metrics related to `Consented to Receive SMS` events.

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