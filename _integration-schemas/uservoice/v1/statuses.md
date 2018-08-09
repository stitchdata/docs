---
tap: "uservoice"
# version: "1.0"

name: "stauses"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Stauses
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/.py
description: |
  The `{{ table.name }}` table contains info about the various suggestion statuses in your {{ integration.display_name }} account. 

replication-method: "Key-based Incremental"

api-method:
  name: List statuses
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-statuses

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The status ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the status was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the status was created."

  - name: "name"
    type: "string"
    description: |
      The name of the status. By default, {{ integration.display_name }} includes five suggestion statuses, which may be modified or deleted:

      - `under review`
      - `planned`
      - `started`
      - `completed`
      - `declined`

      If you created custom suggestion statuses, they will also display in this field.

  - name: "is_open"
    type: "boolean"
    description: "If `true`, voting is enabled on suggestions with this status."

  - name: "hex_color"
    type: "string"
    description: "The hex code of the label color associated with the suggestion status."

  - name: "position"
    type: "integer"
    description: "The position of the feature status in the full list of suggestion statuses in the {{ integration.display_name }} app."

  - name: "allow_comments"
    type: "boolean"
    description: "If `true`, end users are able to post new comments on ideas when this status is assigned."
---