---
tap: "deputy"
version: "1.0"
key: "employee-role"

name: "employee_roles"
doc-link: "https://www.deputy.com/api-doc/Resources/EmployeeRole"

description: |
  The `{{ table.name }}` table contains info about employee roles.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employee role ID."
    foreign-key-id: "employee-role-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employee role was last modified."

  - name: "Role"
    type: "string"
    description: ""

  - name: "Ranking"
    type: "integer"
    description: ""

  - name: "ReportTo"
    type: "integer"
    description: ""

  - name: "Permissions"
    type: "string"
    description: ""

  - name: "Require2fa"
    type: "boolean"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---