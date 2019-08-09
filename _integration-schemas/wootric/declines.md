---
tap: "wootric"
# version: "1.0"

name: "declines"
doc-link: http://docs.wootric.com/api/#get-all-declines
singer-schema: https://github.com/singer-io/tap-wootric/blob/master/tap_wootric/schemas/declines.json
description: |
  The `{{ table.name }}` table contains info about declines, or the instances where a user is presented with a survey opportunity and opts out.

replication-method: "Key-based Incremental"
api-method:
  name: getAllDeclines
  doc-link: http://docs.wootric.com/api/#get-all-declines

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The decline ID."
    # foreign-key-id: "decline-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the decline was updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the decline was created."

  - name: "end_user_id"
    type: "integer"
    description: "The ID of the end user who declined the survey opportunity."
    foreign-key-id: "end-user-id"

  - name: "survey_id"
    type: "integer"
    description: "The ID of the survey associated with the decline."
    foreign-key-id: "survey-id"
---