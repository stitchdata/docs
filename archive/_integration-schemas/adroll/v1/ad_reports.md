---
tap: "adroll"
version: "1"
key: "ad-report"

name: "ad_reports"
doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-report-ad"
singer-schema: "https://github.com/singer-io/tap-adroll/blob/master/tap_adroll/schemas/ad_reports.json"
description: |
  The `{{ table.name }}` table contains ad-level reporting data from your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get ad reports"
  doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-report-ad"

attributes:
  - name: "eid"
    type: "string"
    primary-key: true
    description: "The ad report EID."
    # foreign-key-id: "ad-report-id"

  - name: "date"
    type: "date-time"
    primary-key: true
    description: "The start and end dates of the report."
    foreign-key-id: "report-date"
    replication-key: true

  - name: "ad"
    type: "string"
    description: ""
    foreign-key-id: "ad-id"

  - name: "ad_size"
    type: "string"
    description: ""

  - name: "adjusted_click_through_ratio"
    type: "number"
    description: ""

  - name: "adjusted_cpa"
    type: "number"
    description: ""

  - name: "adjusted_ctc"
    type: "integer"
    description: ""

  - name: "adjusted_total_conversion_rate"
    type: "number"
    description: ""

  - name: "adjusted_total_conversions"
    type: "integer"
    description: ""

  - name: "adjusted_view_through_ratio"
    type: "number"
    description: ""

  - name: "adjusted_vtc"
    type: "integer"
    description: ""

  - name: "advertiser"
    type: "string"
    description: ""

  - name: "attributed_click_through_rev"
    type: "number"
    description: ""

  - name: "attributed_rev"
    type: "number"
    description: ""

  - name: "attributed_view_through_rev"
    type: "number"
    description: ""

  - name: "billing_cost"
    type: "number"
    description: ""

  - name: "click_cpa"
    type: "number"
    description: ""

  - name: "click_through_conversions"
    type: "integer"
    description: ""

  - name: "click_through_ratio"
    type: "number"
    description: ""

  - name: "clicks"
    type: "integer"
    description: ""

  - name: "cost"
    type: "number"
    description: ""

  - name: "cpa"
    type: "number"
    description: ""

  - name: "cpc"
    type: "number"
    description: ""

  - name: "cpm"
    type: "number"
    description: ""

  - name: "created_date"
    type: "string"
    description: ""

  - name: "ctr"
    type: "number"
    description: ""
  
  - name: "height"
    type: "integer"
    description: ""

  - name: "impressions"
    type: "integer"
    description: ""

  - name: "paid_impressions"
    type: "integer"
    description: ""

  - name: "prospects"
    type: "integer"
    description: ""

  - name: "roi"
    type: "number"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "total_conversion_rate"
    type: "number"
    description: ""

  - name: "total_conversions"
    type: "integer"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "view_through_conversions"
    type: "integer"
    description: ""

  - name: "view_through_ratio"
    type: "number"
    description: ""

  - name: "width"
    type: "integer"
    description: ""
---