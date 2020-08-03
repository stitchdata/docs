---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-inventory-number"

name: "transaction_inventory_numbers"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_inventory_numbers.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "inventory_number"
    type: "string"
    description: ""
  - name: "quantity"
    type: "integer"
    description: ""
  - name: "transaction_id"
    type: "integer"
    description: ""
  - name: "transaction_line"
    type: "integer"
    description: ""
---