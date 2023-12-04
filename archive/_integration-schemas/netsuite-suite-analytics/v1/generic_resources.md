---
tap: "netsuite-suite-analytics"
version: "1"
key: "generic-resource"

name: "generic_resources"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/genericresource.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "billing_class_id"
    type: "integer"
    description: ""

  - name: "generic_resource_extid"
    type: "string"
    description: ""

  - name: "generic_resource_id"
    type: "integer"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "labor_cost"
    type: "integer"
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

  - name: "price"
    type: "integer"
    description: ""

  - name: "resource_name"
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

  - name: "workcalendar_id"
    type: "integer"
    description: ""
---