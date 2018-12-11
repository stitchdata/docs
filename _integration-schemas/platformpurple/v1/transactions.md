---
tap: "platformpurple"
version: "1.0"

name: "transactions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-platformpurple/blob/master/tap_platformpurple/schemas/transactions.json"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "transactionID"
    type: "integer"
    primary-key: true
    description: "The transaction ID."
    # foreign-key-id: "transaction-id"

  - name: "dateTime"
    type: "date-time"
    replication-key: true
    description: "The time the transaction occurred."

  - name: "couponCodeUsed"
    type: "string"
    description: "The coupon code used, if applicable."

  - name: "firstName"
    type: "string"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "productID"
    type: "number"
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "productName"
    type: "string"
    description: "THe product name."

  - name: "productSoldFor"
    type: "string"
    description: ""

  - name: "userEmail"
    type: "string"
    description: ""
---