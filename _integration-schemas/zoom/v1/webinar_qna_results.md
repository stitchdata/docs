---
tap: "zoom"
version: "1"
key: "webinar-qna-results"

name: "webinar_qna_results"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/listpastwebinarqa"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_qna_results.json"
description: |
  The `{{ table.name }}` table contains information about about the questions and answers from specific {{ integration.display_name }} webinars.

replication-method: "Full Table"

api-method:
  name: "Get webinar Q&A"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/listpastwebinarqa"

attributes:
  - name: "webinar_uuid"
    type: "string"
    primary-key: true
    description: "The webinar UUID."
    foreign-key-id: "webinar-uuid"

  - name: "email"
    type: "string"
    primary-key: true
    description: "The email used for the webinar Q & A session."
    
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