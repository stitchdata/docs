---
tap: "sendgrid-core"

name: "segments_all"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/segments_all.json
description: |
  The `segments_all` table contains info about the segments in your SendGrid account, and the conditions required for recipients to be added to the segment.

  For example: A segment for recipients with email addresses that contain `@stitchdata.com`

replication-method: "Full Table"

api-method:
  name: "List all segments"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/contactdb.html#List-All-Segments-GET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The segment ID."
    foreign-key-id: "segment-id"

  - name: "name"
    type: "string"
    description: "The name of the segment."

  - name: "recipient_count"
    type: "integer"
    description: "The current number of recipients in the segment."

  - name: "conditions"
    type: "array"
    description: |
      Details about the conditions a recipient must meet to be included in the segment.

      For example: To be included on a segment for Stitch, email addresses must contain `@stitchdata.com`. The condition could be:

      - `field: email`
      - `operator: contains`
      - `value: @stitchdata.com`
    subattributes:
      - name: "field"
        type: "string"
        description: "The name of the field used in the condition. For example: `email`"

      - name: "value"
        type: "string"
        description: "The value associated with the field in `field`. For example: `@stitchdata.com`"

      - name: "operator"
        type: "string"
        description: |
          The operator used in the condition. Possible values are:

          - `eq` (Equal to)
          - `ne` (Not equal to)
          - `lt` (Less than)
          - `gt` (Greater than)
          - `contains`

      - name: "and_or"
        type: "string"
        description: "If applicable, the `and` or `or` operation associated with the condition."
---