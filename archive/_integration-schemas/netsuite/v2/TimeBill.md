---
tap: "netsuite"
version: "2"
name: TimeBill
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TimeBill.html
description: |
  The `{{ table.name }}` table contains info about the time transactions in your {{ integration.display_name }} account. Also known as time bills, these transactions records the hours worked by an employee. This transaction can be used to record billable hours and invoice customers.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "time-bill"
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModified
attributes:
- name: department
  type: varies
  description: ""
- name: supervisorApproval
  type: boolean, string
  description: ""
- name: payrollItem
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: timeModified
  type: boolean, string
  description: ""
- name: temporaryStateJurisdiction
  type: varies
  description: ""
- name: temporaryLocalJurisdiction
  type: varies
  description: ""
- name: caseTaskEvent
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: subsidiary
  type: varies
  description: ""
- name: rate
  type: string, number
  description: ""
- name: employee
  type: varies
  description: ""
- name: customer
  type: varies
  description: ""
- name: approvalStatus
  type: varies
  description: ""
- name: isBillable
  type: boolean, string
  description: ""
- name: timeSheet
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: overrideRate
  type: boolean, string
  description: ""
- name: timeType
  type: varies
  description: ""
- name: hours
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: tranDate
  type: string
  description: ""
- name: paidExternally
  type: boolean, string
  description: ""
- name: rejectionNote
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: price
  type: varies
  description: ""
- name: workplace
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
---