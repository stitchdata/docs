---
tap: "quickbooks"
version: "1"
key: "class"

name: "classes"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/class"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/classes.json"
description: |
  The `{{ table.name }}` table contains info about the classes set up in your {{ integration.display_name }} instance. **Note**: Both active and inactive classes are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a class"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/class#query-a-class"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The class ID."
    foreign-key-id: "class-id"

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

  - name: "ParentRef"
    type: "object"
    description: "Details about the parent class associated with the class."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The parent class ID."
        foreign-key-id: "class-id"

  - name: "Name"
    type: "string"
    description: ""

  - name: "SubClass"
    type: "boolean"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---