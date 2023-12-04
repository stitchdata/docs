---
tap: "netsuite"
version: "2"
name: Note
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Note.html
replication-method: "Full Table"
description: |
  The `{{ table.name }}` table contains info about the notes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "note"

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: noteDate
  type: string
  description: ""
- name: folder
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: transaction
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
- name: topic
  type: varies
  description: ""
- name: title
  type: string
  description: ""
- name: note
  type: string
  description: ""
- name: author
  type: varies
  description: ""
- name: activity
  type: varies
  description: ""
- name: noteType
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: record
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: recordType
  type: varies
  description: ""
- name: entity
  type: varies
  description: ""
- name: media
  type: varies
  description: ""
- name: direction
  type: varies
  description: ""
---