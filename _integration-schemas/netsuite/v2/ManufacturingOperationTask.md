---
tap: "netsuite"
version: "2"
name: ManufacturingOperationTask
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingOperationTask.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ManufacturingOperationTask
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
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