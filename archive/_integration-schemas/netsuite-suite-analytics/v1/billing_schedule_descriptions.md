---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-schedule-description"

name: "billing_schedule_descriptions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_schedule_descriptions.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "billing_schedule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-schedule-id"

  - name: "billing_schedule_type"
    type: "string"
    description: ""

  - name: "frequency"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "recurrence_count"
    type: "integer"
    description: ""
---