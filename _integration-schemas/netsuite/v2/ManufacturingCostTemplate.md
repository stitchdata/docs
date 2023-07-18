---
tap: "netsuite"
version: "2"
name: ManufacturingCostTemplate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ManufacturingCostTemplate.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ManufacturingCostTemplate
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: costDetailList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
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
- name: memo
  type: string
  description: ""
---