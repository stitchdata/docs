---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-supply-plan-source"

name: "item_supply_plan_source"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_supply_plan_source.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "assembly_parent_id"
    type: "integer"
    description: ""

  - name: "date_order"
    type: "date-time"
    description: ""

  - name: "is_detail_transaction_line"
    type: "string"
    description: ""

  - name: "item_supply_plan_id"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "ship_receipt_date"
    type: "date-time"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""

  - name: "transaction_line_id"
    type: "integer"
    description: ""

  - name: "type_id"
    type: "string"
    description: ""
---