---
tap: "netsuite"
version: "2"
name: Bin
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Bin.html
description: |
  The `{{ table.name }}` table contains info about bins, or places in your warehouse where you store inventory items.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "bin"

replication-method: "Full Table"

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
---