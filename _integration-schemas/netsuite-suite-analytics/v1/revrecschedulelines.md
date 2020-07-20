---
tap: "netsuite-suite-analytics"
version: "1"
key: "revenue-recognition-schedule-line"

name: "revrecschedulelines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revrecschedulelines.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "amount"
    type: "string"
    description: ""

  - name: "is_recognized"
    type: "string"
    description: ""

  - name: "journal_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "schedule_id"
    type: "integer"
    description: ""
    foreign-key-id: "revenue-recognition-schedule-id"
---