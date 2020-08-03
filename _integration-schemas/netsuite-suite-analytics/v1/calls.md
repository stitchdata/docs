---
tap: "netsuite-suite-analytics"
version: "1"
key: "call"

name: "calls"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/calls.html"
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

  - name: "call_date"
    type: "date-time"
    description: ""

  - name: "call_extid"
    type: "string"
    description: ""

  - name: "call_id"
    type: "integer"
    description: ""

  - name: "case_id"
    type: "integer"
    description: ""

  - name: "company_id"
    type: "integer"
    description: ""

  - name: "date_completed"
    type: "date-time"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "opportunity_id"
    type: "integer"
    description: ""

  - name: "organizer_id"
    type: "integer"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subject"
    type: "string"
    description: ""
---