---
tap: "deputy"
version: "1.0"
key: "system-usage-tracking"

name: "system_usage_tracking"
doc-link: "https://www.deputy.com/api-doc/Resources/SystemUsageTracking"

description: |
  The `{{ table.name }}` table contains info about system usage tracking.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The system usage tracking ID."
    #foreign-key-id: "system-usage-tracking-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the system usage tracking was last modified."

  - name: "Date"
    type: "date"
    description: ""

  - name: "EmpId"
    type: "integer"
    description: ""

  - name: "CompanyId"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "BalanceId"
    type: "integer"
    description: ""
    foreign-key-id: "system-usage-balance-id"

  - name: "UsageType"
    type: "integer"
    description: ""

  - name: "UsageRecordId"
    type: "integer"
    description: ""

  - name: "Usage"
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