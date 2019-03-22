---
tap: "invoiced"
version: "1.0"

name: "customers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the customers in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all customers"
    doc-link: "https://invoiced.com/docs/api/#list-all-customers"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the customer was last updated."

  - name: "address1"
    type: "string"
    description: "The first line of the customer's address."

  - name: "address2"
    type: "string"
    description: "The second line of the customer's address."

  - name: "attention_to"
    type: "string"
    description: "Used for `ATTN: address` line if `type: company`."

  - name: "autopay"
    type: "boolean"
    description: "If `true`, AutoPay is enabled for the customer."

  - name: "chase"
    type: "boolean"
    description: ""

  - name: "chasing_cadence"
    type: "integer"
    description: ""

  - name: "city"
    type: "string"
    description: "The city of the customer's address."

  - name: "country"
    type: "string"
    description: |
      The two-letter [ISO code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2){:target="new"} of the customer's country.

  - name: "created_at"
    type: "date-time"
    description: "The time the customer was created."

  - name: "credit_hold"
    type: "boolean"
    description: ""

  - name: "credit_limit"
    type: "number"
    description: "The credit limit for the customer."

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "language"
    type: "string"
    description: |
      The two-letter [ISO code](https://en.wikipedia.org/wiki/ISO_639-1){:target="new"} of the customer's language.

  - name: "metadata"
    type: "object"
    description: "Additional information about the customer."
    subattributes: 

  - name: "name"
    type: "string"
    description: "The name of the customer."

  - name: "next_chase_step"
    type: "integer"
    description: ""

  - name: "notes"
    type: "string"
    description: "Additional notes about the customer."

  - name: "number"
    type: "string"
    description: "A unique ID used to tie the customer to external systems."

  - name: "parent_customer"
    type: "integer"
    description: ""

  - name: "payment_source"
    type: "object"
    description: "The customer's payment source, if attached."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The payment source's ID."

      - name: "object"
        type: "string"
        description: |
          The object type of the payment source. Possible values are:

          - `card`
          - `bank_account`

      - name: "brand"
        type: "string"
        description: "**Applicable to `object: card` only.** The card brand."

      - name: "last4"
        type: "string"
        description: "The last four digits of the card or bank account."

      - name: "exp_month"
        type: "integer"
        description: "**Applicable to `object: card` only.** The expiry month."

      - name: "exp_year"
        type: "integer"
        description: "**Applicable to `object: card` only.** The expiry year."

      - name: "funding"
        type: "string"
        description: |
          **Applicable to `object: card` only.** The funding instrument of the card. Possible values are:

          - `credit`
          - `debit`
          - `prepaid`
          - `unknown`

      - name: "bank_name"
        type: "string"
        description: "**Applicable to `object: bank_account` only.** The name of the bank."

      - name: "routing_number"
        type: "string"
        description: "**Applicable to `object: bank_account` only.** The routing number."

      - name: "verified"
        type: "boolean"
        description: "**Applicable to `object: bank_account` only.** Indicates whether the bank account has been verified with instant verification or microdeposits."

      - name: "currency"
        type: "string"
        description: |
          **Applicable to `object: bank_account` only.** The [three letter ISO code](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} used by the bank account.

  - name: "payment_terms"
    type: "string"
    description: "The payment terms for the customer when AutoPay is not enabled."

  - name: "phone"
    type: "string"
    description: "The customer's phone number."

  - name: "postal_code"
    type: "string"
    description: "The customer's postal code."

  - name: "sign_up_page"
    type: "integer"
    description: "The ID of the sign up page used by the customer."

  - name: "state"
    type: "string"
    description: "The customer's state."

  - name: "tax_id"
    type: "string"
    description: "The customer's tax ID."

  - name: "taxable"
    type: "boolean"
    description: "If `true`, the customer is not tax exempt."

  - name: "taxes"
    type: "array"
    description: "The taxes applicable to the customer."
    subattributes: &taxes
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The tax ID."
        foreign-key-id: "tax-id"

      - name: "object"
        type: "string"
        description: "This will be `tax`."

      - name: "amount"
        type: "number"
        description: "The amount of tax."

      - name: "tax_rate"
        type: "number"
        description: "The tax rate the tax was calculated from."

  - name: "type"
    type: "string"
    description: |
      The customer's type. Possible values are:

      - `company`
      - `person`
---