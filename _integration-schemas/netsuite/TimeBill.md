---
tap: "netsuite"
# version: "1.0"

name: "TimeBill"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/TimeBill.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "anything"
    description: ""

  - name: "approvalStatus"
    type: "anything"
    description: ""

  - name: "caseTaskEvent"
    type: "anything"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "customer"
    type: "anything"
    description: ""

  - name: "department"
    type: "anything"
    description: ""

  - name: "employee"
    type: "anything"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "hours"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isBillable"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "location"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "overrideRate"
    type: "boolean, string"
    description: ""

  - name: "paidExternally"
    type: "boolean, string"
    description: ""

  - name: "payrollItem"
    type: "anything"
    description: ""

  - name: "price"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "supervisorApproval"
    type: "boolean, string"
    description: ""

  - name: "temporaryLocalJurisdiction"
    type: "anything"
    description: ""

  - name: "temporaryStateJurisdiction"
    type: "anything"
    description: ""

  - name: "timeSheet"
    type: "anything"
    description: ""

  - name: "timeType"
    type: "anything"
    description: ""

  - name: "tranDate"
    type: "date-time"
    description: ""

  - name: "workplace"
    type: "anything"
    description: ""
---
