---
tap: "netsuite"
version: "2"
name: ResourceAllocation
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ResourceAllocation.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ResourceAllocation
description: |
  The `{{ table.name }}` table contains info about resource allocations, or employee time reservations, in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "resource-allocation"

replication-method: "Full Table"

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: nextApprover
  type: varies
  description: ""
- name: allocationUnit
  type: varies
  description: ""
- name: numberHours
  type: string, number
  description: ""
- name: allocationType
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: allocationResource
  type: varies
  description: ""
- name: requestedby
  type: varies
  description: ""
- name: allocationAmount
  type: string, number
  description: ""
- name: approvalStatus
  type: varies
  description: ""
- name: endDate
  type: string
  description: ""
- name: project
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: notes
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: percentOfTime
  type: string, number
  description: ""
---