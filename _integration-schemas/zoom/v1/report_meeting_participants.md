---
tap: "zoom"
version: "1"
key: "report-meeting-participant"

name: "report_meeting_participants"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportmeetingparticipants"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/report_meeting_participants.json"
description: |
  The `{{ table.name }}` table contains information about your {{ integration.display_name}}'s meeting participants. 

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, a {{ integration.display_name }} Pro plan or higher is required to retrieve this data.

replication-method: "Full Table"

api-method:
  name: "Get meeting participants"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/reports/reportmeetingparticipants"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The participant ID."
    # foreign-key-id: "participant-id"

  - name: "meeting_id"
    type: "string"
    primary-key: true
    description: "The meeting ID."
    foreign-key-id: "meeting-id"
      
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
    description: "The meeting participant's user ID."
    foreign-key-id: "user-id"
---