---
tap: "zoom"
version: "1"
key: ""

name: "report_webinars"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportwebinardetails"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/report_webinars.json"
description: |
  The `{{ table.name }}` table contains information about past webinars in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "getWebinarReport"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportwebinardetails"

attributes:
  - name: "uuid"
    type: "string"
    primary-key: true
    description: "The webinar UUID."
    foreign-key-id: "webinar-uuid"

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
  
  - name: "webinar_id"
    type: "string"
    description: ""
---
