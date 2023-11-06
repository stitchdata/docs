---
tap: "netsuite"
version: "2"
name: ManufacturingOperationTask
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingOperationTask.html
description: |
  The `{{ table.name }}` table contains info about manufacturing operation tasks in your {{ integration.display_name }} account.

  After a WIP work order that has a designated routing is saved in {{ integration.display_name }}, manufacturing operation tasks are created based on the routing. Each of these tasks is a step that must be done in order for the assembly process to be finished.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "manufacturing-operation-task"

replication-method: "Full Table"

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: estimatedWork
  type: string, number
  description: ""
- name: laborResources
  type: string, number
  description: ""
- name: predecessorList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: costDetailList
  type: varies
  description: ""
- name: title
  type: string
  description: ""
- name: manufacturingCostTemplate
  type: varies
  description: ""
- name: actualWork
  type: string, number
  description: ""
- name: endDate
  type: string
  description: ""
- name: autoCalculateLag
  type: boolean, string
  description: ""
- name: workOrder
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: remainingWork
  type: string, number
  description: ""
- name: completedQuantity
  type: string, number
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: inputQuantity
  type: string, number
  description: ""
- name: machineResources
  type: string, number
  description: ""
- name: order
  type: varies
  description: ""
- name: runRate
  type: string, number
  description: ""
- name: setupTime
  type: string, number
  description: ""
- name: manufacturingWorkCenter
  type: varies
  description: ""
- name: operationSequence
  type: string, integer
  description: ""
- name: message
  type: string
  description: ""
---