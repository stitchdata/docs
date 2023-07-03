---
tap: "netsuite"
version: "2"
name: UnitsType
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/UnitsType.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/UnitsType
description: ""
replication-method: "Full Table"
table-key-properties: internalId

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
- name: isInactive
  type: boolean, string
  description: ""
- name: uomList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---