---
tap: "zoom"
version: "1"
key: "meeting-registrant"

name: "meeting_registrants"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingregistrants"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meeting_registrants.json"
description: |
  The `{{ table.name }}` table contains the list of users who have registered for your {{ integration.display_name }} meetings.

replication-method: "Full Table"

api-method:
  name: "Get meeting registrants"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingregistrants"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The registrant's user ID."
    # foreign-key-id: "registrant-id"

  - name: "meeting_id"
    type: "string"
    primary-key: true
    description: "The meeting ID."
    foreign-key-id: "meeting-id"  

  - name: "address"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "county"
    type: "string"
    description: ""

  - name: "create_time"
    type: "date-time"
    description: ""

  - name: "custom_questions"
    type: "array"
    description: ""
    subattributes:
      - name: "title"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""
  
  - name: "industry"
    type: "string"
    description: ""

  - name: "job_title"
    type: "string"
    description: ""

  - name: "join_url"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""
  
  - name: "no_of_employees"
    type: "string"
    description: ""

  - name: "org"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "purchasing_time_frame"
    type: "string"
    description: ""

  - name: "role_in_purchase_process"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---