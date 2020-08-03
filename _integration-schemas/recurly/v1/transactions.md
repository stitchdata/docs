---
tap: "recurly"
version: "1"

name: "transactions"
key: "transaction"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/transactions.json"
description: |
  The `{{ table.name }}` table contains info about the transactions in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "List a site's transactions"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_transactions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The transaction ID."
    foreign-key-id: "transaction-id"

  - name: "collected_at"
    type: "date-time"
    replication-key: true
    description: "If collected, the date and time the transaction was collected. Otherwise, the time the transaction was created."

  - name: "account"
    type: "object"
    anchor-id: 1
    description: "Details about the account associated with the subscription."
    subattributes: &account
      - name: "bill_to"
        type: "string"
        description: |
          Indicates whether charges on the account are billed using the parent's billing info or the account itself. Possible values are:

          - `self` - The account itself.
          - `parent` - All invoices resulting in charges and credits originating from a child will be created on the parent account.

      - name: "code"
        type: "string"
        description: "The unique identifier for the account."

      - name: "company"
        type: "string"
        description: "The company."

      - name: "email"
        type: "string"
        description: "The email."

      - name: "first_name"
        type: "string"
        description: "The first name of the account."

      - name: "id"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

      - name: "last_name"
        type: "string"
        description: "The last name of the account."

      - name: "object"
        type: "string"
        description: "This will be `account`."

      - name: "parent_account_id"
        type: "string"
        description: "If this is a child account, this field will contain the ID of the parent account."
        foreign-key-id: "account-id"

  - name: "amount"
    type: "number"
    description: "The amount of the transaction."

  - name: "avs_check"
    type: "string"
    description: "The result from checking the overall AVS on the processed transaction."

  - name: "billing_address"
    type: "object"
    description: "The billing address for the transaction."
    subattributes:
      - name: "city"
        type: "string"
        description: "The city."

      - name: "country"
        type: "string"
        description: "The country."

      - name: "first_name"
        type: "string"
        description: "The first name on the address."

      - name: "last_name"
        type: "string"
        description: "The last name on the address."

      - name: "name_on_account"
        type: "string"
        description: "The name on the account."

      - name: "phone"
        type: "string"
        description: "The phone number."

      - name: "postal_code"
        type: "string"
        description: "The postal code."

      - name: "region"
        type: "string"
        description: "The region."

      - name: "street1"
        type: "string"
        description: "The first street line."

      - name: "street2"
        type: "string"
        description: "The second street line."

  - name: "collection_method"
    type: "string"
    description: |
      The method by which payment for the transaction was collected. Possible values are:

      - `automatic`
      - `manual`

  - name: "created_at"
    type: "date-time"
    description: "The date and time the transaction was created."

  - name: "currency"
    type: "string"
    description: "The three-letter 4217 ISO currency code."

  - name: "customer_message"
    type: "string"
    description: "For declined transactions, the message displayed to the customer."

  - name: "customer_message_locale"
    type: "string"
    description: "The language code used to display the `customer_message`."

  - name: "cvv_check"
    type: "string"
    description: "When processed, the result from checking the CVV/CVC value on the transaction."

  - name: "gateway_approval_code"
    type: "string"
    description: "The transaction approval code from the payment gateway."

  - name: "gateway_message"
    type: "string"
    description: "The transaction message from the payment gateway."

  - name: "gateway_reference"
    type: "string"
    description: "The transaction reference number from the payment gateway."

  - name: "gateway_response_code"
    type: "string"
    description: "The gateway error code for declined transactions (`success: false`)."

  - name: "gateway_response_time"
    type: "number"
    description: "The time, in seconds, for the gateway to process the transaction."

  - name: "gateway_response_values"
    type: "object"
    description: "The response values from the payment gateway."

  - name: "invoice"
    type: "object"
    description: "Details about the invoice associated with the transaction."
    subattributes: &mini-invoice
      - name: "id"
        type: "string"
        description: "The invoice ID."
        foreign-key-id: "invoice-id"

      - name: "number"
        type: "string"
        description: &number "The invoice number."

      - name: "object"
        type: "string"
        description: &object "This will be `invoice`."

      - name: "state"
        type: "string"
        description: &state |
          The state of the invoice. Possible values are:

          - `pending`
          - `processing`
          - `past_due`
          - `paid`
          - `failed`

      - name: "type"
        type: "string"
        description: &type |
          The type of the invoice. Possible values are:

          - `charge`
          - `credit`
          - `legacy`

  - name: "ip_address_country"
    type: "string"
    description: "The country, based on `ip_address_v4`."

  - name: "ip_address_v4"
    type: "string"
    description: |
      The IP address provided when the billing information was collected:

      - When a customer entered billing info into Recurly.JS or a hosted payment page.
      - When the merchant enters billing info using the API.

  - name: "object"
    type: "string"
    description: ""

  - name: "origin"
    type: "string"
    description: |
      The origin of the transaction. Possible values are:

      - `api`
      - `hpp`
      - `merchant`
      - `recurly_admin`
      - `recurlyjs`
      - `recurring`
      - `transparent`
      - `force_collect`
      - `refunded_externally`
      - `chargeback`

  - name: "original_transaction_id"
    type: "string"
    description: "If the transaction is a refund (`type: refund`), this will be the ID of the original transaction on the invoice being refunded."
    foreign-key-id: "transaction-id"

  - name: "payment_gateway"
    type: "object"
    description: "Details about the payment gateway used to process the transaction."
    subattributes:
      - name: "id"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "payment_method"
    type: "object"
    description: &payment_method_desc "The payment method used in the transaction."
    anchor-id: 1
    subattributes: &payment_method
      - name: "card_type"
        type: "string"
        description: |
          If the payment method is a credit card, this field will contain the type of the credit card. Possible values include:

          - `American Express`
          - `Dankort`
          - `Diners Club`
          - `Discover`
          - `Forbrugsforeningen`
          - `JCB`
          - `Laser`
          - `Maestro`
          - `MasterCard`
          - `Test Card`
          - `Unknown`
          - `Visa`

      - name: "exp_month"
        type: "integer"
        description: "If the payment method is a credit card, this field will contain the expiration month for the credit card."

      - name: "exp_year"
        type: "integer"
        description: "If the payment method is a credit card, this field will contain the expiration year for the credit card."

      - name: "first_six"
        type: "string"
        description: "If the payment method is a credit card, this field will contain the first six digits of the credit card number."

      - name: "last_four"
        type: "string"
        description: "If the payment method is a credit card, this field will contain the last four digits of the credit card number."

      - name: "object"
        type: "string"
        description: ""

  - name: "refunded"
    type: "boolean"
    description: "Indicates if part or all of the transaction was refunded."

  - name: "status"
    type: "string"
    description: &status |
      The current transaction status. Possible values are:

      - `pending`
      - `scheduled`
      - `processing`
      - `success`
      - `void`
      - `declined`
      - `error`
      - `chargeback`

  - name: "status_code"
    type: "string"
    description: ""

  - name: "status_message"
    type: "string"
    description: "For declined transactions (`success: false`), the message displayed to the merchant."

  - name: "subscription_ids"
    type: "array"
    description: "If the transaction refunds one or more subscriptions, this will be a list of the subscription IDs that were refunded."
    subattributes:
      - name: "value"
        type: "string"
        description: "The subscription ID."
        foreign-key-id: "subscription-id"

  - name: "success"
    type: "boolean"
    description: "Indicates if the transaction completed successfully."

  - name: "type"
    type: "string"
    description: |
      The type of the transaction. Possible values include:

      - `authorization` – Verifies billing information and places a hold on money in the customer's account.
      - `capture` – Captures funds held by an authorization and completes a purchase.
      - `purchase` – Combines the authorization and capture in one transaction.
      - `refund` – Returns all or a portion of the money collected in a previous transaction to the customer.
      - `verify` – A $0 or $1 transaction used to verify billing information which is immediately voided.

  - name: "uuid"
    type: "string"
    description: "The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI."

  - name: "voided_at"
    type: "date-time"
    description: "The date and time the transaction was voided."

  - name: "voided_by_invoice"
    type: "object"
    description: "Details about the invoice that voided the transaction."
    subattributes: *mini-invoice
---