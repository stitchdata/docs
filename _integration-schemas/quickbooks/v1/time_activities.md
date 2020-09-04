---
tap: "quickbooks"
version: "1"
key: "time-activity"

name: "time_activities"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/timeactivity"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/time_activities.json"
description: |
  The `{{ table.name }}` table contains info about vendor and employee time records in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a time activity"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/timeactivity#query-a-timeactivity"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The time activity ID."
    foreign-key-id: "time-activity-id"

  - name: "BillableStatus"
    type: "string"
    description: ""

  - name: "CustomerRef"
    type: "object"
    description: "Details about the customer associated with the time activity."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The customer ID."
        foreign-key-id: "customer-id"

  - name: "Description"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "EmployeeRef"
    type: "object"
    description: "Details about the employee associated with the time activity."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The employee ID."
        foreign-key-id: "employee-id"

  - name: "HourlyRate"
    type: "integer"
    description: ""

  - name: "Hours"
    type: "integer"
    description: ""

  - name: "ItemRef"
    type: "object"
    description: "Details about the item associated with the time activity."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "item-id"

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

  - name: "Minutes"
    type: "integer"
    description: ""

  - name: "NameOf"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "Taxable"
    type: "boolean"
    description: ""

  - name: "TxnDate"
    type: "date-time"
    description: ""
---