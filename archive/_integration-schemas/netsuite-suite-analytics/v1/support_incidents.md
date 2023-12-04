---
tap: "netsuite-suite-analytics"
version: "1"
key: "support-incident"

name: "support_incidents"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/support_incidents.html"
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

  - name: "assigned_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "case_email"
    type: "string"
    description: ""

  - name: "case_extid"
    type: "string"
    description: ""

  - name: "case_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "case-id"

  - name: "case_issue_id"
    type: "integer"
    description: ""
    foreign-key-id: "case-issue-id"

  - name: "case_number"
    type: "integer"
    description: ""

  - name: "case_numbercode"
    type: "string"
    description: ""

  - name: "case_origin_id"
    type: "integer"
    description: ""
    foreign-key-id: "case-origin-id"

  - name: "case_phone"
    type: "string"
    description: ""

  - name: "case_profile_id"
    type: "integer"
    description: ""

  - name: "case_stage"
    type: "string"
    description: ""

  - name: "case_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "case-type-id"

  - name: "comments"
    type: "string"
    description: ""

  - name: "company_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "contact_id"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "date_closed"
    type: "date-time"
    description: ""

  - name: "entry_time"
    type: "date-time"
    description: ""

  - name: "helpdesk"
    type: "string"
    description: ""

  - name: "inboundemail"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "last_modification"
    type: "date-time"
    description: ""

  - name: "last_reopened_date"
    type: "date-time"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "module_name"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "priority"
    type: "string"
    description: ""

  - name: "product"
    type: "string"
    description: ""

  - name: "stage"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "stitch_custom_field"
    type: "number"
    description: ""

  - name: "stitch_custom_field_check_box"
    type: "string"
    description: ""

  - name: "stitch_custom_field_currency"
    type: "number"
    description: ""

  - name: "stitch_custom_field_decimal"
    type: "number"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "territory_id"
    type: "integer"
    description: ""
    foreign-key-id: "territory-id"
---