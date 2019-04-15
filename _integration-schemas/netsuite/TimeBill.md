---
tap: "netsuite"
version: "1.0"

name: "TimeBill"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/timebill.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/TimeBill.json"
description: |
  The `{{ table.name }}` table contains info about the time transactions in your {{ integration.display_name }} account. Also known as time bills, these transactions records the hours worked by an employee. This transaction can be used to record billable hours and invoice customers.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Transactions"
  name: "Track Time"

feature-requirements:
  - tab: "Employees"
    name: "Time Tracking"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "time-bill-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "_class"
    type: "varies"
    description: ""

  - name: "approvalStatus"
    type: "varies"
    description: ""

  - name: "caseTaskEvent"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "employee"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "hours"
    type: "varies"
    description: ""

  - name: "isBillable"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "overrideRate"
    type: "boolean, string"
    description: ""

  - name: "paidExternally"
    type: "boolean, string"
    description: ""

  - name: "payrollItem"
    type: "varies"
    description: ""

  - name: "price"
    type: "varies"
    description: ""

  - name: "rate"
    type: "number, string"
    description: ""

  - name: "rejectionNote"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "supervisorApproval"
    type: "boolean, string"
    description: ""

  - name: "temporaryLocalJurisdiction"
    type: "varies"
    description: ""

  - name: "temporaryStateJurisdiction"
    type: "varies"
    description: ""

  - name: "timeSheet"
    type: "varies"
    description: ""

  - name: "timeType"
    type: "varies"
    description: ""

  - name: "tranDate"
    type: "date-time"
    description: ""

  - name: "workplace"
    type: "varies"
    description: ""
---