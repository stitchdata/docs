---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity-status"

name: "entity_status"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entity_status.html"
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

  - name: "description"
    type: "string"
    description: ""

  - name: "entity_status_extid"
    type: "string"
    description: ""

  - name: "entity_status_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "probability"
    type: "number"
    description: ""

  - name: "read_only"
    type: "string"
    description: ""

  - name: "type_0"
    type: "string"
    description: ""
---