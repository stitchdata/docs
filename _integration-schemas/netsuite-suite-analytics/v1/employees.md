---
tap: "netsuite-suite-analytics"
version: "1"
key: "employee"

name: "employees"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/employee.html"
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

  - name: "accountnumber"
    type: "string"
    description: ""

  - name: "address"
    type: "string"
    description: ""

  - name: "approvallimit"
    type: "number"
    description: ""

  - name: "approver_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "billing_class_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-class-id"

  - name: "birthdate"
    type: "date-time"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"

  - name: "comments"
    type: "string"
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

  - name: "default_job_resource_role_id"
    type: "integer"
    description: ""
    foreign-key-id: "job-resource-role-id"

  - name: "department_id"
    type: "integer"
    description: ""
    foreign-key-id: "department-id"

  - name: "email"
    type: "string"
    description: ""

  - name: "employee_extid"
    type: "string"
    description: ""

  - name: "employee_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "employee-id"

  - name: "employee_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-type-id"

  - name: "firstname"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "gender"
    type: "string"
    description: ""

  - name: "hireddate"
    type: "date-time"
    description: ""

  - name: "home_phone"
    type: "string"
    description: ""

  - name: "initials"
    type: "string"
    description: ""

  - name: "is_in_payroll"
    type: "string"
    description: ""

  - name: "is_job_manager"
    type: "string"
    description: ""

  - name: "is_job_resource"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "issalesrep"
    type: "string"
    description: ""

  - name: "issupportrep"
    type: "string"
    description: ""

  - name: "job_description"
    type: "string"
    description: ""

  - name: "jobtitle"
    type: "string"
    description: ""

  - name: "labor_cost"
    type: "integer"
    description: ""

  - name: "last_modified_date"
    type: "date-time"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "lastname"
    type: "string"
    description: ""

  - name: "lastreviewdate"
    type: "date-time"
    description: ""

  - name: "line1"
    type: "string"
    description: ""

  - name: "line2"
    type: "string"
    description: ""

  - name: "line3"
    type: "string"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "loginaccess"
    type: "string"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "marital_status_id"
    type: "integer"
    description: ""

  - name: "middlename"
    type: "string"
    description: ""

  - name: "mobile_phone"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nextreviewdate"
    type: "date-time"
    description: ""

  - name: "office_phone"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "releasedate"
    type: "date-time"
    description: ""

  - name: "salutation"
    type: "string"
    description: ""

  - name: "socialsecuritynumber"
    type: "string"
    description: ""

  - name: "state"
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

  - name: "supervisor_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "target_utilization"
    type: "number"
    description: ""

  - name: "work_calendar_id"
    type: "integer"
    description: ""
    foreign-key-id: "work-calendar-id"

  - name: "zipcode"
    type: "string"
    description: ""
---