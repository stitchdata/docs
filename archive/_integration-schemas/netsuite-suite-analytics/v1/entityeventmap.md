---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity-event-map"

name: "entityeventmap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entityeventmap.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "attendee_status_id"
    type: "string"
    description: ""
  - name: "entity_id"
    type: "integer"
    description: ""
  - name: "event_id"
    type: "integer"
    description: ""
  - name: "resource_id"
    type: "integer"
    description: ""
  - name: "status_id"
    type: "string"
    description: ""
---