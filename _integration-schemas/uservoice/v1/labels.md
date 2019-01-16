---
tap: "uservoice"
# version: "1.0"

name: "labels"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Forum
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/forums.py
description: |
  The `{{ table.name }}` table contains info about labels in your {{ integration.display_name }}, which admins use to internally organize suggestions.

replication-method: "Key-based Incremental"

api-method:
  name: List labels
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-labels

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The label ID."
    foreign-key-id: "label-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the label was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the label was created."

  - name: "name"
    type: "string"
    description: "The name of the label."

  - name: "full_name"
    type: "string"
    description: "The full name of the label."

  - name: "level"
    type: "integer"
    description: ""

  - name: "open_suggestions_count"
    type: "integer"
    description: "The total number of open suggestions associated with the label."

  - name: "links"
    type: "object"
    description: "IDs of nested labels associated with the parent label, if any."
    object-attributes: 
      - name: "parent"
        type: "integer"
        description: "If the label is a nested label, this field will contain the ID of the parent (top-level) label."
        foreign-key-id: "label-id"
---