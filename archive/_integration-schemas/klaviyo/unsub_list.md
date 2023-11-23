---
tap: "klaviyo"
version: "1"
key: "unsubscribe-list"

name: "unsub_list"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/unsub_list.json"
description: |
  The `{{ table.name }}` table contains metrics related to `Unsubscribed from List` events.

replication-method: "Key-based Incremental"

api-method:
  name: "Get metrics info"
  doc-link: "https://www.klaviyo.com/docs/api/metrics"

attributes:
  - name: "id"
    type: "string"
    primay-key: true
    description: "The unsubscribe to list event ID."
  
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
  
  - name: "uuid"
    type: "string"
    description: ""
---