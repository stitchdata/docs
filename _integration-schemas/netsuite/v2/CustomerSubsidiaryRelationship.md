---
tap: "netsuite"
version: "2"
name: CustomerSubsidiaryRelationship
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerSubsidiaryRelationship.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/CustomerSubsidiaryRelationship
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: externalId
  type: string
  description: ""
- name: entity
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: isPrimarySub
  type: boolean, string
  description: ""
- name: primaryCurrency
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---