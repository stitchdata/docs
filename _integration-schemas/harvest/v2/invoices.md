---
tap: "harvest"
version: "2.0"

name: "invoices"
doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoices/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoices.json
description: |
  The `{{ table.name }}` table contains info about the invoices in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all invoices
  doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoices#list-all-invoices

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the invoice was updated."

  - name: "amount"
    type: "number"
    description: "The total amount of the invoice."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client associated with the invoice."
    foreign-key-id: "client-id"

  - name: "client_key"
    type: "string"
    description: "A string used to build a URL to the public web invoice for the associated client."

  - name: "closed_at"
    type: "date-time"
    description: "The date and time the invoice was closed."

  - name: "creator_id"
    type: "integer"
    description: "The ID of the user who created the invoice."
    foreign-key-id: "user-id"

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice was created."

  - name: "currency"
    type: "string"
    description: "The currency denomination of the invoice."

  - name: "discount"
    type: "string, number"
    description: "If applicable, the percentage to be subtracted from the subtotal."

  - name: "discount_amount"
    type: "number"
    description: "If applicable, the amount calculated from `discount`."

  - name: "due_amount"
    type: "number"
    description: "The due amount of the invoice."

  - name: "due_date"
    type: "date-time"
    description: "The date that payment of the invoice is due by."

  - name: "estimate_id"
    type: "integer"
    description: "If applicable, the ID of the estimate associated with the invoice."
    foreign-key-id: "estimate-id"

  - name: "issue_date"
    type: "date-time"
    description: "The date the invoice was issued."

  - name: "notes"
    type: "string"
    description: "Any notes entered about the invoice."

  - name: "number"
    type: "string"
    description: "The invoice number. If no value is set, Harvest will automatically generate a value."

  - name: "paid_at"
    type: "date-time"
    description: "The date and time the invoice was paid."

  - name: "paid_date"
    type: "string"
    description: "The date the invoice was paid."

  - name: "payment_term"
    type: "string"
    description: |
      The timeframe in which the invoice should be paid. Possible values are:

      - `upon receipt`
      - `net 15`
      - `net 30`
      - `net 45`
      - `net 60`
      - `custom`

  - name: "period_start"
    type: "string"
    description: "The start date of the period associated with the invoice."

  - name: "period_end"
    type: "string"
    description: "The end date of the period associated with the invoice."

  - name: "purchase_order"
    type: "string"
    description: "If applicable, the purchase order associated with the invoice."

  - name: "retainer_id"
    type: "integer"
    description: "If applicable, the ID of the retainer associated with the invoice."

  - name: "sent_at"
    type: "date-time"
    description: "The date the invoice was sent."

  - name: "state"
    type: "string"
    description: |
      The state of the invoice. Possible values:

      - `open`
      - `draft` 
      - `paid`
      - `closed`

  - name: "subject"
    type: "string"
    description: "The subject of the invoice."

  - name: "tax"
    type: "string, number"
    description: "The tax percentage applied to the subtotal, including line items and discounts."

  - name: "tax_amount"
    type: "number"
    description: "The first amount of tax included, calculated from `tax`. If `tax` is undefined, this value will be `null`."

  - name: "tax2"
    type: "string, number"
    description: "The tax percentage applied to the subtotal, including line items and discounts."

  - name: "tax2_amount"
    type: "number"
    description: "The amount calculated from `tax2`."
---