---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-history"

name: "transaction_history"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_history.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"
  - name: "action"
    type: "string"
    description: ""
  - name: "amount"
    type: "number"
    description: ""
  - name: "date_time"
    type: "date-time"
    description: ""
  - name: "date_transaction"
    type: "date-time"
    description: ""
  - name: "document_number"
    type: "string"
    description: ""
  - name: "entity_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"
  - name: "transaction_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"
  - name: "transaction_number"
    type: "string"
    description: ""
  - name: "transaction_type"
    type: "string"
    description: ""
  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"
---