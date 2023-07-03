---
tap: "netsuite"
version: "2"
name: ExpenseCategory
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ExpenseCategory.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ExpenseCategory
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: ratesList
  type: varies
  description: ""
- name: rateRequired
  type: boolean, string
  description: ""
- name: name
  type: string
  description: ""
- name: defaultRate
  type: string, number
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: expenseAcct
  type: varies
  description: ""
- name: isInactive
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
- name: translationsList
  type: varies
  description: ""
- name: subsidiaryList
  type: varies
  description: ""
---