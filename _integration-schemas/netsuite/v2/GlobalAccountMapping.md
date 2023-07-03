---
tap: netsuite
version: "2"
name: GlobalAccountMapping
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/GlobalAccountMapping.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/GlobalAccountMapping
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: accountingBook
  type: varies
  description: ""
- name: customDimension
  type: varies
  description: ""
- name: destinationAccount
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: sourceAccount
  type: varies
  description: ""
- name: effectiveDate
  type: string
  description: ""
- name: subsidiary
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
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: location
  type: varies
  description: ""
