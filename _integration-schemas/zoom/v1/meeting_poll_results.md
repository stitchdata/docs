---
tap: "zoom"
version: "1"
key: ""

name: "meeting_poll_results"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/listpastmeetingpolls"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_poll_results.json"
description: |
  The `{{ table.name }}` table contains information about the results of polls from your {{ integration.display_name }} meetings. The only way this information is available is if the host user's role is **Pro** and if the meeting was scheduled.

replication-method: "Full Table"

api-method:
    name: "getPastMeetingPolls"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/listpastmeetingpolls"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: |
      The email used for the {{ integration.display_name }} meeting. 

  - name: "meeting_uuid"
    type: "string"
    primary-key: true
    description: "The meeting UUID"
    foreign-key-id: "meeting-uuid"
    
  - name: "name"
    type: "string"
    description: ""
  - name: "question_details"
    type: "array"
    description: ""
    subattributes:
      - name: "answer"
        type: "string"
        description: ""
      - name: "question"
        type: "string"
        description: ""
---
