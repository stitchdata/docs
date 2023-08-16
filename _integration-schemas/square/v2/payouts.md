---
tap: "square"
version: "2"
key: "payouts"

name: "payouts"
doc-link: "https://developer.squareup.com/reference/square/payouts-api"
singer-schema: https://github.com/singer-io/tap-square/tree/TDL-23235-add-payouts-stream/tap_square/schemas/payouts.json
description: "The `{{ table.name }}` table contains information about all payouts made in {{ integration.display_name }}."

replication-method: "Full Table"

api-method:
  name: "List payouts (V2)"
  doc-link: "https://developer.squareup.com/reference/square/payouts-api/list-payouts"

attributes:
  - name: "id"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "location_id"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""


  - name: "amount_money"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "currency"
      type: "string"
      description: ""


  - name: "destination"
    type: "object"
    description: ""
    subattributes:
    - name: "type"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

  - name: "version"
    type: "integer"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "payout_fee"
    type: "array"
    description: ""
    subattributes:
      - name: "effective_at"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "amount_money"
        type: "object"
        description: ""
        subattributes:
          - name: "currency"
            type: "string"
            description: ""

          - name: "amount"
            type: "integer"
            description: ""


  - name: "arrival_date"
    type: "date-time"
    description: ""

  - name: "end_to_end_id"
    type: "string"
    description: ""
---