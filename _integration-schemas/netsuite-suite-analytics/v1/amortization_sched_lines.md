---
tap: "netsuite-suite-analytics"
version: "1"
key: "amortization-sched-lines"

name: "amortization_sched_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/amortization_sched_lines.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "account_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "accounting_period_id"
    type: "integer"
    netsuite-primary-key: true
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
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "schedule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "amortization-schedule-id"
---