---
tap: "klaviyo"
version: "1"
key: "failed-to-deliver"

name: "failed_to_deliver"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/failed_to_deliver.json"
description: |
  The `{{ table.name }}` table contains metrics related to `Failed to Deliver SMS` events.

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