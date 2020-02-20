---
tap: "chargebee"
version: "1"
key: "payment-source"

name: "payment_sources"
doc-link: "https://apidocs.chargebee.com/docs/api/payment_sources"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/payment_sources.json"
description: |
  The `{{ table.name }}` table contains info about customer payment sources.

replication-method: "Key-based Incremental"

api-method:
    name: "List payment sources"
    doc-link: "https://apidocs.chargebee.com/docs/api/payment_sources#list_payment_sources"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The payment source ID."
    foreign-key-id: "payment-source-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the payment source was last updated."

  - name: "amazon_payment"
    type: "object"
    description: "Amazon payment details associated with the payment source."
    subattributes:
      - name: "agreement_id"
        type: "string"
        description: "The billing agreement ID."

      - name: "email"
        type: "string"
        description: "The email address associated with the Amazon payment account."

  - name: "bank_account"
    type: "object"
    description: "The bank account details, direct debit, or ACH agreement/mandate associated with the payment source."
    subattributes:
      - name: "account_holder_type"
        type: "string"
        description: |
          **Applicable to Stripe ACH users only**. Indicates the account holder type. Possible values are:

          - `individual`
          - `company`

      - name: "account_type"
        type: "string"
        description: |
          **Applicable to Authorze.net ACH users only**. Indicates the type of account. Possible values are:

          - `checking`
          - `savings`

      - name: "bank_name"
        type: "string"
        description: "The name of the account holder's bank."

      - name: "echeck_type"
        type: "string"
        description: |
          **Applicable to Authorze.net ACH users only**. Indicates the type of eCheck. Possible values are:

          - `web`
          - `ppd`

      - name: "last4"
        type: "string"
        description: "The last four digits of the bank account number."

      - name: "mandate_id"
        type: "string"
        description: ""

      - name: "name_on_account"
        type: "string"
        description: "The account holder's name on the bank account."

  - name: "card"
    type: "object"
    description: "Card details associated with the payment source."
    subattributes:
      - name: "billing_addr1"
        type: "string"
        description: "The first line of the billing address."

      - name: "billing_addr2"
        type: "string"
        description: "The second line of the billing address."

      - name: "billing_city"
        type: "string"
        description: "The billing city."

      - name: "billing_country"
        type: "string"
        description: "The billing country."

      - name: "billing_state"
        type: "string"
        description: "The billing state."

      - name: "billing_state_code"
        type: "string"
        description: "The ISO 3166-2 state/province code without the country prefix. Currently supported by {{ integration.display_name }} for USA, Canada and India."

      - name: "billing_zip"
        type: "string"
        description: "The billing zip or postal code."

      - name: "brand"
        type: "string"
        description: |
          The card brand. Possible values are:

          - `visa`
          - `mastercard`
          - `american_express`
          - `discover`
          - `jcb`
          - `diners_club`
          - `other`

      - name: "expiry_month"
        type: "integer"
        description: "The card's expiry month."

      - name: "expiry_year"
        type: "integer"
        description: "The card's expiry year."

      - name: "first_name"
        type: "string"
        description: "The first name of the cardholder."

      - name: "funding_type"
        type: "string"
        description: |
          The card's funding type. Possible values are:

          - `credit`
          - `debit`
          - `prepaid`
          - `not_known`

      - name: "iin"
        type: "string"
        description: "The Issuer Identification Number, or the first six digits of the card number."

      - name: "last4"
        type: "string"
        description: "The last four digits of the card number."

      - name: "last_name"
        type: "string"
        description: "The last name of the card holder."

      - name: "masked_number"
        type: "string"
        description: "The masked credit card number."

  - name: "created_at"
    type: "date-time"
    description: "The time the payment source was created."

  - name: "customer_id"
    type: "string"
    description: "The ID of the customer associated with the payment source."
    foreign-key-id: "customer-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the payment source has been deleted or not."

  - name: "gateway"
    type: "string"
    description: |
      The name of the gateway the payment source is stored with. Refer to [{{ integration.display_name }}'s documentation](https://apidocs.chargebee.com/docs/api/payment_sources#payment_source_gateway){:target="new"} for a full list of possible values.

  - name: "gateway_account_id"
    type: "string"
    description: "The gateway account the payment source is stored with."

  - name: "ip_address"
    type: "string"
    description: "The IP address from where the payment source is created or updated. Used primarily for EU VAT validation."

  - name: "issuing_country"
    type: "string"
    description: "The two-letter ISO country code."

  - name: "object"
    type: "string"
    description: ""

  - name: "paypal"
    type: "object"
    description: "PayPal Express Checkout details associated with the payment source."
    subattributes:
      - name: "agremeent_id"
        type: "string"
        description: "The billing agreement ID."

      - name: "email"
        type: "string"
        description: "The email address associated with PayPal Express Checkout."

  - name: "reference_id"
    type: "string"
    description: |
      The reference ID.

      - For **Amazon** and **PayPal**, this will be the billing agreement ID.
      - For **GoCardless direct debit**, this will be the mandate ID.
      - For **card payments**, this will be the ID provided by the gateway/card vault for the specific payment method.

  - name: "resource_version"
    type: "integer"
    description: "The version number of the payment source. Each update of the payment source results in an incremental change of this value. **Note**: This attribute will be present only if the payment source has been updated after 2016-09-28."

  - name: "status"
    type: "string"
    description: |
      The current status of the payment method. Possible values include:

      - `valid`
      - `expiring`
      - `expired`
      - `invalid`
      - `pending_verification`

  - name: "type"
    type: "string"
    description: |
      The type of the payment source. Possible values include:

      - `card` (Includes credit and debit cards)
      - `paypal_express_checkout`
      - `amazon_payments`
      - `direct_debit`
      - `generic`
      - `alipay`
      - `unionpay`
      - `apple_pay`
      - `wechat_pay`
---