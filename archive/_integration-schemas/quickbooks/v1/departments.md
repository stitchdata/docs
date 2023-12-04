---
tap: "quickbooks"
version: "1"
key: "department"

name: "departments"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/department"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/departments.json"
description: |
  The `{{ table.name }}` table contains info about the departments in your {{ integration.display_name }} instance. **Note**: Both active and inactive departments are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a department"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/department#query-a-department"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The department ID."
    foreign-key-id: "department-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "FullyQualifiedName"
    type: "string"
    description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "ParentRef"
    type: "object"
    description: "If the department is a sub-department, this will contain details about the parent department."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The department ID."
        foreign-key-id: "department-id"

  - name: "SubDepartment"
    type: "boolean"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---