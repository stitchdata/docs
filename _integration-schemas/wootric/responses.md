---
tap: "wootric"
version: "1.0"

name: "responses"
doc-link: http://docs.wootric.com/api/#get-all-responses
singer-schema: https://github.com/singer-io/tap-wootric/blob/master/tap_wootric/schemas/responses.json
description: |
  The `{{ table.name }}` table contains info about end user responses to surveys.

replication-method: "Key-based Incremental"
api-method:
  name: getAllResponses
  doc-link: http://docs.wootric.com/api/#get-all-responses

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The response ID."
    # foreign-key-id: "response-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the response was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the response was created."

  - name: "score"
    type: "integer"
    description: "The response's score."

  - name: "text"
    type: "string"
    description: "The response's comment."

  - name: "ip_address"
    type: "string"
    description: "The response's IP address."

  - name: "origin_url"
    type: "string"
    description: "The response's origin URL."

  - name: "end_user_id"
    type: "integer"
    description: "The ID of the end user who gave the response."
    foreign-key-id: "end-user-id"

  - name: "survey_id"
    type: "integer"
    description: "The ID of the survey associated with the response."
    foreign-key-id: "survey-id"

  - name: "completed"
    type: "boolean"
    description: "Indicates if a response has been completed."

  - name: "excluded_from_calculations"
    type: "boolean"
    description: "Indicates if a response should be excluded from calculations."

  - name: "tags"
    type: "array"
    description: "Tags applied to the response."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag applied to the response."
---