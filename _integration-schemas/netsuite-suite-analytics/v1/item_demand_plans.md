---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-demand-plan"

name: "item_demand_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemdemandplan.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "alt_demand_source_item_id"
    type: "integer"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "historical_analysis_duration"
    type: "integer"
    description: ""

  - name: "item_demand_plan_id"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "last_modified_date"
    type: "date-time"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "projection_duration"
    type: "integer"
    description: ""

  - name: "projection_interval"
    type: "string"
    description: ""

  - name: "projection_method"
    type: "string"
    description: ""

  - name: "projection_start_date"
    type: "date-time"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
---