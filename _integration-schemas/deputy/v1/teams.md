---
tap: "deputy"
version: "1.0"
key: "team"

name: "teams"
doc-link: "https://www.deputy.com/api-doc/Resources/Team"

description: |
  The `{{ table.name }}` table contains info about teams.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The team ID."
    #foreign-key-id: "team-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the team was last modified."

  - name: "LeaderEmployee"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Name"
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