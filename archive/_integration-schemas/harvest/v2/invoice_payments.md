---
tap: "harvest"
version: "2"

name: "invoice_payments"
doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-payments/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoice_payments.json
description: |
  The `{{ table.name }}` table contains info about the payments applied to invoices in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all payments for an invoice
  doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-payments#list-all-payments-for-an-invoice

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The invoice payment ID."
    # foreign-key-id: "invoice-payment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the invoice payment was updated."

  - name: "amount"
    type: "number"
    description: "The amount of the invoice payment."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice payment was created."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the payment."
    foreign-key-id: "invoice-id"

  - name: "notes"
    type: "string"
    description: "Any notes entered about the invoice payment."

  - name: "paid_at"
    type: "date-time"
    description: "The date and time the invoice payment was made."

  - name: "paid_date"
    type: "string"
    description: "The date the payment was made."

  - name: "payment_gateway_id"
    type: "integer"
    description: "If paid via the payment gateway, this field will contain the ID of the payment gateway used to make the invoice payment."

  - name: "payment_gateway_name"
    type: "integer"
    description: "If paid via the payment gateway, this field will contain the name of the payment gateway used to make the invoice payment."

  - name: "recorded_by"
    type: "string"
    description: "The name of the user who recorded the invoice payment."

  - name: "recorded_by_email"
    type: "string"
    description: "The email address of the user who recorded the payment."

  - name: "transaction_id"
    type: "string"
    description: |
      If paid via PayPal, this field will contain the PayPal transaction ID associated with the invoice payment.

      Otherwise, this will contain the card authorization.
---