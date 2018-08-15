---
tap: "harvest"
version: "1.0"

name: "invoices"
doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/show-invoices#show-a-single-invoice
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoices.json
description: |
  The `invoices` table contains info about the invoices in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The invoice ID."
    # foreign-keys:
    #   - table: "invoice_messages"
    #     attribute: "invoice_id"
    #   - table: "invoice_payments"
    #     attribute: "invoice_id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the invoice was updated."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client associated with the invoice."
    # foreign-keys:
    #   - table: "clients"
    #     attribute: "id"
    #   - table: "contacts"
    #     attribute: "client_id"

  - name: "client_name"
    type: "string"
    description: "The name of the client associated with the invoice."

  - name: "period_start"
    type: "string"
    description: "The start date of the period associated with the invoice."

  - name: "period_end"
    type: "string"
    description: "The end date of the period associated with the invoice."

  - name: "number"
    type: "string"
    description: "The invoice number. If no value is set, Harvest will automatically generate a value."

  - name: "issued_at"
    type: "string"
    description: "The date the invoice was issued."

  - name: "due_at"
    type: "string"
    description: "The date that payment of the invoice is due by."

  - name: "amount"
    type: "number"
    description: "The total amount of the invoice."

  - name: "currency"
    type: "string"
    description: "The currency denomination of the invoice."

  - name: "state"
    type: "string"
    description: |
      The state of the invoice. Possible values:

      - `open` - May apply for unpaid, sent invoices (either current or past due)
      - `partial` - Applicable to invoices with partial payments
      - `draft` 
      - `paid` - Applicable to invoices paid in full
      - `unpaid`
      - `pastdue`
      - `closed` - Applicable to written off invoices
    doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/show-invoices/#show-recently-created-invoices

  - name: "notes"
    type: "string"
    description: "Any notes entered about the invoice."

  - name: "purchase_order"
    type: "string"
    description: "If applicable, the purchase order associated with the invoice."

  - name: "due_amount"
    type: "number"
    description: "The due amount of the invoice."

  - name: "due_at_human_format"
    type: "string"
    description: "The human-readable format of the invoice due date."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice was created."

  - name: "tax"
    type: "string, number"
    description: "The tax percentage applied to the subtotal, including line items and discounts."

  - name: "tax_amount"
    type: "number"
    description: "The first amount of tax included, calculated from `tax`. If `tax` is undefined, this value will be `null`."

  - name: "subject"
    type: "string"
    description: "The subject of the invoice."

  - name: "recurring_invoice_id"
    type: "integer"
    description: "If a recurring invoice, this field will contain the ID of the recurring invoice."

  - name: "tax2"
    type: "string, number"
    description: "The tax percentage applied to the subtotal, including line items and discounts."

  - name: "tax2_amount"
    type: "number"
    description: "The amount calculated from `tax2`."

  - name: "client_key"
    type: "string"
    description: "A string used to build a URL to the public web invoice for the associated client."

  - name: "estimate_id"
    type: "integer"
    description: "If applicable, the ID of the estimate associated with the invoice."

  - name: "discount"
    type: "string, number"
    description: "If applicable, the percentage to be subtracted from the subtotal."

  - name: "discount_amount"
    type: "number"
    description: "If applicable, the amount calculated from `discount`."

  - name: "retainer_id"
    type: "integer"
    description: "If applicable, the ID of the retainer associated with the invoice."

  - name: "created_by_id"
    type: "integer"
    description: "The ID of the user who created the invoice."
---