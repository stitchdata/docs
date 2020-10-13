---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-tracking-number"

name: "transaction_tracking_numbers"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_tracking_numbers.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "tracking_number"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""
---