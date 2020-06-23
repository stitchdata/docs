---
tap: "netsuite-suite-analytics"
version: "1"
key: "employee-time"

name: "employee_time"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/employee_time.html"
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

  - name: "approved"
    type: "string"
    description: ""

  - name: "billable"
    type: "string"
    description: ""

  - name: "billed"
    type: "string"
    description: ""

  - name: "billing_class_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-class-id"

  - name: "billing_subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "break_duration"
    type: "number"
    description: ""

  - name: "charge_billing_run_id"
    type: "integer"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"

  - name: "closed"
    type: "date-time"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "day_0"
    type: "date-time"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""
    foreign-key-id: "department-id"

  - name: "duration"
    type: "number"
    description: ""

  - name: "employee_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "employee_time_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "ending"
    type: "date-time"
    description: ""

  - name: "event_id"
    type: "integer"
    description: ""

  - name: "is_outside_project_plan"
    type: "string"
    description: ""

  - name: "is_posted"
    type: "string"
    description: ""

  - name: "is_productive"
    type: "string"
    description: ""

  - name: "is_utilized"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "service-item-id"

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "next_approver_id"
    type: "integer"
    description: ""

  - name: "payroll_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "payroll-item-id"

  - name: "payroll_workplace_id"
    type: "integer"
    description: ""

  - name: "price_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-type-id"

  - name: "rejection_note"
    type: "string"
    description: ""

  - name: "remaining_time_to_charge"
    type: "integer"
    description: ""

  - name: "resource_allocation_id"
    type: "integer"
    description: ""

  - name: "starting"
    type: "date-time"
    description: ""

  - name: "status_code"
    type: "string"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "time_type"
    type: "string"
    description: ""

  - name: "timesheet_id"
    type: "integer"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "transaction_line_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-line-id"

  - name: "unit_cost"
    type: "number"
    description: ""

  - name: "unit_price"
    type: "number"
    description: ""
---