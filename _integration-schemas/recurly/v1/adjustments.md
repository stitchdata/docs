---
tap: "recurly"
version: "1"

name: "adjustments"
key: "adjustment"

doc-link: "https://dev.recurly.com/docs/adjustment-object"
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/adjustments.json"
description: |
  The `{{ table.name }}` table contains info about adjustments, which are credits and charges associated with your customers.

replication-method: "Key-based Incremental"
api-method:
    name: "List an account's line items"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_account_line_items"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The adjustment ID."
    foreign-key-id: "adjustment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the adjustment was last updated."

  - name: "account"
    type: "object"
    description: "Details about the account associated with the adjustment."
    subattributes:
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

  - name: "accounting_code"
    type: "string"
    description: "The accounting code."

  - name: "add_on_code"
    type: "string"
    description: "The code for the add-on the adjustment applies to."

  - name: "add_on_id"
    type: "string"
    description: "The ID of the add-on the adjustment applies to."
    foreign-key-id: "plan-add-on-id"

  - name: "amount"
    type: "number"
    description: "The amount of the adjustment."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the adjustment was created."

  - name: "credit_applied"
    type: "number"
    description: "The amount of credit from this line item that was applied to the invoice."

  - name: "credit_reason_code"
    type: "string"
    description: "The credit reason code associated with the adjustment."

  - name: "currency"
    type: "string"
    description: "The three-letter ISO code of the currency used for the adjustment."

  - name: "description"
    type: "string"
    description: "A description of the adjustment."

  - name: "discount"
    type: "number"
    description: "The discount on the adjustment."

  - name: "end_date"
    type: "date-time"
    description: "The timestamp when the adjustment ended."

  - name: "invoice_id"
    type: "string"
    description: "The ID of the invoice associated with the adjustment."
    foreign-key-id: "invoice-id"

  - name: "invoice_number"
    type: "string"
    description: "The number of the invoice associated with the adjustment."

  - name: "legacy_category"
    type: "string"
    description: |
      The category to describe the role of a line item on a legacy invoice. Possible values include:

      - `charges` - Refers to charges being billed for on this invoice.
      - `credits` - Refers to refund or proration credits. This portion of the invoice can be considered a credit memo.
      - `applied_credits` - Refers to previous credits applied to this invoice. See their original_line_item_id to determine where the credit first originated.
      - `carryforwards` - Can be ignored. They exist to consume any remaining credit balance. A new credit with the same amount will be created and placed back on the account.

  - name: "object"
    type: "string"
    description: ""

  - name: "origin"
    type: "string"
    description: |
      The origin of the adjustment to return. Possible values are:

      - `plan`
      - `plan_trial`
      - `setup_fee`
      - `add_on`
      - `add_on_trial`
      - `one_time`
      - `debit`
      - `credit`
      - `coupon`
      - `carryforward`

  - name: "original_line_item_invoice_id"
    type: "string"
    description: "The invoice where the credit originated. This field will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund."

  - name: "plan_code"
    type: "string"
    description: "The plan code the adjustment applies to."

  - name: "plan_id"
    type: "string"
    description: "The ID of the plan associated with the adjustment."
    foreign-key-id: "plan-id"

  - name: "previous_line_item_id"
    type: "string"
    description: "This field will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund."

  - name: "product_code"
    type: "string"
    description: "For plan-related line items, this will be the plan's code. For add-on related items, this will be the add-on's code."

  - name: "proration_rate"
    type: "number"
    description: "**Applicable only to prorated adjustments.** This represents how much the adjustment was prorated to account for a mid-cycle subscription change."

  - name: "quantity"
    type: "integer"
    description: "The quantity of the adjustment."

  - name: "refund"
    type: "boolean"
    description: "Indicates whether the adjustment is a refund or not."

  - name: "refunded_quantity"
    type: "integer"
    description: "The refunded quantity of the adjustment."

  - name: "shipping_addresses"
    type: "array"
    description: "The shipping address info for the adjustment."
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

  - name: "start_date"
    type: "date-time"
    description: "The timestamp when the adjustment began."

  - name: "state"
    type: "string"
    description: |
      The state of the adjustments to return. Possible values are:

      - `pending`
      - `invoiced`

  - name: "subscription_id"
    type: "string"
    description: "The ID of the subscription associated with the adjustment."

  - name: "subtotal"
    type: "number"
    description: "The subtotal of the adjustment."

  - name: "tax"
    type: "number"
    description: "The tax amount for the adjustment."

  - name: "tax_code"
    type: "string"
    description: |
      **Applicable only to EU VAT and Avalara AvaTax Pro merchants.** The tax code for the adjustment. If using {{ integration.display_name }}'s EU VAT feature, possible values include `unknown`, `physical`, and `digital`.

  - name: "tax_exempt"
    type: "boolean"
    description: "Indicates whether the adjustment is tax exempt or not. If `true`, tax is exempted on the charge."

  - name: "tax_info"
    type: "string"
    description: ""

  - name: "taxable"
    type: "boolean"
    description: "Indicates if the adjustment is taxable."

  - name: "type"
    type: "string"
    description: |
      The type of adjustment to return. Possible values are:

      - `charge`
      - `credit`

  - name: "unit_amount"
    type: "number"
    description: "The unit amount for the adjustment, in cents. For `type: charge`, this will be a positive amount. For `type: credit`, this will be a negative amount."

  - name: "uuid"
    type: "string"
    description: "The unique identifier of the adjustment."
---