---
tap: "recurly"
version: "1"

name: "accounts"
key: "account"

doc-link: "https://dev.recurly.com/docs/account-object"
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about the customer accounts in your {{ integration.display_name }} account. Account objects store the history of the customer, billing info, etc.

  ### Custom fields

  Stitch's {{ integration.display_name }} integration supports replicating custom fields for {{ table.name }} objects.

replication-method: "Key-based Incremental"

api-method:
    name: "List a site's accounts"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_accounts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the account or its billing info was last updated."

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

  - name: "bill_to"
    type: "string"
    description: |
      Indicates whether charges on the account are billed using the parent's billing info or the account itself. Possible values are:

      - `self` - The account itself.
      - `parent` - All invoices resulting in charges and credits originating from a child will be created on the parent account.

  - name: "billing_info"
    type: "object"
    description: "Details about the account's billing info."
    subattributes:
      - name: "account_id"
        type: "string"
        description: "The ID of the account associated with the billing info."

      - name: "address"
        type: "object"
        description: "The address associated with the billing info."
        subattributes: *address

      - name: "company"
        type: "string"
        description: "The billing company."

      - name: "created_at"
        type: "date-time"
        description: "The timestamp when the billing info was created."

      - name: "first_name"
        type: "string"
        description: "The first name."

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
            type: "integer"
            description: "The fraud result score. The value will be a number between `1` and `99`."

      - name: "id"
        type: "string"
        description: "the billing info ID."

      - name: "last_name"
        type: "string"
        description: "The last name."

      - name: "object"
        type: "string"
        description: ""

      - name: "payment_method"
        type: "object"
        description: "Details about the payment method associated with the account's billing info."
        subattributes:
          - name: "card_type"
            type: "string"
            description: |
              The card type. Possible values include:

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
            description: "The expiration month for the card."

          - name: "exp_year"
            type: "integer"
            description: "The expiration year for the card."

          - name: "first_six"
            type: "string"
            description: "The first six digits of the credit card's number."

          - name: "last_four"
            type: "string"
            description: "The last four digits of the credit card's number."

          - name: "object"
            type: "string"
            description: ""

      - name: "updated_at"
        type: "date-time"
        description: "The timestamp when the billing info was last updated."

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
        description: "The customer's VAT number."

  - name: "cc_emails"
    type: "string"
    description: "Additional email addresses that should receive account correspondence. These emails will receive all emails that the `email` field also receives."

  - name: "code"
    type: "string"
    description: "The unique identifier of the account."

  - name: "company"
    type: "string"
    description: "The company name of the account."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the account was created."

  - name: "custom_fields"
    type: "array"
    description: "A list of custom fields associated with the account."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the custom field."

      - name: "value"
        type: "string"
        description: "The value of the custom field."

  - name: "deleted_at"
    type: "date-time"
    description: "The date and time the account was deleted."

  - name: "email"
    type: "string"
    description: "The email address for the account."

  - name: "exemption_certificate"
    type: "string"
    description: "The tax exemption certificate number for the account. If the merchant has an integration for the Vertex tax provider, this optional value will be sent in any tax calculation requests for the account."

  - name: "first_name"
    type: "string"
    description: "The first name of the account."

  - name: "hosted_login_token"
    type: "string"
    description: "The unique token for automatically logging the account into the hosted management pages."

  - name: "last_name"
    type: "string"
    description: "The last name of the account."

  - name: "object"
    type: "string"
    description: "This will be `account`."

  - name: "parent_account_id"
    type: "string"
    description: "If the account is a child account, the ID of the parent account."
    foreign-key-id: "account-id"

  - name: "preferred_locale"
    type: "string"
    description: "Used to determine the language and locale of emails sent on behalf of the merchant to the customer. The list of locales is restricted to those the merchant has enabled on the site."

  - name: "shipping_addresses"
    type: "array"
    description: "The shipping address info for the account."
    subattributes:
      - name: "account_id"
        type: "string"
        description: "The ID of the account associated with the shipping address info."
        foreign-key-id: "account-id"

      - name: "city"
        type: "string"
        description: "The shipping city."

      - name: "company"
        type: "string"
        description: "The shipping company."

      - name: "country"
        type: "string"
        description: "The two-letter ISO country code."

      - name: "created_at"
        type: "date-time"
        description: "The timestamp when the shipping address was created."

      - name: "email"
        type: "string"
        description: "The email associated with the shipping address."

      - name: "first_name"
        type: "string"
        description: "The first name."

      - name: "id"
        type: "string"
        description: "The shipping address ID."

      - name: "last_name"
        type: "string"
        description: "The last name."

      - name: "nickname"
        type: "string"
        description: "The nickname."

      - name: "phone"
        type: "string"
        description: "The phone number."

      - name: "postal_code"
        type: "string"
        description: "The postal code."

      - name: "region"
        type: "string"
        description: "The state or province."

      - name: "street1"
        type: "string"
        description: "The first street line of the address."

      - name: "street2"
        type: "string"
        description: "The second street line of the address."

      - name: "updated_at"
        type: "date-time"
        description: "The timestamp when the shipping address was last updated."

      - name: "vat_number"
        type: "string"
        description: "The VAT number associated with the shipping address."

  - name: "state"
    type: "string"
    description: |
      The state of the account. Possible values are `active` or `closed`.

  - name: "tax_exempt"
    type: "boolean"
    description: |
      The tax status of the account. A value of `true` exempts tax on the account, and `false` applies tax.

  - name: "username"
    type: "string"
    description: "The username of the account."

  - name: "vat_number"
    type: "string"
    description: "The VAT number of the account."
---