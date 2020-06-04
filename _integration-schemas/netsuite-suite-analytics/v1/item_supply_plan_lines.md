---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-supply-line"

name: "item_supply_plan_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_supply_plan_lines.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "is_order_created"
    type: "string"
    description: ""

  - name: "item_supply_plan_id"
    type: "integer"
    description: ""

  - name: "line_id"
    type: "integer"
    description: ""

  - name: "order_date"
    type: "date-time"
    description: ""

  - name: "order_type"
    type: "string"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "receipt_date"
    type: "date-time"
    description: ""

  - name: "source_location_id"
    type: "integer"
    description: ""
---