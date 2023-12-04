---
tap: "zoom"
version: "1"
key: "report-meeting"

name: "report_meetings"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportmeetingdetails"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/report_meetings.json"
description: |
  The `{{ table.name }}` table contains detailed reports about past {{ integration.display_name }} meetings.

replication-method: "Full Table"

api-method:
  name: "Get meeting reports"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportmeetingdetails"

attributes:
  - name: "uuid"
    type: "string"
    primary-key: true
    description: "The report UUID."
    
  - name: "dept"
    type: "integer"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "end_time"
    type: "date-time"
    description: ""

  - name: "id"
    type: "integer"
    description: ""

  - name: "meeting_id"
    type: "string"
    description: "The meeting ID."
    foreign-key-id: "meeting-id"

  - name: "participants_count"
    type: "integer"
    description: ""

  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "topic"
    type: "string"
    description: ""

  - name: "total_minutes"
    type: "integer"
    description: ""

  - name: "tracking_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "field"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "type"
    type: "integer"
    description: ""

  - name: "user_email"
    type: "string"
    description: ""

  - name: "user_name"
    type: "string"
    description: ""
---