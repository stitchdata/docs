---
tap: "netsuite"
version: "2"
name: VendorSubsidiaryRelationship
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/VendorSubsidiaryRelationship.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/VendorSubsidiaryRelationship
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: primaryCurrency
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: creditLimit
  type: string, number
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: baseCurrency
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: isPrimarySub
  type: boolean, string
  description: ""
- name: entity
  type: varies
  description: ""
- name: taxItem
  type: varies
  description: ""
