---
tap: "pepperjam"
version: "1"
key: "creative_text"

name: "creative_text"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Text"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_text.json"
description: |
  The  {{ table.name }} table contains information about text creatives in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "getTextCreative"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Text"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The text ID."
    #foreign-key-id: "text-id"

  - name: "modified"
    type: "date-time"
    description: "The time the text was last modified."
    replication-key: true  

  - name: "allow_deep_link"
    type: "integer"
    description: ""
  - name: "created"
    type: "date-time"
    description: ""
  - name: "description"
    type: "string"
    description: ""
  - name: "end_date"
    type: "date-time"
    description: ""
  - name: "link_anchor_text"
    type: "string"
    description: ""
  - name: "private"
    type: "integer"
    description: ""
  - name: "private_affiliates"
    type: "null"
    description: ""
  - name: "promotions"
    type: "null"
    description: ""
  - name: "start_date"
    type: "date-time"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "url"
    type: "string"
    description: ""
  - name: "view_date"
    type: "date-time"
    description: ""
---
