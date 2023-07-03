---
tap: "netsuite"
version: "2"
name: SalesRole
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SalesRole.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/SalesRole
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
- name: name
  type: string
  description: ""
- name: description
  type: string
  description: ""
- name: isSalesRep
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
