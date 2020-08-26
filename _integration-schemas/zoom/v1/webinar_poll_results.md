---
tap: "zoom"
version: "1"
key: ""

name: "webinar_poll_results"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/listpastwebinarpollresults"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_poll_results.json"
description: |
  The `{{ table.name }}` data contains information about poll results from specific {{ integration.display_name }} webinars. To retrieve this information, you need a webinar license, a **Rate Limit Label** value of `Medium`, and the following scopes: `webinar:read:admin`, `webinar:read`.

replication-method: "Full Table"

api-method:
    name: "getWebinarPollResults"
    doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/listpastwebinarpollresults"

attributes:
  - name: "webinar_uuid"
    type: "string"
    primary-key: true
    description: "The webinar UUID."
    foreign-key-id: "webinar-uuid"

  - name: "email"
    type: "string"
    primary-key: true
    description: |
      The email used for the {{ integration.display_name }} webinar. 

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
