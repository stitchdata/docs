---
tap: "zoom"
version: "1"
key: "meeting-poll"

name: "meeting_polls"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingpolls"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_polls.json"
description: |
  The `{{table.name}}` table contains information about the polls from your {{ integration.display_name }} meetings.

replication-method: "Full Table"

api-method:
  name: "Get meeting polls"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingpolls"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The poll ID."
    # foreign-key-id: "poll-id"

  - name: "meeting_id"
    type: "string"
    primary-key: true
    description: "The meeting ID."
    foreign-key-id: "meeting-id"
    
  - name: "anonymous"
    type: "boolean"
    description: ""

  - name: "poll_type"
    type: "integer"
    description: ""

  - name: "questions"
    type: "array"
    description: ""
    subattributes:
    - name: "answer_max_character"
      type: "integer"
      description: ""

    - name: "answer_min_character"
      type: "integer"
      description: ""

    - name: "answer_required"
      type: "boolean"
      description: ""

    - name: "case_sensitive"
      type: "boolean"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "rating_max_label"
      type: "string"
      description: ""

    - name: "rating_max_value"
      type: "integer"
      description: ""

    - name: "rating_min_label"
      type: "string"
      description: ""

    - name: "rating_min_value"
      type: "integer"
      description: ""

    - name: "right_answers"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

    - name: "show_as_dropdown"
      type: "boolean"
      description: ""

    - name: "type"
      type: "string"
      description: ""

    - name: "prompts"
      type: "array"
      description: ""
      subattributes:
      - name: "prompt_question"
        type: "string"
        description: ""

      - name: "prompt_right_answers"
        type: "array"
        description: ""
        subattributes:
        - name: "items"
          type: "string"
          description: ""


    - name: "answers"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""


  - name: "status"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---