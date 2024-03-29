---
tap: "netsuite"
version: "2"
name: Bom
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Bom.html
description:  |
  The `{{ table.name }}` table contains info about bills of materials (BOM): the quantities of raw materials, assemblies, sub-components, and parts needed to manufacture a product.

  {{ integration.permission-for-table | flatify }}

replication-method: "Full Table"
table-key-properties: internalId
key: bom

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
---