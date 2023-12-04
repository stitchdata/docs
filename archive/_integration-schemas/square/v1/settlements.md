---
tap: "square"
version: "1"
key: "settlement"

name: "settlements"
doc-link: "https://developer.squareup.com/reference/square/settlements-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/settlements.json"
description: |
  The `{{ table.name }}` table contains information about deposits and withdrawals issued by {{ integration.display_name }}.

  **Note**: This table can't be replicated if the **Connect to a sandbox environment** box is checked in the [integration's settings](#add-stitch-data-source) due to limits imposed by {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List settlements (V1)"
  doc-link: "https://developer.squareup.com/reference/square/settlements-api/v1-list-settlements"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The settlement ID."
    # foreign-key-id: "settlement-id"

  - name: "bank_account_id"
    type: "string"
    description: "The ID of the bank account associated with the settlement."
    foreign-key-id: "bank-account-id"

  - name: "entries"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "null"
        description: ""
  
  - name: "initiated_at"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "total_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency_code"
        type: "string"
        description: ""
---