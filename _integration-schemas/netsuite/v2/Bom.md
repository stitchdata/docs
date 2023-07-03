---
tap: "netsuite"
version: "2"
name: Bom
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Bom.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Bom
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: legacyBomForAssembly
  type: varies
  description: ""
- name: restrictToLocationsList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: availableForAllLocations
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
- name: usedOnAssembly
  type: boolean, string
  description: ""
- name: restrictToAssembliesList
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: subsidiaryList
  type: varies
  description: ""
- name: useComponentYield
  type: boolean, string
  description: ""
- name: memo
  type: string
  description: ""
- name: availableForAllAssemblies
  type: boolean, string
  description: ""
