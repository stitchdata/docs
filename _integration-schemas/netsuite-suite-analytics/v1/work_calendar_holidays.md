---
tap: "netsuite-suite-analytics"
version: "1"
key: "work-calendar-holiday"

name: "work_calendar_holidays"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/work_calendar_holidays.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_holiday"
    type: "date-time"
    netsuite-primary-key: true
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "work_calendar_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "work-calendar-id"
---