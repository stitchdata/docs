---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-revision"

name: "item_revisions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/itemrevision.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "effective_date"
    type: "date-time"
    description: ""

  - name: "externalid"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "item_revision_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "item_revision_item"
    type: "integer"
    description: ""

  - name: "item_revision_name"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "obsolete_date"
    type: "date-time"
    description: ""
---