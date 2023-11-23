---
tap: "netsuite"
version: "2"
name: File
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/File.html
description: |
  The `{{ table.name }}` table contains info about the files in your {{ integration.display_name }} File Cabinet.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "file"

replication-method: "Key-based Incremental"
attributes:
- name: attachFrom
  type: varies
  description: ""
- name: description
  type: string
  description: ""
- name: encoding
  type: varies
  description: ""
- name: fileSize
  type: string, number
  description: ""
- name: department
  type: string
  description: ""
- name: caption
  type: string
  description: ""
- name: textFileEncoding
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: bundleable
  type: boolean, string
  description: ""
- name: featuredDescription
  type: string
  description: ""
- name: mediaTypeName
  type: string
  description: ""
- name: siteDescription
  type: string
  description: ""
- name: fileType
  type: varies
  description: ""
- name: content
  type: string
  description: ""
- name: folder
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: mediaFile
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
- name: urlComponent
  type: string
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: storeDisplayThumbnail
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: _class
  type: string
  description: ""
- name: hideInBundle
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: url
  type: string
  description: ""
- name: createdDate
  type: string
  description: ""
- name: isPrivate
  type: boolean, string
  description: ""
- name: owner
  type: varies
  description: ""
- name: altTagCaption
  type: string
  description: ""
- name: siteCategoryList
  type: varies
  description: ""
---