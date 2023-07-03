---
tap: "netsuite"
version: "2"
name: ItemDemandPlan
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemDemandPlan.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ItemDemandPlan
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: month
  type: varies
  description: ""
- name: demandPlanCalendarType
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: year
  type: string, integer
  description: ""
- name: endDate
  type: string
  description: ""
- name: demandPlanMatrix
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
- name: units
  type: varies
  description: ""
- name: location
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
