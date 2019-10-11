---
tap: "deputy"
version: "1.0"
key: "roster-open"

name: "roster_opens"
doc-link: "https://www.deputy.com/api-doc/Resources/RosterOpen"

description: |
  The `{{ table.name }}` table contains info about roster opens.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The roster open ID."
    #foreign-key-id: "roster-open-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the roster open was last modified."

  - name: "Roster"
    type: "integer"
    description: ""
    foreign-key-id: "roster-id"

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Accepted"
    type: "boolean"
    description: ""

  - name: "Seen"
    type: "boolean"
    description: ""

  - name: "Declined"
    type: "boolean"
    description: ""

  - name: "Link"
    type: "string"
    description: ""

  - name: "Message"
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