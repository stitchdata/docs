---
tap: "zoom"
version: "1"
key: "report-webinar-participant"

name: "report_webinar_participants"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportwebinarparticipants"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/report_webinar_participants.json"
description: |
  The `{{ table.name }}` table contains information about your {{ integration.display_name}}'s webinar participants. 

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, a Pro plan or higher with with the webinar add-on enabled is required to retrieve this data.

replication-method: "Full Table"

api-method:
  name: "Get webinar participants"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportwebinarparticipants"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The webinar participant ID."
    # foreign-key-id: "webinar-participant-id"

  - name: "webinar_id"
    type: "string"
    primary-key: true
    description: "The webinar ID."
    foreign-key-id: "webinar-id"

  - name: "attentiveness_score"
    type: "string"
    description: ""

  - name: "duration"
    type: "string"
    description: ""
  
  - name: "join_time"
    type: "date-time"
    description: ""

  - name: "leave_time"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "user_email"
    type: "string"
    description: ""

  - name: "user_id"
    type: "string"
    description: "The webinar participant's user ID."
    foreign-key-id: "user-id"
---