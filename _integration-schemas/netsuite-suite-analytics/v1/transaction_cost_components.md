---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-cost-components"

name: "transaction_cost_components"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_cost_components.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "amount"
    type: "number"
    description: ""

  - name: "cost_category"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "standard_cost"
    type: "number"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""

  - name: "transaction_line"
    type: "integer"
    description: ""
---