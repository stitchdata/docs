---
tap: "platformpurple"
# version: "1.0"

name: "transactions"
doc-link: 
singer-schema: https://github.com/singer-io/tap-platformpurple/blob/master/tap_platformpurple/schemas/transactions.json
description: |
  The `{{ table.name }}` contains info about

replication-method: "Key-based Incremental / Full Table"

attributes:
  - name: "transactionID"
    type: "integer"
    primary-key: true
    description: ""

  - name: "dateTime"
    type: "date-time"
    description: ""

  - name: "productID"
    type: "number"
    description: ""

  - name: "productSoldFor"
    type: "string"
    description: ""

  - name: "productName"
    type: "string"
    description: ""

  - name: "couponCodeUsed"
    type: "string"
    description: ""

  - name: "userEmail"
    type: "string"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""
---