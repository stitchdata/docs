---
tap: "intercom"
version: "1"
name: "company_segments"
doc-link: ""

singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/company_segments.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The company segment ID."
    foreign-key-id: "company-segment" 

  - name: "updated_at"
    type: "date-time"
    description: "The time the company segment was last updated."
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
