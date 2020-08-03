---
tap: "netsuite-suite-analytics"
version: "1"
key: "memorized-tran"

name: "memorized_trans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/memorized_trans.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "action"
    type: "string"
    description: ""

  - name: "automatic_entry"
    type: "string"
    description: ""

  - name: "date_next_posting"
    type: "date-time"
    description: ""

  - name: "date_subsequent_posting"
    type: "date-time"
    description: ""

  - name: "days_in_advance"
    type: "integer"
    description: ""

  - name: "employee_id"
    type: "integer"
    description: ""

  - name: "frequency"
    type: "string"
    description: ""

  - name: "ingroup"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_indefinite"
    type: "string"
    description: ""

  - name: "isdeferred"
    type: "string"
    description: ""

  - name: "isgroup"
    type: "string"
    description: ""

  - name: "memorized_id"
    type: "integer"
    description: ""

  - name: "next_occurance"
    type: "date-time"
    description: ""

  - name: "number_remaining"
    type: "integer"
    description: ""

  - name: "repeat_every"
    type: "integer"
    description: ""

  - name: "subsequent_occurance"
    type: "date-time"
    description: ""

  - name: "time_period"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""

  - name: "update_addresses"
    type: "string"
    description: ""

  - name: "update_prices"
    type: "string"
    description: ""
---