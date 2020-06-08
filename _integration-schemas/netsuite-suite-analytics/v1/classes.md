---
tap: "netsuite-suite-analytics"
version: "1"
key: "class"

name: "classes"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/classes.html"
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

  - name: "class_extid"
    type: "string"
    description: ""

  - name: "class_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "class-id"

  - name: "full_name"
    type: "string"
    description: ""

  - name: "is_including_child_subs"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"
---