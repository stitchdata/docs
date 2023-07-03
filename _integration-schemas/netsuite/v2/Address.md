---
tap: "netsuite"
version: "2"
name: Address
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Address.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Address
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: addr3
  type: string
  description: ""
- name: addr1
  type: string
  description: ""
- name: addrPhone
  type: string
  description: ""
- name: addressee
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: city
  type: string
  description: ""
- name: state
  type: string
  description: ""
- name: addrText
  type: string
  description: ""
- name: zip
  type: string
  description: ""
- name: addr2
  type: string
  description: ""
- name: attention
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: override
  type: boolean, string
  description: ""
- name: country
  type: varies
  description: ""
---