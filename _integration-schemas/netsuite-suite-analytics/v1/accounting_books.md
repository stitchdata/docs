---
tap: "netsuite-suite-analytics"
version: "1"
key: "accounting-book"

name: "accounting_books"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/accountingbook.html"
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

  - name: "accounting_book_extid"
    type: "string"
    description: ""

  - name: "accounting_book_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "accounting_book_name"
    type: "string"
    description: ""

  - name: "base_book_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-book-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "effective_period_id"
    type: "integer"
    description: ""

  - name: "form_template_component_id"
    type: "string"
    description: ""

  - name: "form_template_id"
    type: "integer"
    description: ""

  - name: "is_adjustment_only"
    type: "string"
    description: ""

  - name: "is_arrangement_level_reclass"
    type: "string"
    description: ""

  - name: "is_consolidated"
    type: "string"
    description: ""

  - name: "is_contingent_revenue_handling"
    type: "string"
    description: ""

  - name: "is_include_child_subsidiaries"
    type: "string"
    description: ""

  - name: "is_primary"
    type: "string"
    description: ""

  - name: "is_two_step_revenue_allocation"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "unbilled_receivable_grouping"
    type: "string"
    description: ""
---