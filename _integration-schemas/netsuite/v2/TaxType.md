---
tap: "netsuite"
version: "2"
name: TaxType
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TaxType.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/TaxType
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
- name: name
  type: string
  description: ""
- name: nexusAccountsList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: doesNotAddToTotal
  type: boolean, string
  description: ""
- name: nexusesTaxList
  type: varies
  description: ""
- name: postToItemCost
  type: boolean, string
  description: ""
- name: reverseCharge
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: country
  type: varies
  description: ""
- name: taxInNetAmount
  type: boolean, string
  description: ""
