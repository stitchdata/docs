---
tap: "netsuite"
version: "2"
name: ManufacturingRouting
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingRouting.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ManufacturingRouting
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: isDefault
  type: boolean, string
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: autoCalculateLag
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: routingStepList
  type: varies
  description: ""
- name: routingComponentList
  type: varies
  description: ""
- name: billOfMaterials
  type: varies
  description: ""
- name: locationList
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
---