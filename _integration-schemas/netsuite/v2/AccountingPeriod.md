---
tap: netsuite
version: "2"
name: AccountingPeriod
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/AccountingPeriod.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/AccountingPeriod
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: allLocked
  type: boolean, string
  description: ""
- name: isQuarter
  type: boolean, string
  description: ""
- name: closed
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: allowNonGLChanges
  type: boolean, string
  description: ""
- name: startDate
  type: string
  description: ""
- name: payrollLocked
  type: boolean, string
  description: ""
- name: apLocked
  type: boolean, string
  description: ""
- name: endDate
  type: string
  description: ""
- name: fiscalCalendarsList
  type: varies
  description: ""
- name: isYear
  type: boolean, string
  description: ""
- name: isAdjust
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: arLocked
  type: boolean, string
  description: ""
- name: closedOnDate
  type: string
  description: ""
- name: fiscalCalendar
  type: varies
  description: ""
- name: periodName
  type: string
  description: ""
