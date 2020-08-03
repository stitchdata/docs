---
tap: "deputy"
version: "1"
key: "company-period"

name: "company_periods"
doc-link: "https://www.deputy.com/api-doc/Resources/CompanyPeriod"

description: |
  The `{{ table.name }}` table contains info about company periods.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The company period ID."
    foreign-key-id: "company-period-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the was last modified."

  - name: "Start"
    type: "integer"
    description: ""

  - name: "DateStart"
    type: "date"
    description: ""

  - name: "End"
    type: "integer"
    description: ""

  - name: "DateEnd"
    type: "date"
    description: ""

  - name: "Company"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "PayPeriod"
    type: "integer"
    description: ""
    foreign-key-id: "pay-period-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---