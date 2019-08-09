---
tap: "stripe"
version: "1.0"

name: "invoices"
doc-link: "https://stripe.com/docs/api/invoices"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about invoices. Invoices are statements of amounts owed by customers, which can be one-off charges or generated periodically from a subscription.

  #### Invoice line items

  Full records for the line items associated with an invoice can be found in the [`invoice_line_items`](#invoice_line_items) table. To replicate these records, you must set this table and the `invoice_line_items` table to replicate.

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

  - name: "date"
    type: "date-time"
    replication-key: true
    description: "The time at which the invoice was created. Measured in seconds since the Unix epoch."

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

  - name: "description"
    type: "string"
    description: "A description of the invoice."

  - name: "discount"
    type: "object"
    description: "Describes the current discount active on the invoice."
    subattributes:
      - name: "coupon"
        type: "object"
        description: "Details about the coupon applied to the invoice."
        subattributes:
          - name: "id"
            type: "string"
            description: "The coupon ID."
            foreign-key-id: "coupon-id"

          - name: "amount_off"
            type: "integer"
            description: "The amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer."

          - name: "created"
            type: "date-time"
            description: ""

          - name: "currency"
            type: "string"
            description: |
              The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"} of the amount to take off (`amount_off`).

          - name: "duration"
            type: "string"
            description: |
              Indicates how long a customer who applies this coupon will get the discount. Possible values are:

              - `forever`
              - `once`
              - `repeating`

          - name: "duration_in_months"
            type: "integer"
            description: "Indicates the number of months the coupon applies if `duration: repeating`."

          - name: "livemode"
            type: "boolean"
            description: "Indicates if the coupon exists in live mode (`true`) or in test mode (`false`)."

          - name: "max_redemptions"
            type: "integer"
            description: "The maximum number of times this coupon can be redeemed in total across all customers before it is no longer valid."

          - name: "metadata"
            type: "object"
            description: ""
            anchor-id: 1
            subattributes: &metadata
              - name: "ANYTHING"
                type: "ANYTHING"
                description: "This info will vary."

          - name: "name"
            type: "string"
            description: "The name of the coupon as it is displayed to customers."

          - name: "object"
            type: "string"
            description: "The type of {{ integration.display_name }} object. This will be `coupon`."

          - name: "percent_off"
            type: "integer"
            description: "The percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon."

          - name: "percent_off_precise"
            type: "number"
            description: ""

          - name: "redeem_by"
            type: "date-time"
            description: "The date afer which the coupon can no longer be redeemed."

          - name: "times_redeemed"
            type: "integer"
            description: "The number of times this coupon has been applied to a customer."

          - name: "valid"
            type: "boolean"
            description: "Taking into account all of the other coupon properties, indicates whether this coupon can still be applied to a customer."

      - name: "customer"
        type: "string"
        description: "The ID of the customer the discount applies to."
        foreign-key-id: "customer-id"

      - name: "end"
        type: "date-time"
        description: "If the coupon has a `duration` of `repeating`, the date that this discount will end. If the coupon has a `duration` of `once` or `forever`, this attribute will be null."

      - name: "object"
        type: "string"
        description: "The type of {{ integration.display_name }} object. This will be `discount`."

      - name: "start"
        type: "date-time"
        description: "Date that the coupon was applied."

      - name: "subscription"
        type: "string"
        description: "The subscription that this coupon is applied to, if it is applied to a particular subscription."
        foreign-key-id: "subscription-id"
        
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
    description: "The IDs of the line items that make up the invoice. Full details for these records are in the [`invoice_line_items`](#invoice_line_items) table."
    subattributes:
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
    anchor-id: 2
    subattributes: *metadata

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