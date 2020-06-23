---
tap: "netsuite-suite-analytics"
version: "1"
key: "case-escalation-history"

name: "caseescalationhistory"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/caseescalationhistory.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "case_id"
    type: "integer"
    description: ""
    foreign-key-id: "case-id"

  - name: "entity_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "escalation_action"
    type: "string"
    description: ""

  - name: "escalation_date"
    type: "date-time"
    description: ""

  - name: "escalator_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "message"
    type: "string"
    description: ""
---