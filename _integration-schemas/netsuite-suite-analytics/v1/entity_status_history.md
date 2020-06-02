---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity-status-history"

name: "entity_status_history"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entity_status_history.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "comment_0"
    type: "string"
    description: ""

  - name: "date_0"
    type: "date-time"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "entity_status_new_id"
    type: "integer"
    description: ""

  - name: "entity_status_old_id"
    type: "integer"
    description: ""
---