---
tap: "netsuite-suite-analytics"
version: "1"
key: "resource-allocation"

name: "resource_allocations"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/resourceallocation.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "allocation_type"
    type: "string"
    description: ""

  - name: "allocation_unit"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "num_hours"
    type: "number"
    description: ""

  - name: "num_percent"
    type: "number"
    description: ""

  - name: "project_id"
    type: "integer"
    description: ""

  - name: "project_task_id"
    type: "integer"
    description: ""

  - name: "requestor_id"
    type: "integer"
    description: ""

  - name: "resource_allocation_extid"
    type: "string"
    description: ""

  - name: "resource_allocation_id"
    type: "integer"
    description: ""

  - name: "resource_id"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""
---