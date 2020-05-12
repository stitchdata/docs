---
tap: "pepperjam"
version: "1"
key: "creative_performance_by_publisher"

name: "creative_performance_by_publisher"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativePerformanceByPublisher"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_performance_by_publisher.json"
description: |
  The {{ table.name }} table contains information about your {{ integration.display_name }} creatives' performance, per publisher, within a given year time frame.

replication-method: "Key-based Incremental"

api-method:
    name: "getCreativePerformanceByPublisher"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativePerformanceByPublisher"

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

  - name: "publisher_id"
    type: "integer"
    primary-key: true
    description: "The publisher ID."
    #foreign-key-id: "publisher-id"

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
  - name: "publisher"
    type: "string"
    description: ""
  - name: "sales"
    type: "null"
    description: ""
  - name: "transactions"
    type: "integer"
    description: ""
---
