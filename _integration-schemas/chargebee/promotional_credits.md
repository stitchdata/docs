---
tap: "chargebee"
version: "1"
key: "promotional-credit"

name: "promotional_credits"
doc-link: "https://apidocs.chargebee.com/docs/api/promotional_credits"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/promotional_credits.json"
description: |
  The `{{ table.name }}` table contains info about the promotional_credits in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List promotional credits"
    doc-link: "https://apidocs.chargebee.com/docs/api/promotional_credits#list_promotional_credits"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The promotional credit ID."
    # foreign-key-id: "promotional-credit-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the promotional credit was created."

  - name: "amount"
    type: "string"
    description: "The amount of the promotional credit."

  - name: "closing_balance"
    type: "integer"
    description: "The closing balance on the end date."

  - name: "credit_type"
    type: "string"
    description: |
      The type of promotional credit provided to the customer. Possible values are:

      - `loyalty_credits`
      - `referral_rewards`
      - `general`

  - name: "currency_code"
    type: "string"
    description: "The currency code (ISO 4217 format) for promotional credit."

  - name: "customer_id"
    type: "string"
    description: "The ID of the customer associated with the promotional credit."
    foreign-key-id: "customer-id"

  - name: "description"
    type: "string"
    description: "Description of the promotional credit."

  - name: "done_by"
    type: "string"
    description: "The user who added/deducted the credit."

  - name: "type"
    type: "string"
    description: |
      The type of promotional credit. Possible values are:

      - `increment`
      - `decrement`
---