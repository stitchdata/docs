---
tap: "netsuite"
version: "2"
name: PayrollItem
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PayrollItem.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/PayrollItem
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: inactive
  type: boolean, string
  description: ""
- name: vendor
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: itemType
  type: varies
  description: ""
- name: accountCategory
  type: varies
  description: ""
- name: liabilityAccount
  type: varies
  description: ""
- name: expenseAccount
  type: varies
  description: ""
- name: employeePaid
  type: boolean, string
  description: ""
---