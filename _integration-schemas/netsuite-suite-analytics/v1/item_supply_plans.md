---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-supply-plan"

name: "item_supply_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemsupplyplan.html"
description: |
  {{ integration.netsuite-replication-keys | flatify }}

  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "item_supply_plan_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
---