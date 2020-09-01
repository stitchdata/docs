---
tap: "square"
version: "1"
key: ""

name: "employees"
doc-link: "https://developer.squareup.com/reference/square/employees-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/employees.json"
description: |
  The `{{ table.name }}` table contains information about your employees in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "List employees"
    doc-link: "https://developer.squareup.com/reference/square/employees-api/v1-list-employees"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The employee ID."
    foreign-key-id: "employee-id"

  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  - name: "first_name"
    type: "string"
    description: ""
  
  - name: "is_owner"
    type: "boolean"
    description: ""
  - name: "last_name"
    type: "string"
    description: ""
  - name: "location_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: "The location IDs of the employee."
        foreign-key-id: "location-id"
  - name: "status"
    type: "string"
    description: ""
  - name: "updated_at"
    type: "date-time"
    description: ""
---
