---
tap: "netsuite"
version: "2"
name: FairValuePrice
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/FairValuePrice.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/FairValuePrice
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: lowValuePercent
  type: string, number
  description: ""
- name: highValuePercent
  type: string, number
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: itemRevenueCategory
  type: varies
  description: ""
- name: dimensionList
  type: varies
  description: ""
- name: fairValueRangePolicy
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
- name: isVsoePrice
  type: boolean, string
  description: ""
- name: highValue
  type: string, number
  description: ""
- name: fairValueFormula
  type: varies
  description: ""
- name: fairValue
  type: string, number
  description: ""
- name: currency
  type: varies
  description: ""
- name: endDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: unitsType
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: lowValue
  type: string, number
  description: ""
- name: units
  type: varies
  description: ""
---