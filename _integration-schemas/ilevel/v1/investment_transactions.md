---
tap: "ilevel"
version: "1"
key: "investment-transaction"

name: "investment_transactions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/investment_transactions.json"
description: |
  The `{{ table.name }}` table contains info about investment transactions in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "GetInvestmentTransactions"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The investment transaction ID."
    foreign-key-id: "investment-transaction-id"

  - name: "last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the investment transaction was last modified."

  - name: "amount"
    type: "number"
    description: ""

  - name: "as_of"
    type: "date-time"
    description: ""

  - name: "client"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "cost_per_share"
    type: "number"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "custom1"
    type: "string"
    description: ""

  - name: "custom2"
    type: "string"
    description: ""

  - name: "custom3"
    type: "date-time"
    description: ""

  - name: "custom4"
    type: "date-time"
    description: ""

  - name: "custom5"
    type: "string"
    description: ""

  - name: "custom6"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "group_id"
    type: "integer"
    description: ""

  - name: "internal_id"
    type: "string"
    description: ""

  - name: "investment"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "investment-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "last_modified_by"
    type: "object"
    description: ""
    subattributes:
      - name: "email_address"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "middle_name"
        type: "string"
        description: ""

      - name: "user_name"
        type: "string"
        description: ""

  - name: "local_amount"
    type: "number"
    description: ""

  - name: "local_currency"
    type: "string"
    description: ""

  - name: "original_id"
    type: "integer"
    description: ""

  - name: "owner"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        # foreign-key-id: "owner-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "scenario"
    type: "object"
    description: ""
    subattributes:
      - name: "excel_name"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "scenario-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "security"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "security-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "shares"
    type: "number"
    description: ""

  - name: "transaction_category"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "transaction_date"
    type: "date-time"
    description: ""

  - name: "transaction_type"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "value_per_share"
    type: "number"
    description: ""
---