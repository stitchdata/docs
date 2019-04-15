---
tap: "netsuite"
version: "1.0"

name: "AccountingPeriod"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/accountingperiod.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/AccountingPeriod.json"
description: |
  The `{{ table.name }}` table contains info about the accounting periods in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Setup"
  name: "Manage Accounting Periods"

feature-requirements:
  - tab: "Accounting"
    name: "Accounting Periods"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "accounting-period-id"

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
    type: "varies"
    description: ""

  - name: "fiscalCalendarsList"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
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