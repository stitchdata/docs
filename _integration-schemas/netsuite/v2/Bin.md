---
tap: netsuite
version: "2"
name: Bin
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Bin.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Bin
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
- name: binNumber
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
