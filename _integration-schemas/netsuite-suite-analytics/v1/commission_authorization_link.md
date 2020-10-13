---
tap: "netsuite-suite-analytics"
version: "1"
key: "commission-authorization-link"

name: "commission_authorization_link"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/commission_authorization_link.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "authorized_amount"
    type: "integer"
    description: ""

  - name: "calc_type"
    type: "string"
    description: ""

  - name: "commission_transaction_id"
    type: "integer"
    description: ""

  - name: "commission_transaction_line_id"
    type: "integer"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "schedule_id"
    type: "integer"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""
---