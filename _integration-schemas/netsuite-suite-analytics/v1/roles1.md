---
tap: "netsuite-suite-analytics"
version: "1"
key: "role"

name: "roles1"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/role.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "center_created_by"
    type: "integer"
    description: ""

  - name: "center_created_date"
    type: "date-time"
    description: ""

  - name: "center_id"
    type: "string"
    description: ""

  - name: "center_modified_by"
    type: "integer"
    description: ""

  - name: "center_modified_date"
    type: "date-time"
    description: ""

  - name: "center_name"
    type: "string"
    description: ""

  - name: "class_restriction_type"
    type: "string"
    description: ""

  - name: "custom_record_permission_name"
    type: "string"
    description: ""

  - name: "department_restriction_type"
    type: "string"
    description: ""

  - name: "employee_restriction_type"
    type: "string"
    description: ""

  - name: "is_classallowviewing"
    type: "string"
    description: ""

  - name: "is_departmentallowviewing"
    type: "string"
    description: ""

  - name: "is_employeeallowviewing"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_itemclassrestricted"
    type: "string"
    description: ""

  - name: "is_itemdepartmentrestricted"
    type: "string"
    description: ""

  - name: "is_itemlocationtrestricted"
    type: "string"
    description: ""

  - name: "is_locationallowviewing"
    type: "string"
    description: ""

  - name: "is_subsidiaryallowviewing"
    type: "string"
    description: ""

  - name: "location_restriction_type"
    type: "string"
    description: ""

  - name: "permission_id"
    type: "string"
    description: ""

  - name: "permission_level_id"
    type: "integer"
    description: ""

  - name: "permission_level_name"
    type: "string"
    description: ""

  - name: "permission_name"
    type: "string"
    description: ""

  - name: "permsofroles_date_modified"
    type: "date-time"
    description: ""

  - name: "permsofroles_modified_by"
    type: "integer"
    description: ""

  - name: "role_created_by"
    type: "integer"
    description: ""

  - name: "role_created_date"
    type: "date-time"
    description: ""

  - name: "role_id"
    type: "integer"
    description: ""

  - name: "role_modified_by"
    type: "integer"
    description: ""

  - name: "role_name"
    type: "string"
    description: ""
---