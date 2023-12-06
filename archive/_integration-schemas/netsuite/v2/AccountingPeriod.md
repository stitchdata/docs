---
tap: "netsuite"
version: "2"
name: AccountingPeriod
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/AccountingPeriod.html
description: |
  The `{{ table.name }}` table contains info about the accounting periods in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "accounting-period"

replication-method: "Full Table"

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
---