---
tap: "pepperjam"
version: "1"
key: "creative_performance_by_publisher"

name: "creative_performance_by_publisher"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativePerformanceByPublisher"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_performance_by_publisher.json"
description: |
  The `{{ table.name }}` table contains information about your {{ integration.display_name }} creatives' performance, per publisher, within a {{ table.attribution-window-days }}-day time frame from the date of the last table replication.

  **Note**: During every replication job, Stitch will replicate the last {{ table.attribution-window-days }} days' worth of data for this table. Refer to the [Attribution windows and data extraction](#attribution-windows-data-extraction) section for more info.

replication-method: "Key-based Incremental"
attribution-window: true
attribution-window-days: "30"

api-method:
  name: "getCreativePerformanceByPublisher"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativePerformanceByPublisher"

attributes:
  - name: "creative_id"
    type: "integer"
    primary-key: true
    description: "The creative ID."
    foreign-key-id: "creative-id"

  - name: "creative_type"
    type: "string"
    primary-key: true
    description: "The type of creative."

  - name: "date"
    type: "date"
    primary-key: true
    description: "The date the creative was published."

  - name: "publisher_id"
    type: "integer"
    primary-key: true
    description: "The publisher ID."
    foreign-key-id: "publisher-id"

  - name: "datetime"
    type: "date-time"
    description: "The duration of the creative."
    replication-key: true
      
  - name: "affiliate_usage"
    type: "integer"
    description: ""
  - name: "click_through_rate"
    type: "number"
    description: ""
  - name: "clicks"
    type: "integer"
    description: ""
  - name: "commission"
    type: "number"
    description: ""
  - name: "creative_name"
    type: "string"
    description: ""
  - name: "earnings_per_click"
    type: "number"
    description: ""
  - name: "group_id"
    type: "integer"
    description: ""
    foreign-key-id: "group-id"
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
    type: "number"
    description: ""
  - name: "transactions"
    type: "integer"
    description: ""
---