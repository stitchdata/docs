---
tap: "zoom"
version: "1"
key: ""

name: "webinar_polls"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarpolls"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_polls.json"
description: |
  The `{{ table.name }}` table contains information about polls in your {{ integration.display_name }} webinars.

replication-method: "Full Table"

api-method:
    name: "getWebinarPolls"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarpolls"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The webinar poll ID."
    foreign-key-id: "webinar-poll-id"

  - name: "webinar_id"
    type: "string"
    primary-key: true
    description: "The webinar ID."
    foreign-key-id: "webinar-id"
      
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
