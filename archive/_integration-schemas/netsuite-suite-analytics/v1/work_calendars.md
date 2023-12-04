---
tap: "netsuite-suite-analytics"
version: "1"
key: "work-calendar"

name: "work_calendars"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/work_calendars.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "isdefault"
    type: "string"
    description: ""

  - name: "isfriday"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "ismonday"
    type: "string"
    description: ""

  - name: "issaturday"
    type: "string"
    description: ""

  - name: "issunday"
    type: "string"
    description: ""

  - name: "isthursday"
    type: "string"
    description: ""

  - name: "istuesday"
    type: "string"
    description: ""

  - name: "iswednesday"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "start_hour"
    type: "date-time"
    description: ""

  - name: "work_calendar_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "work-calendar-id"

  - name: "work_hours_per_day"
    type: "integer"
    description: ""
---