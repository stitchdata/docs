---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity"

name: "entity"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entity.html"
description: |
  {{ integration.netsuite-replication-keys | flatify }}

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

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "address_one"
    type: "string"
    description: ""

  - name: "address_three"
    type: "string"
    description: ""

  - name: "address_two"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "entity_extid"
    type: "string"
    description: ""

  - name: "entity_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "entity-id"

  - name: "entity_type"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "global_subscription_status"
    type: "integer"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_online_bill_pay"
    type: "string"
    description: ""

  - name: "is_unavailable"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "login_access"
    type: "string"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "middle_name"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "originator_id"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "salutation"
    type: "string"
    description: ""

  - name: "state"
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

  - name: "subsidiary"
    type: "integer"
    description: ""

  - name: "unsubscribed"
    type: "string"
    description: ""

  - name: "zipcode"
    type: "string"
    description: ""
---