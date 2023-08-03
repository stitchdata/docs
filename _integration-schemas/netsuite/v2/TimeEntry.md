---
tap: "netsuite"
version: "2"
name: TimeEntry
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TimeEntry.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/TimeEntry
description: |
  The `{{ table.name }}` table contains info about the time entries in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "time-entry"
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModified
attributes:
- name: department
  type: varies
  description: ""
- name: payrollItem
  type: varies
  description: ""
- name: nullFieldList
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
- name: customer
  type: varies
  description: ""
- name: approvalStatus
  type: varies
  description: ""
- name: isBillable
  type: boolean, string
  description: ""
- name: billingClass
  type: string
  description: ""
- name: externalId
  type: string
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
- name: paidExternally
  type: boolean, string
  description: ""
- name: location
  type: varies
  description: ""
- name: price
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
---