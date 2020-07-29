---
tap: "intercom"
version: "1"

name: "company_segments"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#company-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/company_segments.json"
description: |
  The `{{ table.name }}` table contains information about company segments in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "listAllSegments"
    doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#list-segments"

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
