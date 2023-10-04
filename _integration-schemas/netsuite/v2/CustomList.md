---
tap: "netsuite"
version: "2"
name: CustomList
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomList.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/CustomList
description: |
  The `{{ table.name }}` table contains info about 

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "custom-list"

replication-method: "Full Table"

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
- name: customValueList
  type: varies
  description: ""
- name: isMatrixOption
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: scriptId
  type: string
  description: ""
- name: isOrdered
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: translationsList
  type: varies
  description: ""
- name: convertToCustomRecord
  type: boolean, string
  description: ""
- name: owner
  type: varies
  description: ""
---