---
tap: "deputy"
version: "1.0"
key: "pay-period"

name: "pay_periods"
doc-link: "https://www.deputy.com/api-doc/Resources/PayPeriod"

description: |
  The `{{ table.name }}` table contains info about pay periods.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The pay period ID."
    foreign-key-id: "pay-period-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the pay period was last modified."

  - name: "Name"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "StartDate"
    type: "date"
    description: ""

  - name: "Cycle"
    type: "integer"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---