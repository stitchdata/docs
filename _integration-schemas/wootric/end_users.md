---
tap: "wootric"
# version:

name: "end_users"
doc-link: 
singer-schema: https://github.com/singer-io/tap-wootric/blob/master/tap_wootric/schemas/end_users.json
description: |
  The `end_users` table contains info about the end users associated with survey opportunities.

replication-method: "Incremental"
api-method:
  name: getAllEndUsers
  doc-link: http://docs.wootric.com/api/#get-all-end-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The end user ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the end user was updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the end user was created."

  - name: "email"
    type: "string"
    description: "The end user's email address."

  - name: "last_surveyed"
    type: "date-time"
    description: "The time the end user was last surveyed."

  - name: "external_created_at"
    type: "date-time"
    description: "The UNIX timestamp of when the user was created externally."

  - name: "page_views_count"
    type: "integer"
    description: "The end user's total number of page views."
---