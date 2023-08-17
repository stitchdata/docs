---
tap: "stripe"
version: "3"
key: ""

name: "customers"
doc-link: "https://stripe.com/docs/api/customers/object"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/customers.json
description: |
  The `{{ table.name }}` table contains info about your customers.

replication-method: "Key-based Incremental"

api-method:
    name: "List all customers"
    doc-link: "https://stripe.com/docs/api/customers/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "created"
    type: "string"
    replication-key: true
    description: "Time at which the object was created. Measured in seconds since the Unix epoch."  

  - name: "account_balance"
    type: "integer"
    description: ""

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


  - name: "balance"
    type: "integer"
    description: ""

  - name: "cards"
    type: "array"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "object"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "exp_month"
      type: "integer"
      description: ""

    - name: "dynamic_last4"
      type: "string"
      description: ""

    - name: "exp_year"
      type: "integer"
      description: ""

    - name: "last4"
      type: "string"
      description: ""

    - name: "funding"
      type: "string"
      description: ""

    - name: "brand"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "customer"
      type: "string"
      description: ""

    - name: "cvc_check"
      type: "string"
      description: ""

    - name: "address_line2"
      type: "string"
      description: ""

    - name: "address_line1"
      type: "string"
      description: ""

    - name: "fingerprint"
      type: "string"
      description: ""

    - name: "address_zip"
      type: "string"
      description: ""

    - name: "address_city"
      type: "string"
      description: ""

    - name: "address_country"
      type: "string"
      description: ""

    - name: "address_line1_check"
      type: "string"
      description: ""

    - name: "tokenization_method"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "address_state"
      type: "string"
      description: ""

    - name: "address_zip_check"
      type: "string"
      description: ""

    - name: "type"
      type: "string"
      description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "default_card"
    type: "string"
    description: ""

  - name: "default_source"
    type: "string"
    description: ""

  - name: "delinquent"
    type: "boolean"
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
        description: "The ID of the discount object. "

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
      description: ""

    - name: "start"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "subscription"
      type: "string"
      description: ""

    - name: "checkout_session"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: "The ID of the discount object. "

    - name: "invoice"
      type: "string"
      description: "The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice."

    - name: "invoice_item"
      type: "string"
      description: "The invoice item id (or invoice line item id for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item."

    - name: "promotion_code"
      type: "string"
      description: "The promotion code applied to create this discount."


  - name: "email"
    type: "string"
    description: ""

  - name: "invoice_prefix"
    type: "string"
    description: ""

  - name: "invoice_settings"
    type: "object"
    description: ""
    subattributes:
    - name: "custom_fields"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

    - name: "default_payment_method"
      type: "string"
      description: ""

    - name: "footer"
      type: "string"
      description: ""


  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "name"
    type: "string"
    description: ""

  - name: "next_invoice_sequence"
    type: "integer"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "preferred_locales"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "shipping"
    type: "object"
    description: ""
    subattributes:
    - name: "address"
      type: "object"
      description: ""
      subattributes:
      - name: "line2"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "line1"
        type: "string"
        description: ""


    - name: "name"
      type: "string"
      description: ""

    - name: "phone"
      type: "string"
      description: ""


  - name: "sources"
    type: "array"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "type"
      type: "string"
      description: ""

    - name: "address_zip"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "card"
      type: "object"
      description: ""
      subattributes:
      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "three_d_secure"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""


    - name: "statement_descriptor"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "address_country"
      type: "string"
      description: ""

    - name: "funding"
      type: "string"
      description: ""

    - name: "dynamic_last4"
      type: "string"
      description: ""

    - name: "exp_year"
      type: "integer"
      description: ""

    - name: "last4"
      type: "string"
      description: ""

    - name: "exp_month"
      type: "integer"
      description: ""

    - name: "brand"
      type: "string"
      description: ""

    - name: "address_line2"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""

    - name: "cvc_check"
      type: "string"
      description: ""

    - name: "usage"
      type: "string"
      description: ""

    - name: "address_line1"
      type: "string"
      description: ""

    - name: "owner"
      type: "object"
      description: ""
      subattributes:
      - name: "verified_address"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "address"
        type: "object"
        description: ""
        subattributes:
        - name: "line2"
          type: "string"
          description: ""

        - name: "state"
          type: "string"
          description: ""

        - name: "city"
          type: "string"
          description: ""

        - name: "postal_code"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "line1"
          type: "string"
          description: ""


      - name: "verified_email"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "verified_name"
        type: "string"
        description: ""

      - name: "verified_phone"
        type: "string"
        description: ""


    - name: "tokenization_method"
      type: "string"
      description: ""

    - name: "client_secret"
      type: "string"
      description: ""

    - name: "fingerprint"
      type: "string"
      description: ""

    - name: "address_city"
      type: "string"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "address_line1_check"
      type: "string"
      description: ""

    - name: "receiver"
      type: "object"
      description: ""
      subattributes:
      - name: "refund_attributes_method"
        type: "string"
        description: ""

      - name: "amount_returned"
        type: "integer"
        description: ""

      - name: "amount_received"
        type: "integer"
        description: ""

      - name: "refund_attributes_status"
        type: "string"
        description: ""

      - name: "address"
        type: "string"
        description: ""

      - name: "amount_charged"
        type: "integer"
        description: ""


    - name: "flow"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "ach_credit_transfer"
      type: "object"
      description: ""
      subattributes:
      - name: "bank_name"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "routing_number"
        type: "string"
        description: ""

      - name: "swift_code"
        type: "string"
        description: ""

      - name: "refund_account_holder_type"
        type: "string"
        description: ""

      - name: "refund_account_holder_name"
        type: "string"
        description: ""

      - name: "refund_account_number"
        type: "string"
        description: ""

      - name: "refund_routing_number"
        type: "string"
        description: ""

      - name: "account_number"
        type: "string"
        description: ""


    - name: "customer"
      type: "string"
      description: ""

    - name: "address_zip_check"
      type: "string"
      description: ""

    - name: "status"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "address_state"
      type: "string"
      description: ""

    - name: "alipay"
      type: "object"
      description: ""
      subattributes:

    - name: "bancontact"
      type: "object"
      description: ""
      subattributes:

    - name: "eps"
      type: "object"
      description: ""
      subattributes:

    - name: "ideal"
      type: "object"
      description: ""
      subattributes:

    - name: "multibanco"
      type: "object"
      description: ""
      subattributes:

    - name: "redirect"
      type: "object"
      description: ""
      subattributes:
      - name: "failure_reason"
        type: "string"
        description: ""

      - name: "return_url"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""




  - name: "sources"
    type: "object"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "type"
      type: "string"
      description: ""

    - name: "address_zip"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "card"
      type: "object"
      description: ""
      subattributes:
      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "last4"
        type: "string"
        description: ""

      - name: "dynamic_last4"
        type: "string"
        description: ""

      - name: "address_line1_check"
        type: "string"
        description: ""

      - name: "exp_month"
        type: "integer"
        description: ""

      - name: "tokenization_method"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "exp_year"
        type: "integer"
        description: ""

      - name: "three_d_secure"
        type: "string"
        description: ""

      - name: "funding"
        type: "string"
        description: ""

      - name: "brand"
        type: "string"
        description: ""

      - name: "cvc_check"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "address_zip_check"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""


    - name: "statement_descriptor"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "address_country"
      type: "string"
      description: ""

    - name: "funding"
      type: "string"
      description: ""

    - name: "dynamic_last4"
      type: "string"
      description: ""

    - name: "exp_year"
      type: "integer"
      description: ""

    - name: "last4"
      type: "string"
      description: ""

    - name: "exp_month"
      type: "integer"
      description: ""

    - name: "brand"
      type: "string"
      description: ""

    - name: "address_line2"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""

    - name: "cvc_check"
      type: "string"
      description: ""

    - name: "usage"
      type: "string"
      description: ""

    - name: "address_line1"
      type: "string"
      description: ""

    - name: "owner"
      type: "object"
      description: ""
      subattributes:
      - name: "verified_address"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "address"
        type: "object"
        description: ""
        subattributes:
        - name: "line2"
          type: "string"
          description: ""

        - name: "state"
          type: "string"
          description: ""

        - name: "city"
          type: "string"
          description: ""

        - name: "postal_code"
          type: "string"
          description: ""

        - name: "country"
          type: "string"
          description: ""

        - name: "line1"
          type: "string"
          description: ""


      - name: "verified_email"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "verified_name"
        type: "string"
        description: ""

      - name: "verified_phone"
        type: "string"
        description: ""


    - name: "tokenization_method"
      type: "string"
      description: ""

    - name: "client_secret"
      type: "string"
      description: ""

    - name: "fingerprint"
      type: "string"
      description: ""

    - name: "address_city"
      type: "string"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "address_line1_check"
      type: "string"
      description: ""

    - name: "receiver"
      type: "object"
      description: ""
      subattributes:
      - name: "refund_attributes_method"
        type: "string"
        description: ""

      - name: "amount_returned"
        type: "integer"
        description: ""

      - name: "amount_received"
        type: "integer"
        description: ""

      - name: "refund_attributes_status"
        type: "string"
        description: ""

      - name: "address"
        type: "string"
        description: ""

      - name: "amount_charged"
        type: "integer"
        description: ""


    - name: "flow"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "ach_credit_transfer"
      type: "object"
      description: ""
      subattributes:
      - name: "bank_name"
        type: "string"
        description: ""

      - name: "fingerprint"
        type: "string"
        description: ""

      - name: "routing_number"
        type: "string"
        description: ""

      - name: "swift_code"
        type: "string"
        description: ""

      - name: "refund_account_holder_type"
        type: "string"
        description: ""

      - name: "refund_account_holder_name"
        type: "string"
        description: ""

      - name: "refund_account_number"
        type: "string"
        description: ""

      - name: "refund_routing_number"
        type: "string"
        description: ""

      - name: "account_number"
        type: "string"
        description: ""


    - name: "customer"
      type: "string"
      description: ""

    - name: "address_zip_check"
      type: "string"
      description: ""

    - name: "status"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "address_state"
      type: "string"
      description: ""

    - name: "alipay"
      type: "object"
      description: ""
      subattributes:

    - name: "bancontact"
      type: "object"
      description: ""
      subattributes:

    - name: "eps"
      type: "object"
      description: ""
      subattributes:

    - name: "ideal"
      type: "object"
      description: ""
      subattributes:

    - name: "multibanco"
      type: "object"
      description: ""
      subattributes:

    - name: "redirect"
      type: "object"
      description: ""
      subattributes:
      - name: "failure_reason"
        type: "string"
        description: ""

      - name: "return_url"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""




  - name: "subscriptions"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "tax_exempt"
    type: "string"
    description: ""

  - name: "tax_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "id"
      type: "string"
      description: "Unique identifier for the object."

    - name: "object"
      type: "string"
      description: "String representing the object’s type. Objects of the same type share the same value."

    - name: "country"
      type: "string"
      description: "Two-letter ISO code representing the country of the tax ID."

    - name: "created"
      type: "string"
      description: "Time at which the object was created. Measured in seconds since the Unix epoch."

    - name: "customer"
      type: "string"
      description: "ID of the customer."

    - name: "livemode"
      type: "boolean"
      description: "Has the value true if the object exists in live mode or the value false if the object exists in test mode"

    - name: "type"
      type: "string"
      description: "Type of the tax ID."

    - name: "value"
      type: "string"
      description: "Value of the tax ID"

    - name: "verification"
      type: "object"
      description: "Tax ID verification information."
      subattributes:
      - name: "status"
        type: "string"
        description: ""

      - name: "verified_address"
        type: "string"
        description: ""

      - name: "verified_name"
        type: "string"
        description: ""




  - name: "tax_ids"
    type: "object"
    description: ""
    subattributes:
    - name: "id"
      type: "string"
      description: "Unique identifier for the object."

    - name: "object"
      type: "string"
      description: "String representing the object’s type. Objects of the same type share the same value."

    - name: "country"
      type: "string"
      description: "Two-letter ISO code representing the country of the tax ID."

    - name: "created"
      type: "string"
      description: "Time at which the object was created. Measured in seconds since the Unix epoch."

    - name: "customer"
      type: "string"
      description: "ID of the customer."

    - name: "livemode"
      type: "boolean"
      description: "Has the value true if the object exists in live mode or the value false if the object exists in test mode"

    - name: "type"
      type: "string"
      description: "Type of the tax ID."

    - name: "value"
      type: "string"
      description: "Value of the tax ID"

    - name: "verification"
      type: "object"
      description: "Tax ID verification information."
      subattributes:
      - name: "status"
        type: "string"
        description: ""

      - name: "verified_address"
        type: "string"
        description: ""

      - name: "verified_name"
        type: "string"
        description: ""




  - name: "tax_info"
    type: "string"
    description: ""

  - name: "tax_info_verification"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---