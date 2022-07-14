---
tap: "stripe"
version: "2"
key: ""

name: "invoices"
doc-link: "https://stripe.com/docs/api/invoices" 
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/invoices.json
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

  - name: "created"
    type: "string"
    replication-key: true
    description: "The time at which the invoice was created. Measured in seconds since the Unix epoch."

  - name: "account_country"
    type: "string"
    description: ""

  - name: "account_name"
    type: "string"
    description: ""

  - name: "account_tax_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "amount_due"
    type: "integer"
    description: ""

  - name: "amount_paid"
    type: "integer"
    description: ""

  - name: "amount_remaining"
    type: "integer"
    description: ""

  - name: "application_fee"
    type: "integer"
    description: ""

  - name: "application_fee_amount"
    type: "integer"
    description: "The fee in cents that will be applied to the invoice and transferred to the application owner’s Stripe account when the invoice is paid."

  - name: "attempt_count"
    type: "integer"
    description: ""

  - name: "attempted"
    type: "boolean"
    description: ""

  - name: "auto_advance"
    type: "boolean"
    description: ""

  - name: "automatic_tax"
    type: "object"
    description: "Settings and latest results for automatic tax lookup for this invoice."
    subattributes:
    - name: "enabled"
      type: "boolean"
      description: "Whether Stripe automatically computes tax on this invoice."

    - name: "status"
      type: "string"
      description: "The status of the most recent automated tax calculation for this invoice."


  - name: "billing"
    type: "string"
    description: ""

  - name: "billing_reason"
    type: "string"
    description: ""

  - name: "charge"
    type: "string"
    description: "The ID of the latest charge generated for this invoice."
    foreign-key-id: "charge-id"

  - name: "closed"
    type: "boolean"
    description: ""

  - name: "collection_method"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "custom_fields"
    type: "array"
    description: "Custom fields displayed on the invoice."
    subattributes:
    - name: "name"
      type: "string"
      description: "The name of the custom field."

    - name: "value"
      type: "string"
      description: "The value of the custom field."


  - name: "customer"
    type: "string"
    description: "The ID of the customer associated with the invoice."
    foreign-key-id: "customer-id"

  - name: "customer_address"
    type: "object"
    description: ""
    subattributes:
    - name: "city"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "line1"
      type: "string"
      description: ""

    - name: "line2"
      type: "string"
      description: ""

    - name: "postal_code"
      type: "string"
      description: ""

    - name: "state"
      type: "string"
      description: ""


  - name: "customer_email"
    type: "string"
    description: ""

  - name: "customer_name"
    type: "string"
    description: ""

  - name: "customer_phone"
    type: "string"
    description: ""

  - name: "customer_shipping"
    type: "object"
    description: ""
    subattributes:
    - name: "address"
      type: "object"
      description: ""
      subattributes:
      - name: "city"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "line1"
        type: "string"
        description: ""

      - name: "line2"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""


    - name: "name"
      type: "string"
      description: ""

    - name: "phone"
      type: "string"
      description: ""


  - name: "customer_tax_exempt"
    type: "string"
    description: ""

  - name: "customer_tax_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "type"
      type: "string"
      description: ""

    - name: "value"
      type: "string"
      description: ""


  - name: "date"
    type: "string"
    description: ""

  - name: "default_payment_method"
    type: "string"
    description: ""

  - name: "default_source"
    type: "string"
    description: ""

  - name: "default_tax_rates"
    type: "array"
    description: ""
    subattributes:
    - name: "id"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "active"
      type: "boolean"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "description"
      type: "string"
      description: ""

    - name: "display_name"
      type: "string"
      description: ""

    - name: "inclusive"
      type: "boolean"
      description: ""

    - name: "jurisdiction"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "metadata"
      type: "object"
      description: ""

    - name: "percentage"
      type: "string"
      description: ""

    - name: "state"
      type: "string"
      description: ""


  - name: "description"
    type: "string"
    description: ""

  - name: "discount"
    type: "object"
    description: ""
    subattributes:
    - name: "end"
      type: "string"
      description: ""

    - name: "coupon"
      type: "object"
      description: ""
      subattributes:
      - name: "metadata"
        type: "object"
        description: ""
        subattributes:

      - name: "valid"
        type: "boolean"
        description: ""

      - name: "livemode"
        type: "boolean"
        description: ""

      - name: "amount_off"
        type: "integer"
        description: ""

      - name: "redeem_by"
        type: "string"
        description: ""

      - name: "duration_in_months"
        type: "integer"
        description: ""

      - name: "percent_off_precise"
        type: "number"
        description: ""

      - name: "max_redemptions"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "times_redeemed"
        type: "integer"
        description: ""

      - name: "id"
        type: "string"
        description: "The coupon ID."
        foreign-key-id: "coupon-id"

      - name: "duration"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "percent_off"
        type: "number"
        description: ""

      - name: "created"
        type: "string"
        description: ""


    - name: "customer"
      type: "string"
      description: "The ID of the customer the discount applies to."
      foreign-key-id: "customer-id"

    - name: "start"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "subscription"
      type: "string"
      description: "The subscription that this coupon is applied to, if it is applied to a particular subscription."
      foreign-key-id: "subscription-id"

    - name: "checkout_session"
      type: "string"
      description: "The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode."

    - name: "id"
      type: "string"
      description: "The ID of the discount object."

    - name: "invoice"
      type: "string"
      description: "The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice."

    - name: "invoice_item"
      type: "string"
      description: "The invoice item id (or invoice line item id for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item."

    - name: "promotion_code"
      type: "string"
      description: "The promotion code applied to create this discount."


  - name: "discounts"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "due_date"
    type: "string"
    description: ""

  - name: "ending_balance"
    type: "integer"
    description: ""

  - name: "finalized_at"
    type: "string"
    description: ""

  - name: "footer"
    type: "string"
    description: ""

  - name: "forgiven"
    type: "boolean"
    description: ""

  - name: "hosted_invoice_url"
    type: "string"
    description: ""

  - name: "invoice_pdf"
    type: "string"
    description: ""

  - name: "last_finalization_error"
    type: "object"
    description: ""
    subattributes:
    - name: "code"
      type: "string"
      description: ""

    - name: "doc_url"
      type: "string"
      description: ""

    - name: "message"
      type: "string"
      description: ""

    - name: "param"
      type: "string"
      description: ""

    - name: "payment_method_type"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""


  - name: "lines"
    type: "array, object"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "next_payment_attempt"
    type: "string"
    description: ""

  - name: "number"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "on_behalf_of"
    type: "string, object"
    description: "The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account."
    subattributes:

  - name: "paid"
    type: "boolean"
    description: ""

  - name: "paid_out_of_band"
    type: "boolean"
    description: "Returns true if the invoice was manually marked paid, returns false if the invoice hasn’t been paid yet or was paid on Stripe."

  - name: "payment"
    type: "string"
    description: ""

  - name: "payment_intent"
    type: "string"
    description: ""

  - name: "payment_settings"
    type: "object"
    description: "Configuration settings for the PaymentIntent that is generated when the invoice is finalized."
    subattributes:
    - name: "payment_method_options"
      type: "object"
      description: "Payment-method-specific configuration to provide to the invoice’s PaymentIntent."
      subattributes:
      - name: "acss_debit"
        type: "object"
        description: ""
        subattributes:
        - name: "mandate_options"
          type: "object"
          description: ""
          subattributes:
          - name: "transaction_type"
            type: "string"
            description: ""


        - name: "verification_method"
          type: "string"
          description: ""


      - name: "bancontact"
        type: "object"
        description: ""
        subattributes:
        - name: "preferred_language"
          type: "string"
          description: ""


      - name: "card"
        type: "object"
        description: ""
        subattributes:
        - name: "request_three_d_secure"
          type: "string"
          description: ""



    - name: "payment_method_types"
      type: "array"
      description: "The list of payment method types (e.g. card) to provide to the invoice’s PaymentIntent"
      subattributes:
      - name: "items"
        type: "string"
        description: ""


  - name: "period_end"
    type: "string"
    description: ""

  - name: "period_start"
    type: "string"
    description: ""

  - name: "post_payment_credit_notes_amount"
    type: "integer"
    description: ""

  - name: "pre_payment_credit_notes_amount"
    type: "integer"
    description: ""

  - name: "quote"
    type: "object, string"
    description: "The quote this invoice was generated from."
    subattributes:

  - name: "receipt_number"
    type: "string"
    description: ""

  - name: "starting_balance"
    type: "integer"
    description: ""

  - name: "statement_description"
    type: "string"
    description: ""

  - name: "statement_descriptor"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "status_transitions"
    type: "object"
    description: ""
    subattributes:
    - name: "finalized_at"
      type: "string"
      description: ""

    - name: "marked_uncollectible_at"
      type: "string"
      description: ""

    - name: "paid_at"
      type: "string"
      description: ""

    - name: "voided_at"
      type: "string"
      description: ""


  - name: "subscription"
    type: "string"
    description: "The ID that the invoice was prepared for."
    foreign-key-id: "subscription-id"

  - name: "subtotal"
    type: "integer"
    description: ""

  - name: "tax"
    type: "integer"
    description: ""

  - name: "tax_percent"
    type: "number"
    description: ""

  - name: "total"
    type: "integer"
    description: ""

  - name: "total_discount_amounts"
    type: "array"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "discount"
      type: "string"
      description: ""


  - name: "total_tax_amounts"
    type: "array"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "inclusive"
      type: "boolean"
      description: ""

    - name: "tax_rate"
      type: "string"
      description: ""


  - name: "transfer_data"
    type: "object"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "destination"
      type: "string"
      description: ""


  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"

  - name: "webhooks_delivered_at"
    type: "string"
    description: ""
---