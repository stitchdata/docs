---
tap: "netsuite"
version: "2"
name: TimeSheet
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TimeSheet.html
description: |
  The `{{ table.name }}` table contains info about the time sheets in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "timesheet"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: totalHours
  type: varies
  description: ""
- name: employee
  type: varies
  description: ""
- name: approvalStatus
  type: varies
  description: ""
- name: endDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: timeGridList
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
---