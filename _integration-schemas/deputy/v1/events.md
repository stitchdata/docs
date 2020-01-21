---
tap: "deputy"
version: "1"
key: "event"

name: "events"
doc-link: "https://www.deputy.com/api-doc/Resources/Event"

description: |
  The `{{ table.name }}` table contains info about events.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The event ID."
    #foreign-key-id: "event-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the event was last modified."

  - name: "Title"
    type: "string"
    description: ""

  - name: "Schedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "Colour"
    type: "string"
    description: ""

  - name: "ShowOnRoster"
    type: "boolean"
    description: ""

  - name: "BlockTimeOff"
    type: "boolean"
    description: ""

  - name: "AddToBudget"
    type: "number"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---