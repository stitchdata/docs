---
tap: "netsuite-suite-analytics"
version: "1"
key: "support-rep"

name: "support_reps"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/support_reps.html"
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

  - name: "account_number"
    type: "string"
    description: ""

  - name: "address"
    type: "string"
    description: ""

  - name: "address1"
    type: "string"
    description: ""

  - name: "address2"
    type: "string"
    description: ""

  - name: "address3"
    type: "string"
    description: ""

  - name: "approval_limit"
    type: "number"
    description: ""

  - name: "approver_id"
    type: "integer"
    description: ""

  - name: "birthdate"
    type: "date-time"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "def_acct_corp_card_expenses_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "def_expense_report_currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "department_id"
    type: "integer"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "employee_type_id"
    type: "integer"
    description: ""

  - name: "firstname"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "identification_number"
    type: "string"
    description: ""

  - name: "initials"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "lastname"
    type: "string"
    description: ""

  - name: "loginaccess"
    type: "string"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "midname"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
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

  - name: "subsidiary_id"
    type: "integer"
    description: ""

  - name: "supervisor_id"
    type: "integer"
    description: ""

  - name: "support_rep_extid"
    type: "string"
    description: ""

  - name: "support_rep_id"
    type: "integer"
    description: ""

  - name: "zipcode"
    type: "string"
    description: ""
---