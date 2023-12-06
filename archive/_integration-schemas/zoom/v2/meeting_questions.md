---
tap: "zoom"
version: "2"
key: "meeting-question"

name: "meeting_questions"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingregistrantsquestionsget"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_questions.json"
description: |
  The `{{ table.name }}` table contains questions that users will see when registering for your {{ integration.display_name }} meetings.

replication-method: "Full Table"

api-method:
  name: "Get meeting questions"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingregistrantsquestionsget"

attributes:
  - name: "meeting_id"
    type: "string"
    primary-key: true
    description: "The meeting ID."
    foreign-key-id: "meeting-id"

  - name: "custom_questions"
    type: "array"
    description: ""
    subattributes:
    - name: "title"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "required"
      type: "boolean"
      description: ""

    - name: "answers"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "questions"
    type: "array"
    description: ""
    subattributes:
    - name: "field_name"
      type: "string"
      description: ""

    - name: "required"
      type: "boolean"
      description: ""
---