---
tap: "quickbooks"
version: "1"
key: "budget"

name: "budgets"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/budget"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/budgets.json"
description: |
  The `{{ table.name }}` table contains info about the current state of budgets in your {{ integration.display_name }} instance. **Note**: Both active and inactive budgets are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query the budget"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/budget#query-the-budget"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The budget ID."
    foreign-key-id: "budget-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "BudgetDetail"
    type: "array"
    description: ""
    subattributes:
      - name: "AccountRef"
        type: "object"
        description: "Details about the account associated with the budget."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The account ID."
            foreign-key-id: "account-id"

      - name: "ClassRef"
        type: "object"
        description: "Details about the class associated with the budget."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The class ID."
            foreign-key-id: "class-id"

      - name: "CustomerRef"
        type: "object"
        description: "Details about the customer associated with the budget."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The customer ID."
            foreign-key-id: "customer-id"

      - name: "DepartmentRef"
        type: "object"
        description: "Details about the department associated with the budget."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The department ID."
            foreign-key-id: "department-id"

      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "BudgetDate"
        type: "date-time"
        description: ""

  - name: "BudgetEntryType"
    type: "string"
    description: ""

  - name: "BudgetType"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "EndDate"
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

  - name: "Name"
    type: "string"
    description: ""

  - name: "StartDate"
    type: "date-time"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---