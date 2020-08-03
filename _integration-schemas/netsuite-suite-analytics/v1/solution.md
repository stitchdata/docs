---
tap: "netsuite-suite-analytics"
version: "1"
key: "solution"

name: "solution"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/solution.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "id_0"
    type: "string"
    description: ""

  - name: "is_available_online"
    type: "string"
    description: ""

  - name: "long_description"
    type: "string"
    description: ""

  - name: "solution_extid"
    type: "string"
    description: ""

  - name: "solution_id"
    type: "integer"
    description: ""
---