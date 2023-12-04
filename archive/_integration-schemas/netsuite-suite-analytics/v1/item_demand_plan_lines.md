---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-demand-plan-line"

name: "item_demand_plan_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_demand_plan_lines.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "demand_date"
    type: "date-time"
    description: ""

  - name: "item_demand_plan_id"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""
---