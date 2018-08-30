---
tap: "harvest"
version: "1.0"

name: "invoice_messages"
doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/invoice-messages-payments/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoice_messages.json
description: |
  The `invoice_messages` table contains info about invoice messages, or emails sent to clients about invoices.

replication-method: "Key-based Incremental"
api-method:
  name: showInvoiceMessages
  doc-link: http://help.getharvest.com/api-v1/invoices-api/invoices/invoice-messages-payments/#show-invoice-messages

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the invoice message."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the invoice message was last updated."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the invoice message."
    # foreign-keys:
    #   - table: "invoices"
    #     attribute: "id"

  - name: "send_me_a_copy"
    type: "boolean"
    description: "Indicates if a copy should be sent to the current user."

  - name: "body"
    type: "string"
    description: "The body of the invoice message."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice message was created."

  - name: "sent_by"
    type: "string"
    description: "The name of the user who created the invoice message."

  - name: "sent_by_email"
    type: "string"
    description: "The email address of the user who created the invoice message."

  - name: "thank_you"
    type: "boolean"
    description: "Indicates if this is a `thank you` message."

  - name: "subject"
    type: "string"
    description: "The subject of the invoice message."

  - name: "include_pay_pal_link"
    type: "boolean"
    description: "Indicates if a PayPal link should be included with the invoice message."

  - name: "sent_from_email"
    type: "string"
    description: "The email address the invoice message was sent from."

  - name: "sent_from"
    type: "string"
    description: "The name of the user who sent the invoice message."

  - name: "send_reminder_on"
    type: "date-time"
    description: "The date that a reminder should be sent."

  - name: "full_recipient_list"
    type: "string"
    description: "The list of recipients who should receive the invoice message."
---