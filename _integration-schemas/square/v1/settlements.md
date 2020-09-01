---
tap: "square"
version: "1"
key: ""

name: "settlements"
doc-link: "https://developer.squareup.com/reference/square/settlements-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/settlements.json"
description: |
  The `{{ table.name }}` table contains information about deposits and withdrawals issued by {{ integration.display_name }. This table cannot be replicated with a sandbox account due to restrictions from {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "List settlements"
    doc-link: "https://developer.squareup.com/reference/square/settlements-api/v1-list-settlements"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The settlement ID."

  - name: "bank_account_id"
    type: "string"
    description: "The bank account ID."
    foreign-key-id: "bank-id"

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
