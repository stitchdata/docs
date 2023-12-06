---
tap: "harvest"
version: "2"

name: "estimates"
doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimates/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/estimates.json
description: |
  The `{{ table.name }}` table contains info about the estimates in  your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: List all estimates
  doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-messages/#list-all-messages-for-an-estimate

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The estimate ID."
    foreign-key-id: "estimate-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the estimate was last updated."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client the estimate is associated with."
    foreign-key-id: "client-id"

  - name: "creator_id"
    type: "integer"
    description: "The ID of the user that created the estimate."
    foreign-key-id: "user-id"

  - name: "client_key"
    type: "string"
    description: "A string used to build a URL to the public web invoice for the client."

  - name: "number"
    type: "string"
    description: "The estimate number."

  - name: "purchase_order"
    type: "string"
    description: "The purchase order number."

  - name: "amount"
    type: "number"
    description: "The total amount of the estimate, including discounts and taxes."

  - name: "tax"
    type: "string, number"
    description: "The tax percentage applied to the subtotal, including line items and discounts."

  - name: "tax_amount"
    type: "number"
    description: "The first amount of tax included, calculated from `tax`."

  - name: "tax2"
    type: "string, number"
    description: "The percentage applied to the subtotal, including line items and discounts."

  - name: "tax2_amount"
    type: "number"
    description: "The second amount of tax included, calculated from `tax2`."

  - name: "discount"
    type: "string, number"
    description: "The percentage to be subtracted from the subtotal."

  - name: "discount_amount"
    type: "number"
    description: "The discount amount, calulated from `discount`."

  - name: "subject"
    type: "string"
    description: "The estimate subject."

  - name: "notes"
    type: "string"
    description: "Any additional notes included on the estimate."

  - name: "currency"
    type: "string"
    description: "The currency code associated with the estimate."

  - name: "state"
    type: "string"
    description: |
      The current state of the estimate. Possible values are:

      - `draft`
      - `sent`
      - `accepted`
      - `declined`

  - name: "issue_date"
    type: "string"
    description: "The date the estimate was issued."

  - name: "sent_at"
    type: "date-time"
    description: "The time the estimate was sent."

  - name: "accepted_at"
    type: "date-time"
    description: "The time the estimate was accepted."

  - name: "declined_at"
    type: "date-time"
    description: "The time the estimate was declined."

  - name: "created_at"
    type: "date-time"
    description: "The time the estimate was created."
---