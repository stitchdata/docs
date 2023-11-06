---
tap: "netsuite"
version: "2"
name: Deleted
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Deleted.html
description: |
  The `{{ table.name }}` table contains info about deleted records.

  {{ integration.permission-for-table | flatify }}

  #### Objects with delete support

  According to [{{ integration.display_name }}'s documentation](https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html){:target="new"}, only certain objects support the `{{ table.api-method.name }}` operation Stitch uses to retrieve deleted record data from the SuiteTalk API.

  Refer to the [Deleted records](#deleted-records) section for more info and a list of record types with delete support.

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "deleted"

replication-method: "Key-based Incremental"

api-method:
    name: "getDeleted"
    doc-link: "https://system.netsuite.com/app/help/helpcenter.nl?fid=section_N3497592.html"

attributes:
- name: deletedDate
  type: string
  description: ""
  replication-key: true
- name: name
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: externalId
  type: string
  description: ""
- name: type
  type: string
  description: ""
  primary-key: true
- name: scriptId
  type: string
  description: ""
- name: customRecord
  type: boolean
  description: ""
---