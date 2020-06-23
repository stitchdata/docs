---
tap: "netsuite-suite-analytics"
version: "1"
key: "support-case-history"

name: "supportcasehistory"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/supportcasehistory.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "case_id"
    type: "integer"
    description: ""

  - name: "date_closed"
    type: "date-time"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "employee_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"
---