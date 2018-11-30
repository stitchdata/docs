---
tap: "stripe"
version: "1.0"

name: "invoices"
doc-link: "https://stripe.com/docs/api/invoices"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about invoices. Invoices are statements of amounts owed by customers, which can be one-off charges or generated periodically from a subscription.

replication-method: "Key-based Incremental"

api-method:
    name: "List all invoices"
    doc-link: "https://stripe.com/docs/api/invoices/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "amount_due"
    type: "integer"
    description: |
      The final amount due at the time of the invoice.

  - name: "amount_paid"
    type: "integer"
    description: "The amount (in cents) that was paid."

  - name: "amount_remaining"
    type: "integer"
    description: "The amount remaining (in cents) that is due."

  - name: "application_fee"
    type: "integer"
    description: "The fee (in cents) that will be applied to the invoice and transfered to the application owner's {{ integration.display_name }} account when the invoice is paid."

  - name: "attempt_count"
    type: "integer"
    description: "The number of payment attempts made for this invoice, from the perspective of the payment retry schedule."

  - name: "attempted"
    type: "boolean"
    description: "Indicates whether an attempt has been made to pay the invoice."

  - name: "auto_advance"
    type: "boolean"
    description: "Indicates whether {{ integration.display_name }} will perform automatic collection of the invoice."

  - name: "billing"
    type: "string"
    description: |
      The type of billing action performed by {{ integration.display_name }} to pay the invoice. Possible values are:

      - `charge_automatically` - {{ integration.display_name }} will attempt to pay the invoice using the default source attached to the customer.
      - `send_invoice` - {{ integration.display_name }} will email this invoice to the customer with payment instructions.

  - name: "billing_reason"
    type: "string"
    description: |
      Indicates why the invoice was created. Possible values are:

      - `subscription_cycle` - Indicates an invoice was created by a subscription advancing into a new period.
      - `subscription_update` - Indicates an invoice was created due to creating or updating a subscription.
      - `subscription` - Set for all old invoices to indicate either a change to a subscription or a period advancement.
      - `manual` - Set for all invoices unrelated to a subscription.
      - `upcoming` - Reserved for simulated invoices.

  - name: "charge"
    type: "string"
    description: "The ID of the latest charge generated for this invoice."
    foreign-key-id: "charge-id"

  - name: "closed"
    type: "boolean"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}.

  - name: "customer"
    type: "string"
    description: "The ID of the customer associated with the invoice."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: "A description of the invoice."

  - name: "discount"
    type: "object"
    description: ""
    object-attributes:
        
  - name: "due_date"
    type: "date-time"
    description: "The date on which payment for the invoice is due."

  - name: "ending_balance"
    type: "integer"
    description: "The ending customer balance after the invoice is finalized."

  - name: "forgiven"
    type: "boolean"
    description: ""

  - name: "hosted_invoice_url"
    type: "string"
    description: "The URL for the hosted invoice page, which allows customers to view and pay the invoice."

  - name: "invoice_pdf"
    type: "string"
    description: "The link to download the PDF for the invoice."

  - name: "lines"
    type: "array"
    description: "Details about the individual line items that make up the invoice."
    array-attributes:
      - name: "value"
        type: "string"
        primary-key: true
        description: "The ID of the line item."
        foreign-key-id: "invoice-line-item-id"

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: "Additional information attached to the invoice."
    object-attributes:
      - name: "TODO"
        type: 
        description: ""

  - name: "next_payment_attempt"
    type: "date-time"
    description: "The time at which the next payment will be attempted."

  - name: "number"
    type: "string"
    description: "A unique ID that appears on email sent to the customer for the invoice. This value begins with the customer's unique `invoice_prefix`, if specified."

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `invoice`."

  - name: "paid"
    type: "boolean"
    description: "Indicates whether payment was successfully collected for this invoice."

  - name: "payment"
    type: "string"
    description: ""

  - name: "period_end"
    type: "date-time"
    description: "The end of the usage period during which invoice items were added to this invoice."

  - name: "period_start"
    type: "date-time"
    description: "The start of the usage period during which invoice items were added to this invoice."

  - name: "receipt_number"
    type: "string"
    description: "The transaction number that appears on email receipts sent for this invoice."

  - name: "starting_balance"
    type: "integer"
    description: "The starting customer balance before the invoice is finalized."

  - name: "statement_description"
    type: "string"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "statement_descriptor"
    type: "string"
    description: "Additional information about the invoice. This appears on the customer's credit card statement."

  - name: "subscription"
    type: "string"
    description: "The ID that the invoice was prepared for."
    foreign-key-id: "subscription-id"

  - name: "subtotal"
    type: "integer"
    description: "The total of all subscriptions, invoice items, and prorations on the invoice before any discount is applied."

  - name: "tax"
    type: "integer"
    description: "The amount of tax included in the total, calculated from `tax_percent` and the `subtotal`."

  - name: "tax_percent"
    type: "number"
    description: "The percentage of the subtotal that has been added to the total amount of the invoice, including invoice line items and discounts. This field is inheirited from the `subscription`'s `tax_percent` attribute."

  - name: "total"
    type: "integer"
    description: "The total of the invoice after any discounts."

  - name: "updated"
    type: "date-time"
    description: "The time the invoice was last updated."

  - name: "webhooks_delivered_at"
    type: "date-time"
    description: "The time at which webhooks for this invoice were successfully delivered."
---