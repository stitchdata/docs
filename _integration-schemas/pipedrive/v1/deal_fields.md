---
tap: "pipedrive"
version: "1"
key: "deal-fields"

name: "deal_fields"
doc-link: https://developers.pipedrive.com/docs/api/v1/DealFields#getDealFields
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_pipedrive/schemas/deal_fields.json
description: |
  The `{{ table.name }}` table contains info about all deal fields.

api-method:
    name: "DealFields"
    doc-link: "https://developers.pipedrive.com/docs/api/v1/DealFields#getDealFields"

replication-method: "Key-based Incremental"

attributes:
  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "add_visible_flag"
    type: "boolean"
    description: ""

  - name: "bulk_edit_allowed"
    type: "boolean"
    description: ""

  - name: "details_visible_flag"
    type: "boolean"
    description: ""

  - name: "edit_flag"
    type: "boolean"
    description: ""

  - name: "field_type"
    type: "string"
    description: ""

  - name: "filtering_allowed"
    type: "boolean"
    description: ""

  - name: "id"
    type: "integer"
    description: ""
    primary-key: true

  - name: "important_flag"
    type: "boolean"
    description: ""

  - name: "index_visible_flag"
    type: "boolean"
    description: ""

  - name: "key"
    type: "string"
    description: ""

  - name: "last_updated_by_user_id"
    type: "integer"
    description: ""

  - name: "mandatory_flag"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "options"
    type: "array"
    description: ""
    subattributes:
    - name: "id"
      type: "string"
      description: ""

    - name: "label"
      type: "string"
      description: ""


  - name: "order_nr"
    type: "integer"
    description: ""

  - name: "searchable_flag"
    type: "boolean"
    description: ""

  - name: "sortable_flag"
    type: "boolean"
    description: ""

  - name: "update_time"
    type: "date-time"
    description: ""
    replication-key: true
---