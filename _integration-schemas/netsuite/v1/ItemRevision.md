---
tap: "netsuite"
version: "1"

name: "ItemRevision"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/itemrevision.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemRevision.json"
description: |
  The `{{ table.name }}` table contains info about item revisions in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-revision"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "item-revision-id"

  - name: "effectiveDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "inactive"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "obsoleteDate"
    type: "date-time"
    description: ""
---