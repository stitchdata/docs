---
tap: "pepperjam"
version: "1"
key: "creative_performance"

name: "creative_performance"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativeDetails"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_performance.json"
description: |
  The {{ table.name }} table contains information about your {{ integration.display_name }} creatives' performance within a 30-day time frame from the date of the last table replication.

replication-method: "Key-based Incremental"
attribution-window: true

api-method:
    name: "getCreativeDetails"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativeDetails"

attributes:
  - name: "creative_id"
    type: "integer"
    primary-key: true
    description: "The creative ID."
    #foreign-key-id: "creative-id"

  - name: "creative_type"
    type: "string"
    primary-key: true
    description: "The type of creative."
    #foreign-key-id: "type-id"

  - name: "date"
    type: "date"
    primary-key: true
    description: "The date the creative was published."
    #foreign-key-id: "date-id"

  - name: "datetime"
    type: "date-time"
    description: "The duration of the creative."
    replication-key: true
      
  - name: "affiliate_usage"
    type: "integer"
    description: ""
  - name: "click_through_rate"
    type: "null"
    description: ""
  - name: "clicks"
    type: "integer"
    description: ""
  - name: "commission"
    type: "null"
    description: ""
  - name: "creative_name"
    type: "string"
    description: ""
  - name: "earnings_per_click"
    type: "null"
    description: ""
  - name: "group_id"
    type: "integer"
    description: ""
  - name: "impressions"
    type: "integer"
    description: ""
  - name: "items"
    type: "integer"
    description: ""
  - name: "sales"
    type: "null"
    description: ""
  - name: "transactions"
    type: "integer"
    description: ""
---
