---
tap: "uservoice"
# version: "1.0"

name: "segmented_values"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/segmented_values.py
description: |
  The `{{ table.name }}` table contains info about segmented values, which are calculated columns that aggregate supporter metrics for a segment.

replication-method: "Key-based Incremental"

api-method:
  name: List segmented values
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-segmented-values

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The segmented value ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the segmented value was last updated."

  - name: "name"
    type: "string"
    description: "The display name of the segmented value. For example: `Philadelphia`"

  - name: "key"
    type: "string"
    description: "The segmented value key. For example: `cv_philadelphia.accounts_count`"

  - name: "object_type"
    type: "string"
    description: ""

  - name: "column_type"
    type: "string"
    description: ""

  - name: "links"
    type: "object"
    description: ""
    object-attributes: 
    - name: "updated_by"
      type: "integer"
      description: "The ID of the user who last updated the segmented value."
      foreign-key: true
      table: "users"

    - name: "created_by"
      type: "integer"
      description: "The ID of the user who created the segmented value."
      foreign-key: true
      table: "users"

    - name: "segment"
      type: "integer"
      description: "The ID of the segment associated with the segmented value."
      foreign-key: true
      table: "segments"
---