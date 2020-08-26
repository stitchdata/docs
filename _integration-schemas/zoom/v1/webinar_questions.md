---
tap: "zoom"
version: "1"
key: ""

name: "webinar_questions"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarregistrantsquestionsget"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_questions.json"
description: |
  The `{{ table.name }}` table contains information about your questions to be answered when registering for a {{ integration.display_name }} webinar. To retrieve this information, you must have a **Rate Limit Label** value of `Light`, pro plan or higher with a Webinar add-on, and the following scopes: `webinar:read:admin`, `webinar:read`.

replication-method: "Full Table"

api-method:
    name: "getWebinarQuestions"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinarregistrantsquestionsget"

attributes:
  - name: "webinar_id"
    type: "string"
    primary-key: true
    description: "The webinar ID."
    foreign-key-id: "webinar-id"

  - name: "custom_questions"
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
      - name: "required"
        type: "boolean"
        description: ""
      - name: "title"
        type: "string"
        description: ""
      - name: "type"
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
