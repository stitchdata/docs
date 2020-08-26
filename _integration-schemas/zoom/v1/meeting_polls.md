---
tap: "zoom"
version: "1"
key: ""

name: "meeting_polls"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingpolls"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_polls.json"
description: |
  The `{{table.name}}` table contains information about the polls from your {{ integration.display_name }} meetings.

replication-method: "Full Table"

api-method:
    name: "getMeetingPolls"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingpolls"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The poll ID."
    foreign-key-id: "poll-id"

  - name: "meeting_id"
    type: "string"
    primary-key: true
    description: "The meeting ID."
    foreign-key-id: "meeting-id"

  - name: "questions"
    type: "array"
    description: ""
    subattributes:
      - name: "answers"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "title"
    type: "string"
    description: ""
---
