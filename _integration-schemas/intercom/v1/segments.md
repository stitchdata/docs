---
tap: "intercom"
version: "1"

name: "segments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/segments.json"
description: 
  The `{{ table.name }}` table contains information about segments within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The segment ID."
    foreign-key-id: "segment-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the segment was last updated."
    replication-key: true  

  - name: "count"
    type: "integer"
    description: ""
  - name: "created_at"
    type: "date-time"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
---
