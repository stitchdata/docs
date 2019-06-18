---
tap: "pipedrive"
version: "1.0"
key: "dealflow"

name: "dealflow"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/dealflow.json"
description: |
  The `{{ table.name }}` table contains info about the updates made to a deal.

replication-method: ""

api-method:
  name: "List updates about a deal"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Deals/get_deals_id_flow"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The deal flow ID."
    # foreign-key-id: "deal-flow-id"

  - name: "log_time"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "additional_data"
    type: "string"
    description: ""

  - name: "change_source"
    type: "string"
    description: ""

  - name: "field_key"
    type: "string"
    description: ""

  - name: "is_bulk_update_flag"
    type: "boolean"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "new_value"
    type: "string"
    description: ""

  - name: "old_value"
    type: "string"
    description: ""

  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---