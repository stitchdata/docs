---
tap: "deputy"
version: "1.0"
key: "system-usage-balance"

name: "system_usage_balances"
doc-link: "https://www.deputy.com/api-doc/Resources/SystemUsageBalance"

description: |
  The `{{ table.name }}` table contains info about system usage balances.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The system usage balance ID."
    foreign-key-id: "system-usage-balance-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the system usage balance was last modified."

  - name: "Type"
    type: "integer"
    description: ""

  - name: "Date"
    type: "date"
    description: ""

  - name: "Credit"
    type: "number"
    description: ""

  - name: "Description"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---