---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-bin-number"

name: "transaction_bin_numbers"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_bin_numbers.html"
description: |
  From NetSuite's documentation:

  > Each line in this table represents one and only one bin.

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "bin_number"
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