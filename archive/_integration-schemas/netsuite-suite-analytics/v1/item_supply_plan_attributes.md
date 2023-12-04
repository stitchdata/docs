---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-supply-plan-attribute"

name: "item_supply_plan_attributes"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_supply_plan_attributes.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "demand_source"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "item_supply_plan_id"
    type: "integer"
    description: ""

  - name: "lead_time"
    type: "integer"
    description: ""

  - name: "quantity_on_hand"
    type: "number"
    description: ""

  - name: "safety_stock"
    type: "number"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""
---