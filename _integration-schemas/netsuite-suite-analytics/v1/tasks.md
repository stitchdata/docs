---
tap: "netsuite-suite-analytics"
version: "1"
key: "task"

name: "tasks"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/task.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "assigned_id"
    type: "integer"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "due_date"
    type: "date-time"
    description: ""

  - name: "estimated_hours"
    type: "number"
    description: ""

  - name: "estimated_hours_override"
    type: "number"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "priority"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "task_extid"
    type: "string"
    description: ""

  - name: "task_id"
    type: "integer"
    description: ""

  - name: "taskorder"
    type: "integer"
    description: ""
---