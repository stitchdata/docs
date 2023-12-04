---
tap: "netsuite-suite-analytics"
version: "1"
key: "deleted-record"

name: "deleted_records"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/deletedrecord.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_deleted"
    type: "date-time"
    replication-key: true
    description: |
      The time the record was deleted.
  - name: "custom_record_type"
    type: "string"
    description: ""
  - name: "entity_id"
    type: "integer"
    description: ""
  - name: "entity_name"
    type: "string"
    description: ""
  - name: "is_custom_list"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "record_base_type"
    type: "string"
    description: ""
  - name: "record_id"
    type: "integer"
    description: ""
  - name: "record_type_name"
    type: "string"
    description: ""
---