---
tap: "square"
version: "1"
key: ""

name: "cash_drawer_shifts"
doc-link: "https://developer.squareup.com/reference/square/cash-drawers-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/cash_drawer_shifts.json"
description: |
  The `{{ table.name }}` table contains infomration about cash transactions in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "Retrieve cash drawer shift"
    doc-link: "https://developer.squareup.com/reference/square/cash-drawers-api/retrieve-cash-drawer-shift"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The cash drawer shift ID."
    foreign-key-id: "cash-drawer-id"
  - name: "closed_at"
    type: "date-time"
    description: ""
  - name: "closed_cash_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""
      - name: "currency"
        type: "string"
        description: ""
  - name: "description"
    type: "string"
    description: ""
  - name: "ended_at"
    type: "date-time"
    description: ""
  - name: "expected_cash_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""
      - name: "currency"
        type: "string"
        description: ""
  
  - name: "opened_at"
    type: "date-time"
    description: ""
  - name: "opened_cash_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""
      - name: "currency"
        type: "string"
        description: ""
  - name: "state"
    type: "string"
    description: ""
---
