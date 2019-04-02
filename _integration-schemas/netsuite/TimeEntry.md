---
tap: "netsuite"
# version: "1.0"

name: "TimeEntry"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/TimeEntry.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "varies"
    description: ""

  - name: "approvalStatus"
    type: "varies"
    description: ""

  - name: "billingClass"
    type: "string"
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

  - name: "customer"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "hours"
    type: "varies"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isBillable"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
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

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "timeType"
    type: "varies"
    description: ""
---
