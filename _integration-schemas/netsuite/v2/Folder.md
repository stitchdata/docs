---
tap: "netsuite"
version: "2"
name: Folder
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Folder.html
description: |
  The `{{ table.name }}` table contains info about the folders in your {{ integration.display_name }} File Cabinet.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "folder"

replication-method: "Key-based Incremental"
attributes:
- name: description
  type: string
  description: ""
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: bundleable
  type: boolean, string
  description: ""
- name: group
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: folderType
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: hideInBundle
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: isPrivate
  type: boolean, string
  description: ""
- name: location
  type: varies
  description: ""
---