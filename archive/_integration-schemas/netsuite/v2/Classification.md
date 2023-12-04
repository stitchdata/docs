---
tap: "netsuite"
version: "2"
name: Classification
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Classification.html
description: |
  The `{{ table.name }}` table contains info about the classifications in your {{ integration.display_name }} account.

  As classifications inherit the permissions set on the parent record, the permissions required for the parent record are required to access classification data.

  For example: To get classification data for a location, the user must have the permission for accessing location data.

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "classification"

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