---
tap: "quickbooks"
version: "1"
key: "employee"

name: "employees"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/employee"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/employees.json"
description: |
  The `{{ table.name }}` table contains info about the people working for your company. **Note**: Both active and inactive employees are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query an employee"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/employee#query-an-employee"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The employee ID."
    foreign-key-id: "employee-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "BillableTime"
    type: "boolean"
    description: ""

  - name: "BirthDate"
    type: "date-time"
    description: ""

  - name: "DisplayName"
    type: "string"
    description: ""

  - name: "FamilyName"
    type: "string"
    description: ""

  - name: "GivenName"
    type: "string"
    description: ""

  - name: "HiredDate"
    type: "date-time"
    description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "PrimaryPhone"
    type: "object"
    description: ""
    subattributes:
      - name: "FreeFormNumber"
        type: "string"
        description: ""

  - name: "PrintOnCheckName"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---