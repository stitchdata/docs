---
tap: "deputy"
version: "1.0"
key: "public-holiday"

name: "public_holidays"
doc-link: "https://www.deputy.com/api-doc/Resources/PublicHoliday"

description: |
  The `{{ table.name }}` table contains info about public holidays.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The public holiday ID."
    #foreign-key-id: "public-holiday-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the public holiday was last modified."

  - name: "Title"
    type: "string"
    description: ""

  - name: "Schedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---