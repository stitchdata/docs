---
tap: "pepperjam"
version: "1"
key: "publisher_performance"

name: "publisher_performance"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#PublisherPerformance"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/publisher_performance.json"
description: |
  The `{{ table.name }}` table contains information about publishers' performance within a {{ table.attribution-window-days }}-day time frame from the date of the last table replication.

  **Note**: During every replication job, Stitch will replicate the last {{ table.attribution-window-days }} days' worth of data for this table. Refer to the [Attribution windows and data extraction](#attribution-windows-data-extraction) section for more info.

replication-method: "Key-based Incremental"
attribution-window: true
attribution-window-days: "30"

api-method:
  name: "getPublisherPerformance"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#PublisherPerformance"

attributes:
  - name: "publisher_id"
    type: "integer"
    description: "The publisher ID."
    foreign-key-id: "publisher-id"

  - name: "order_id"
    type: "integer"
    description: "The order ID."
    foreign-key-id: "order-id"

  - name: "sale_date"
    type: "date-time"
    primary-key: true
    description: "The date the sale was made."
    replication-key: true

  - name: "bonus_amount"
    type: "number"
    description: ""
  - name: "clicks"
    type: "integer"
    description: ""
  - name: "company"
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
  - name: "leads"
    type: "integer"
    description: ""
  - name: "publisher"
    type: "string"
    description: ""
  - name: "publisher_bonus"
    type: "number"
    description: ""
  - name: "publisher_commission"
    type: "number"
    description: ""
  - name: "publisher_type"
    type: "string"
    description: ""
  - name: "sale_lead_amount"
    type: "number"
    description: ""
  - name: "sales"
    type: "integer"
    description: ""
  - name: "site_bonus"
    type: "number"
    description: ""
  - name: "site_commission"
    type: "number"
    description: ""
  - name: "state"
    type: "string"
    description: ""
  - name: "total_commission"
    type: "number"
    description: ""
  - name: "website"
    type: "string"
    description: ""
---