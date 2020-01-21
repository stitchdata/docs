---
tap: "deputy"
version: "1"
key: "roster-swap"

name: "roster_swaps"
doc-link: "https://www.deputy.com/api-doc/Resources/RosterSwap"

description: |
  The `{{ table.name }}` table contains info about roster swaps.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The roster swap ID."
    #foreign-key-id: "roster-swap-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the roster swap was last modified."

  - name: "SourceRoster"
    type: "integer"
    description: ""
    foreign-key-id: "roster-id"

  - name: "TargetRoster"
    type: "integer"
    description: ""
    foreign-key-id: "roster-id"

  - name: "Employee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Status"
    type: "integer"
    description: ""

  - name: "RequestMessage"
    type: "string"
    description: ""

  - name: "ResponseMessage"
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