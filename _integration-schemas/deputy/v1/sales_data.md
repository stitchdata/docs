---
tap: "deputy"
version: "1.0"
key: "sale-data"

name: "sales_data"
doc-link: "https://www.deputy.com/api-doc/Resources/SalesData"

description: |
  The `{{ table.name }}` table contains info about sales data.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The sale data ID."
    #foreign-key-id: "sale-data-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the sale data was last modified."

  - name: "Date"
    type: "date"
    description: ""

  - name: "Timestamp"
    type: "integer"
    description: ""

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "OperationalUnit"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "SalesRef"
    type: "string"
    description: ""

  - name: "SalesQty"
    type: "number"
    description: ""

  - name: "SalesAmount"
    type: "number"
    description: ""

  - name: "SalesPayload"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---