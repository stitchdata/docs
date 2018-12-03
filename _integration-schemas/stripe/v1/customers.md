---
tap: "stripe"
version: "1.0"

name: "customers"
doc-link: "https://stripe.com/docs/api/customers/object"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/customers.json"
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
    type: "date-time"
    replication-key: true
    description: "Time at which the object was created. Measured in seconds since the Unix epoch."

  - name: "account_balance"
    type: "integer"
    description: "The current balance, if any, being stored on the customer's account."

  - name: "cards"
    type: "array"
    description: "Details about the customer's cards."
    array-attributes: &card-attributes
      - name: "id"
        type: "string"
        description: "The card ID."

      - name: "address_city"
        type: "string"
        description: &address-city "The city associated with the card's billing address."

      - name: "address_country"
        type: "string"
        description: &address-country "The billing address country."

      - name: "address_line1"
        type: "string"
        description: &address-line1 "The first line of the billing address."

      - name: "address_line1_check"
        type: "string"
        description: &address-line1-check |
          If `address_line1` was provided, the results of the check. Possible values are:

          - `pass`
          - `fail`
          - `unavailable`
          - `unchecked`

      - name: "address_line2"
        type: "string"
        description: &address-line2 "The second line of the billing address."

      - name: "address_state"
        type: "string"
        description: &address-state "The state/county/province/region of the billing address."

      - name: "address_zip"
        type: "string"
        description: &address-zip "The zip or postal code of the billing address."

      - name: "address_zip_check"
        type: "string"
        description: &address-zip-check |
          If `address_zip` was provided, the results of the check. Possible values are:

          - `pass`
          - `fail`
          - `unavailable`
          - `unchecked`

      - name: "brand"
        type: "string"
        description: &brand |
          The brand of the card. Possible values are:

          - `American Express`
          - `Diners Club`
          - `Discover`
          - `JCB`
          - `MasterCard`
          - `UnionPay`
          - `Visa`
          - `Unknown`

      - name: "country"
        type: "string"
        description: &country "The two-letter ISO code representing the country of the card."

      - name: "customer"
        type: "string"
        description: "The ID of the customer that the card belongs to."
        foreign-key-id: "customer-id"

      - name: "cvc_check"
        type: "string"
        description: &cvc-check |
          If a CVC was provided, this will be the result of the check. Possible values are:

          - `pass`
          - `fail`
          - `unavailable`
          - `unchecked`

      - name: "dynamic_last4"
        type: "string"
        description: &dynamic-last4 "**For tokenized numbers only.** The last four digits of the device account number."

      - name: "exp_month"
        type: "integer"
        description: &exp-month "The two-digit number representing the card's expiration month."

      - name: "exp_year"
        type: "integer"
        description: &exp-year "The four-digit number representing the card's expiration year."

      - name: "fingerprint"
        type: "string"
        description: &fingerprint "A unique ID for the card number."

      - name: "funding"
        type: "string"
        description: &funding |
          The card's funding type. Possible values are:

          - `credit`
          - `debit`
          - `prepaid`
          - `unknown`

      - name: "last4"
        type: "string"
        description: &last4 "The last four digits of the card."

      - name: "metadata"
        type: "object"
        description: "Additional information attached to the card."
        object-attributes:
          - name: "TODO"
            type: 
            description: ""

      - name: "name"
        type: "string"
        description: &card-name "The name of the cardholder."

      - name: "object"
        type: "string"
        description: "The type of {{ integration.display_name }} object. This will be `card`."

      - name: "tokenization_method"
        type: "string"
        description: &tokenization-method |
          If the card number is tokenized, this is the method that was used. Possible values are:

          - `apple_pay`
          - `android_pay`

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"} the customer can be charged in for recurring billing purposes.

  - name: "default_card"
    type: "string"
    description: ""

  - name: "default_source"
    type: "string"
    description: "The ID of the default source attached to this customer."

  - name: "delinquent"
    type: "boolean"
    description: |
      When the customer's latest invoice is billed by charging automatically, this will be `true` if the invoice's latest charge failed.

      When the customer's latest invoice is billed by sending an invoice, this will be `true` if the invoice is not paid by its due date.

  - name: "description"
    type: "string"
    description: "The description of the customer."

  - name: "discount"
    type: "object"
    description: "Describes the current discount active on the customer."
    object-attributes:
      - name: "coupon"
        type: "object"
        description: "Details about the coupon applied to the customer."
        object-attributes:
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
            object-attributes:
              - name: ""
                type: ""
                description: ""

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

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "invoice_prefix"
    type: "string"
    description: "The prefix used to generate unique invoice numbers for the customer."

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the customer exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: ""
    object-attributes:
      - name: "TODO"
        type: ""
        description: ""

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `customer`."

  - name: "shipping"
    type: "object"
    description: "Mailing and shipping addresses for the customer. Appears on invoices emailed to this customer."
    object-attributes:
      - name: "address"
        type: "object"
        description: ""
        object-attributes:
          - name: "city"
            type: "string"
            description: "The city of the shipping address."

          - name: "country"
            type: "string"
            description: "The two-letter country code of the shipping address. For example: `us`"

          - name: "line1"
            type: "string"
            description: "The first address line of the shipping address."

          - name: "line2"
            type: "string"
            description: "The second address line of the shipping address."

          - name: "postal_code"
            type: "string"
            description: "The zip or postal code of the shipping address."

          - name: "state"
            type: "string"
            description: "The state, county, province, region, etc. of the shipping address"

      - name: "name"
        type: "string"
        description: "The recipient's name."

      - name: "phone"
        type: "string"
        description: "The recipient's phone number, including extension."

  - name: "sources"
    type: "array"
    description: "The customer's payment sources."
    doc-link: "https://stripe.com/docs/api/sources/object"
    array-attributes:
      - name: "ach_credit_transfer"
        type: "object"
        description: "If the source is an ACH credit transfer, this will contain the details about the ACH credit transfer source."
        doc-link: "https://stripe.com/docs/sources/ach-credit-transfer"
        object-attributes:
          - name: "account_number"
            type: "string"
            description: "A positive integer in the smallest currency unit (that is, `100` cents for `$1.00`, or `1 for `¥1`, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready."

          - name: "bank_name"
            type: "string"
            description: "The name of the bank the credit transfer should be sent to."

          - name: "fingerprint"
            type: "string"
            description: ""

          - name: "refund_account_holder_name"
            type: "string"
            description: ""

          - name: "refund_account_holder_type"
            type: "string"
            description: ""

          - name: "refund_account_number"
            type: "string"
            description: ""

          - name: "refund_routing_number"
            type: "string"
            description: ""

          - name: "routing_number"
            type: "string"
            description: "The routing number of the bank receiving the credit transfer."

          - name: "swift_code"
            type: "string"
            description: ""

      - name: "address_city"
        type: "string"
        description: *address-city

      - name: "address_country"
        type: "string"
        description: *address-country

      - name: "address_line1"
        type: "string"
        description: *address-line1

      - name: "address_line1_check"
        type: "string"
        description: *address-line1-check

      - name: "address_line2"
        type: "string"
        description: *address-line2

      - name: "address_state"
        type: "string"
        description: *address-state

      - name: "address_zip"
        type: "string"
        description: *address-zip

      - name: "address_zip_check"
        type: "string"
        description: *address-zip-check

      - name: "alipay"
        type: ""
        description: "If the source is an Alipay source, this will contain the details about the Alipay source."
        doc-link: "https://stripe.com/docs/sources/alipay"
        object-attributes:
          # - name: "TODO"
          #   type: ""
          #   description: ""

      - name: "amount"
        type: "integer"
        description: ""

      - name: "bancontact"
        type: ""
        description: "If the source is a Bancontact source, this will contain the details about the Bancontact source."
        doc-link: "https://stripe.com/docs/sources/bancontact"
        object-attributes:
          # - name: "TODO"
          #   type: ""
          #   description: ""

      - name: "brand"
        type: "string"
        description: *brand

      - name: "card"
        type: "object"
        description: "If the source is a card source, this will contain the details about the card source."
        object-attributes: *card-attributes

      - name: "client_secret"
        type: "string"
        description: "The client secret of the source. Used for client-side retrieval using a publishable key."

      - name: "country"
        type: "string"
        description: *country

      - name: "created"
        type: "date-time"
        description: "The time the source was created."

      - name: "currency"
        type: "string"
        description: |
          The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"} associated with the source.

      - name: "customer"
        type: "string"
        description: "The ID of the customer to which the source is attached."

      - name: "cvc_check"
        type: "string"
        description: *cvc-check

      - name: "dynamic_last4"
        type: "string"
        description: *dynamic-last4

      - name: "eps"
        type: ""
        description: "If the source is an EPS source, this will contain the details about the EPS source."
        doc-link: "https://stripe.com/docs/sources/eps"
        object-attributes:

      - name: "exp_month"
        type: "integer"
        description: *exp-month

      - name: "exp_year"
        type: "integer"
        description: *exp-year

      - name: "fingerprint"
        type: "string"
        description: *fingerprint

      - name: "flow"
        type: "string"
        description: |
          The authentication flow of the source. Possible values are:

          - `redirect`
          - `receiver`
          - `code_verification`
          - `none`

      - name: "funding"
        type: "string"
        description: *funding

      - name: "id"
        type: "string"
        description: "The source ID."

      - name: "ideal"
        type: "object"
        description: "If the source is an iDEAL source, this will contain the details about the iDEAL source."
        doc-link: "https://stripe.com/docs/sources/ideal"
        object-attributes:

      - name: "last4"
        type: "string"
        description: *last4

      - name: "livemode"
        type: "boolean"
        description: "Indicates if the source exists in live mode (`true`) or in test mode (`false`)."

      - name: "metadata"
        type: "object"
        description: ""
        object-attributes:

      - name: "multibanco"
        type: "object"
        description: ""
        doc-link: "https://stripe.com/docs/sources/multibanco"
        object-attributes:

      - name: "name"
        type: "string"
        description: *card-name

      - name: "object"
        type: "string"
        description: "The type of {{ integration.display_name }} object. This will be `source`."

      - name: "owner"
        type: "object"
        description: "Details about the owner of the payment instrument that may be used or required by particular source types."
        object-attributes:
          - name: "address"
            type: "object"
            description: "The owner's address."
            object-attributes:
              - name: "city"
                type: "string"
                description: "The city of the owner's address."

              - name: "country"
                type: "string"
                description: "The country of the owner's address."

              - name: "line1"
                type: "string"
                description: "The first line of the owner's address."

              - name: "line2"
                type: "string"
                description: "The second line of the owner's address."

              - name: "postal_code"
                type: "string"
                description: "The postal code of the owner's address."

              - name: "state"
                type: "string"
                description: "The state of the owner's address."

          - name: "email"
            type: "string"
            description: "The owner's email address."

          - name: "name"
            type: "string"
            description: "The owner's full name."

          - name: "phone"
            type: "string"
            description: "The owner's phone number."

          - name: "verified_address"
            type: "string"
            description: "The verified owner's address. Verified values are verified or provided by the payment directly at the time of authorization or settlement."

          - name: "verified_email"
            type: "string"
            description: "The verified owner's email address. Verified values are verified or provided by the payment directly at the time of authorization or settlement."

          - name: "verified_name"
            type: "string"
            description: "The verified owner's full name. Verified values are verified or provided by the payment directly at the time of authorization or settlement."

          - name: "verified_phone"
            type: "string"
            description: "The verified owner's phone number. Verified values are verified or provided by the payment directly at the time of authorization or settlement."

      - name: "receiver"
        type: "object"
        description: "Information related to the receiver flow. These attributes will be present if `flow: receiver`."
        object-attributes:
          - name: "address"
            type: "string"
            description: "The address of the receiver source. This is the value that should be communicated to the customer to send their funds to."

          - name: "amount_charged"
            type: "integer"
            description: "The total amount charged by you, expressed in the source's currency."

          - name: "amount_received"
            type: "integer"
            description: "The total amount received by the receiver source, expressed in the source's currency."

          - name: "amount_returned"
            type: "integer"
            description: "The total amount returned to the customer, expressed in the source's currency."

          - name: "refund_attributes_method"
            type: "string"
            description: ""

          - name: "refund_attributes_status"
            type: "string"
            description: ""

      - name: "redirect"
        type: "object"
        description: "Information related to the redirect flow. These attributes will be present if `flow: redirect`."
        object-attributes:
          - name: "failure_reason"
            type: "string"
            description: |
              The failure reason for the redirect. Possible values are:

              - `user_abort` - The customer aborted or dropped out of the redirect flow
              - `declined` - The authentication failed or the transaction was declined
              - `processing_error` - The redirect failed due to a technical error; only present if the redirect status is `failed`.

          - name: "return_url"
            type: "string"
            description: "The URL you provide to redirect the customer to after they authenticate their payment."

          - name: "status"
            type: "string"
            description: |
              The status of the redirect. Possible values are:

              - `pending` - Ready to be used by your customer to authenticate the transaction
              - `succeeded` - Successful authentication; cannot be reused
              - `not_required` - Redirect should not be used
              - `failed` - Failed authentication; cannot be reused

          - name: "url"
            type: "string"
            description: "The URL provided to you to redirect a customer as part of a redirect authentication flow."

      - name: "statement_descriptor"
        type: "string"
        description: "Extra information about a source. This will appear on your customer’s statement every time you charge the source."

      - name: "status"
        type: "string"
        description: |
          The status of the source. Possible values are:

          - `canceled`
          - `chargeable`
          - `consumed`
          - `failed`
          - `pending`

      - name: "tokenization_method"
        type: "string"
        description: *tokenization-method

      - name: "type"
        type: "string"
        description: |
          The type of the source. Possible values are:

          - `ach_credit_transfer`
          - `ach_debit`
          - `alipay`
          - `bancontact`
          - `card`
          - `card_present`
          - `eps`
          - `giropay`
          - `ideal`
          - `multibanco`
          - `p24`
          - `paper_check`
          - `sepa_credit_transfer`
          - `sepa_debit`
          - `sofort`
          - `three_d_secure`

      - name: "usage"
        type: "string"
        description: |
          Indicates if the source should be reusable or not. Some source types may or may not be reusable by construction, while others may leave the option at creation. Possible values are:

          - `reusable`
          - `single_use`

  - name: "subscriptions"
    type: "array"
    description: "The customer's current subscriptions."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The subscription ID."
        foreign-key-id: "subscription-id"

  - name: "tax_info"
    type: "string"
    description: ""

  - name: "tax_info_verification"
    type: "string"
    description: ""

  - name: "updated"
    type: "date-time"
    description: "The time at which the customer was last updated."
---