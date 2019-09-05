---
tap: "mailchimp"
version: "1.0"

key: "list-segment"
name: "list_segments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/list_segments.json"
description: |
  The `{{ table.name }}` table contains info about the available segments for a specific list.

replication-method: "Full Table"

api-method:
    name: "Get information about all segments in a list"
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/lists/segments/#read-get_lists_list_id_segments"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique ID for the segment."
    #foreign-key-id: "list-segment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the segment was last updated in ISO 8601 format."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the segment was created in ISO 8601 format."

  - name: "list_id"
    type: "string"
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "member_count"
    type: "integer"
    description: "The number of active subscribers currently included in the segment."

  - name: "name"
    type: "string"
    description: "The name of the segment."

  - name: "options"
    type: "object"
    description: "The conditions of the segment. Static segments (tags) and fuzzy segments don’t have conditions."
    subattributes:
      - name: "conditions"
        type: "array"
        description: "The segment conditions."
        subattributes:
          - name: "condition_type"
            type: "string"
            description: "The type of the segment."

          - name: "field"
            type: "string"
            description: "The segment field."

          - name: "op"
            type: "string"
            description: "The operator."

          - name: "value"
            type: "string"
            description: "The value."

      - name: "match"
        type: "string"
        description: |
          The match type. Possible values are:

          - `any`
          - `all`

  - name: "type"
    type: "string"
    description: |
      The type of segment. Possible values are:

      - `saved`
      - `static`
      - `fuzzy`
---