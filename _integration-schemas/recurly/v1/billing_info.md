---
tap: "recurly"
version: "1.0"

name: "billing_info"
key: "billing-info"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/billing_info.json"
description: |
  The `{{ table.name }}` table contains info about the billing information for [`accounts`](#accounts).

  **Note**: To replicate this table, you must also have the [`accounts`](#accounts) table set to replicate.

  ### Custom fields

  Stitch's {{ integration.display_name }} integration supports replicating custom fields for {{ table.name }} objects.

replication-method: "Key-based Incremental"
api-method:
    name: "Fetch an account's billing information"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/get_billing_info"

attributes:
  - name: "account_id"
    type: "string"
    primary-key: true
    description: "The ID of the account associated with the billing info."
    foreign-key-id: "account-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the billing info was last updated."

  - name: "address"
    type: "object"
    description: "The address info for the account."
    subattributes: &address
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

  - name: "company"
    type: "string"
    description: "The company name of the account."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the billing info was created."

  - name: "custom_fields"
    type: "array"
    description: "A list of the custom fields associated with the billing info."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the custom field."

      - name: "value"
        type: "string"
        description: "The value of the custom field."

  - name: "exemption_certificate"
    type: "string"
    description: "The tax exemption certificate number for the account. If the merchant has an integration for the Vertex tax provider, this optional value will be sent in any tax calculation requests for the account."

  - name: "first_name"
    type: "string"
    description: "The first name of the account."

  - name: "fraud"
    type: "object"
    description: "Details about the most recent fraud result."
    subattributes:
      - name: "decision"
        type: "string"
        description: |
          The fraud result decision. Possible values are:

          - `approve`
          - `review`
          - `decline`
          - `escalate`

      - name: "risk_rules_triggered"
        type: "object"
        description: ""

      - name: "score"
        type: "number"
        description: "The fraud result score. The value will be a number between `1` and `99`."

  - name: "id"
    type: "string"
    description: "The billing info ID."

  - name: "last_name"
    type: "string"
    description: "The last name of the account."

  - name: "object"
    type: "string"
    description: ""

  - name: "payment_method"
    type: "object"
    description: "Details about the payment method associated with the account's billing info."
    subattributes:
      - name: "account_type"
        type: "string"
        description: "The account type."

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
        type: "number"
        description: "If the payment method is a credit card, this field will contain the expiration month for the credit card."

      - name: "exp_year"
        type: "number"
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

      - name: "routing_number"
        type: "integer"
        description: "If the payment method is a check, this field will contain the routing number associated with the check's bank account."

      - name: "routing_number_bank"
        type: "string"
        description: ""

  - name: "updated_by"
    type: "object"
    description: "Details about the user who last updated the billing info for the account."
    subattributes:
      - name: "country"
        type: "string"
        description: |
          The [two-letter ISO country code](http://www.iso.org/iso/country_names_and_code_elements){:target="new"} of the user who last updated the billing info, based on their `ip`.

      - name: "ip"
        type: "string"
        description: "The IPv4 address of the user who last updated the billing info."

  - name: "valid"
    type: "boolean"
    description: "Indicates if the billing info is valid."

  - name: "vat_number"
    type: "string"
    description: "The VAT number associated with the account."
---