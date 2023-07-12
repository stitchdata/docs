---
tap: "zoom"
version: "1"
key: "webinar-poll-results"

name: "webinar_poll_results"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/listpastwebinarpollresults"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinar_poll_results.json"
description: |
  The `{{ table.name }}` data contains information about poll results from specific {{ integration.display_name }} webinars. 

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, the following requirements must be met to retrieve this data:

  - A {{ integration.display_name }} webinar license
  - A Pro plan or higher
  - An authentication app with the `webinar:read:admin` and `webinar:read` scopes

replication-method: "Full Table"

api-method:
  name: "Get webinar poll results"
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
    description: "The email used for the {{ integration.display_name }} webinar."

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