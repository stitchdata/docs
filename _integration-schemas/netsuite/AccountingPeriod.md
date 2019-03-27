---
tap: "netsuite"
# version: "1.0"

name: "AccountingPeriod"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/AccountingPeriod.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "allLocked"
    type: "boolean, string"
    description: ""

  - name: "allowNonGLChanges"
    type: "boolean, string"
    description: ""

  - name: "apLocked"
    type: "boolean, string"
    description: ""

  - name: "arLocked"
    type: "boolean, string"
    description: ""

  - name: "closed"
    type: "boolean, string"
    description: ""

  - name: "closedOnDate"
    type: "date-time"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "fiscalCalendar"
    type: "anything"
    description: ""

  - name: "fiscalCalendarsList"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isAdjust"
    type: "boolean, string"
    description: ""

  - name: "isQuarter"
    type: "boolean, string"
    description: ""

  - name: "isYear"
    type: "boolean, string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "parent"
    type: "anything"
    description: ""

  - name: "payrollLocked"
    type: "boolean, string"
    description: ""

  - name: "periodName"
    type: "string"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""
---
