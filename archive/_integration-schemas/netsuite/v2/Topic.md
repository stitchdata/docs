---
tap: "netsuite"
version: "2"
name: Topic
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Topic.html
description: |
  The `{{ table.name }}` table contains info about the topics used to organize knowledge base solutions in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "topic"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: title
  type: string
  description: ""
- name: parentTopic
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: longDescription
  type: string
  description: ""
- name: solutionList
  type: varies
  description: ""
---