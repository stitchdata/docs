---
tap: "deputy"
version: "1.0"
key: "state"

name: "states"
doc-link: "https://www.deputy.com/api-doc/Resources/State"

description: |
  The `{{ table.name }}` table contains info about states.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The state ID."
    #foreign-key-id: "state-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the state was last modified."

  - name: "Country"
    type: "integer"
    description: ""
    foreign-key-id: "country-id"

  - name: "Code"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "State"
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