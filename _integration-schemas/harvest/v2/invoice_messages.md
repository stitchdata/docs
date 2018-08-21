---
tap: "harvest"
version: "2.0"

name: "invoice_messages"
doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/invoice_messages.json
description: |
  The `{{ table.name }}` table contains info about invoice messages, or emails sent to clients about invoices.

replication-method: "Key-based Incremental"
api-method:
  name: List all messages for an invoice
  doc-link: https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the invoice message."
    foreign-key-id: "invoice-message-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the invoice message was last updated."

  - name: "sent_by"
    type: "string"
    description: "The name of the user who created the invoice message."

  - name: "sent_by_email"
    type: "string"
    description: "The email address of the user who created the invoice message."

  - name: "sent_from"
    type: "string"
    description: "The name of the user who sent the invoice message."

  - name: "sent_from_email"
    type: "string"
    description: "The email address the invoice message was sent from."

  - name: "subject"
    type: "string"
    description: "The subject of the invoice message."

  - name: "body"
    type: "string"
    description: "The body of the invoice message."

  - name: "include_link_to_client_invoice"
    type: "boolean"
    description: "If `true`, a link to the client invoice was included in the message body."

  - name: "attach_pdf"
    type: "boolean"
    description: "If `true`, a PDF of the invoice was attached to the message."

  - name: "send_me_a_copy"
    type: "boolean"
    description: "If `true`, a copy will be emailed to the current user."

  - name: "thank_you"
    type: "boolean"
    description: "Indicates if this is a `thank you` message."

  - name: "event_type"
    type: "string"
    description: |
      The type of event that occurred with the message. Possible values are:

      - `send`
      - `close`
      - `draft`
      - `re-open`
      - `view`

  - name: "reminder"
    type: "boolean"
    description: "If `true`, this is a reminder message."

  - name: "send_reminder_on"
    type: "date-time"
    description: "The date that a reminder should be sent."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice message was created."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the invoice message."
    foreign-key-id: "invoice-id"

  - name: "recipients"
    type: "object"
    description: "Details about the recipients of the message."
    object-attributes:
      - name: "name"
        type: "string"
        description: "The name of the message recipient."

      - name: "email"
        type: "string"
        description: "The email address of the message recipient."
---