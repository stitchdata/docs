---
tap: "deputy"
version: "1.0"
key: "company"

name: "companies"
doc-link: "https://www.deputy.com/api-doc/Resources/Company"

description: |
  The `{{ table.name }}` table contains info about companies.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the company was last modified."

  - name: "Portfolio"
    type: "integer"
    description: ""

  - name: "Code"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "ParentCompany"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "CompanyName"
    type: "string"
    description: ""

  - name: "TradingName"
    type: "string"
    description: ""

  - name: "BusinessNumber"
    type: "string"
    description: ""

  - name: "CompanyNumber"
    type: "string"
    description: ""

  - name: "IsWorkplace"
    type: "boolean"
    description: ""

  - name: "IsPayrollEntity"
    type: "boolean"
    description: ""

  - name: "PayrollExportCode"
    type: "integer"
    description: ""

  - name: "Address"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "Contact"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---