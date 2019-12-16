---
tap: "uservoice"
version: "1.0"

name: "segments"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Segments
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/segments.py
description: |
  The `{{ table.name }}` table contains info about segments, which are subsets of your end users and accounts defined by a set of criteria.

replication-method: "Key-based Incremental"

api-method:
  name: List segments
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-segments

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The segment ID."
    # foreign-key-id: "segment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the segment was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the segment was created."

  - name: "key"
    type: "string"
    description: "The segment key."

  - name: "name"
    type: "string"
    description: "The display name of the segment. For example: `Philadelphia`"

  - name: "filters"
    type: "object"
    description: "Details about the filters used in the segment."
    subattributes:
      - name: "operator"
        type: "string"
        description: "The operator used in the filter. For example: `and`, `or`"

      - name: "column"
        type: "string"
        description: "The column the filter uses."

      - name: "operand"
        type: "string"
        description: ""

      - name: "unit"
        type: ""
        description: ""

      - name: "expressions"
        type: "object"
        description: ""
        subattributes:
          - name: "operator"
            type: "string"
            description: ""

          - name: "column"
            type: "string"
            description: ""

          - name: "operand"
            type: "string"
            description: ""

          - name: "unit"
            type: ""
            description: ""
---