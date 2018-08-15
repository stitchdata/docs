---
tap: "harvest"
version: "1.0"

name: "invoice_payments"
doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/invoice-messages-payments#show-payments-for-an-invoice
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoice_payments.json
description: |
  The `invoice_payments` table contains info about the payments applied to invoices in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: showPaymentsForAnInvoice
  doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/invoice-messages-payments/#show-payments-for-an-invoice

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The invoice payment ID."
    # foreign-keys:
    #   - table: "invoices"
    #     attribute: "id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the invoice payment was updated."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the payment."
    # foreign-keys:
    #   - table: "invoices"
    #     attribute: "id"

  - name: "amount"
    type: "number"
    description: "The amount of the invoice payment."

  - name: "paid_at"
    type: "date-time"
    description: "The date the invoice payment was made."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice payment was created."

  - name: "notes"
    type: "string"
    description: "Any notes entered about the invoice payment."

  - name: "recorded_by"
    type: "string"
    description: "The name of the user who recorded the invoice payment."

  - name: "recorded_by_email"
    type: "string"
    description: "The email address of the user who recorded the payment."

  - name: "paypal_transaction_id"
    type: "integer"
    description: "If paid via PayPal, this field will contain the PayPal transaction ID associated with the invoice payment."

  - name: "authorization"
    type: "string"
    description: "If applicable, this field will contain information about the authorization associated with the invoice payment."

  - name: "payment_gateway_id"
    type: "integer"
    description: "If paid via the payment gateway, this field will contain the ID of the payment gateway used to make the invoice payment."
---