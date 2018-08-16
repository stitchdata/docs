---
tap: "xero"
version: "1.0"

name: "employees"
doc-link: &api-doc https://developer.xero.com/documentation/api/employees
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/employees.json
description: |
  The `{{ table.name }}` table contains info about employees.

  **Note**: According to [Xero's documentation](https://developer.xero.com/documentation/api/employees), the endpoint that produces this table is:

  > Used for an [employee type](https://help.xero.com/int/Contacts_EmployeeAdd) used exclusively by the global Payrun functionality in Xero core accounting.

  As a result, this table may not contain all employee data. Refer to the `contacts` table if you believe you are missing records.

replication-method: "Key-based Incremental"

api-method:
  name: getEmployees
  doc-link: *api-doc

attributes:
  - name: "EmployeeID"
    type: "string"
    primary-key: true
    description: "The employee ID."
    # foreign-key-id: "employee-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the employee was last updated, in UTC."

  - name: "Status"
    type: "string"
    description: |
      The current status of the employee. Possible values are:

      - `ACTIVE`
      - `ARCHIVED`

  - name: "FirstName"
    type: "string"
    description: "The first name of the employee."

  - name: "LastName"
    type: "string"
    description: "The last name of the employee."

  - name: "ExternalLink"
    type: "string"
    description: "A link to an external resource for the employee. For example: An employee record in an external system."
---