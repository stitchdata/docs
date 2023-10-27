---
tap: "netsuite"
version: "2"
name: Department
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Department.html
description: |
  The `{{ table.name }}` table contains info about the departments in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "department"

replication-method: "Full Table"

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: parent
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
- name: classTranslationList
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: subsidiaryList
  type: varies
  description: ""
---