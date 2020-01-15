---
tap: "uservoice"
version: "1"

name: "feature_statuses"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Feature
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/feature_statuses.py
description: |
  The `{{ table.name }}` table contains info about feature statuses, which are used to indicate a feature's current state.

replication-method: "Key-based Incremental"

api-method:
  name: List feature statuses
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-feature-statuses

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The feature status ID."
    foreign-key-id: "feature-status-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the feature status was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the feature status was created."

  - name: "name"
    type: "string"
    description: |
      The name of the feature status. By default, {{ integration.display_name }} includes six feature statuses, which may be modified or deleted:

      - `Proposed`
      - `Designing`
      - `Developing`
      - `Researching`
      - `Beta`
      - `Complete`

      If you created custom feature statuses, they will also display in this field.

  - name: "hex_color"
    type: "string"
    description: "The hex code of the label color associated with the feature status."

  - name: "position"
    type: "integer"
    description: "The position of the feature status in the full list of feature statuses in the {{ integration.display_name }} app."

  - name: "is_default"
    type: "boolean"
    description: "If `true`, this is the feature status that is applied to new features."

  - name: "links"
    type: "object"
    description: ""
    subattributes: 
    - name: "created_by"
      type: "integer"
      description: "The ID of the user who created the feature."
      foreign-key-id: "user-id"

    - name: "updated_by"
      type: "integer"
      description: "The ID of the user who last updated the feature."
      foreign-key-id: "user-id"
---