---
tap: "netsuite-suite-analytics"
version: "1"
key: "item-account-map"

name: "item_account_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/item_account_map.html"
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

  - name: "accounting_book_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "class_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_effective"
    type: "date-time"
    description: ""

  - name: "date_end"
    type: "date-time"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""
    foreign-key-id: "department-id"

  - name: "destination_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "form_template_component_id"
    type: "string"
    description: ""

  - name: "form_template_id"
    type: "integer"
    description: ""

  - name: "is_class_any"
    type: "string"
    description: ""

  - name: "is_department_any"
    type: "string"
    description: ""

  - name: "is_location_any"
    type: "string"
    description: ""

  - name: "item_account_map_extid"
    type: "string"
    description: ""

  - name: "item_account_map_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "item_account_type"
    type: "string"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "source_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"
---