---
tap: "netsuite-suite-analytics"
version: "1"
key: "amortization-schedule"

name: "amortization_schedules"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/amortizationschedule.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "amount"
    type: "number"
    description: ""

  - name: "initial_amount"
    type: "string"
    description: ""

  - name: "is_template"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "period_offset"
    type: "integer"
    description: ""

  - name: "residual"
    type: "string"
    description: ""

  - name: "schedule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "amortization-schedule-id"

  - name: "schedule_method"
    type: "string"
    description: ""

  - name: "schedule_number"
    type: "string"
    description: ""

  - name: "schedule_type"
    type: "string"
    description: ""

  - name: "start_offset"
    type: "integer"
    description: ""

  - name: "term_source"
    type: "string"
    description: ""
---