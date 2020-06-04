---
tap: "netsuite-suite-analytics"
version: "1"
key: "case-stage-change"

name: "case_stage_changes"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/case_stage_changes.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "case_id"
    type: "integer"
    description: ""
    foreign-key-id: "case-id"

  - name: "casestage"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""
---