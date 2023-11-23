---
tap: "recurly"
version: "1"

name: "plans"
key: "plan"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/plans.json"
description: |
  The `{{ table.name }}` table contains info about the plans in your {{ integration.display_name }} account. A plan tells {{ integration.display_name }} how much to charge customers.

replication-method: "Key-based Incremental"
api-method:
    name: "List a site's plans"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_plans"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The plan ID."
    foreign-key-id: "plan-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the plan was last updated."

  - name: "accounting_code"
    type: "string"
    description: "Accounting code for invoice line items for the plan."

  - name: "auto_renew"
    type: "boolean"
    description: "Subscriptions will automatically inherit this value once they are active. If `auto_renew: true`, then a subscription will automatically renew its term at renewal. If `auto_renew: false`, then a subscription will expire at the end of its term."

  - name: "code"
    type: "string"
    description: "The unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the plan was created."

  - name: "currencies"
    type: "array"
    description: "Details about the currencies associated with the plan."
    subattributes:
      - name: "currency"
        type: "string"
        description: "The three-letter ISO 4217 currency code."

      - name: "setup_fee"
        type: "number"
        description: "Amount of one-time setup fee automatically charged at the beginning of a subscription billing cycle. For subscription plans with a trial, the setup fee will be charged at the time of signup. Setup fees do not increase with the quantity of a subscription plan."

      - name: "unit_amount"
        type: "number"
        description: ""

  - name: "deleted_at"
    type: "date-time"
    description: "The date and time the plan was deleted."

  - name: "description"
    type: "string"
    description: "The description of the plan."

  - name: "hosted_pages"
    type: "object"
    description: "The hosted pages associated with the plan."
    subattributes:
      - name: "bypass_confirmation"
        type: "boolean"
        description: "If true, the customer will be sent directly to the `success_url` after a successful signup, bypassing {{ integration.display_name }}'s hosted confirmation page."

      - name: "cancel_url"
        type: "string"
        description: "The URL to redirect to on canceled signup on the hosted payment pages."

      - name: "display_quantity"
        type: "boolean"
        description: "Indicates if the quantity field is displayed on hosted pages for the plan."

      - name: "success_url"
        type: "string"
        description: "The URL to redirect to after signup on the hosted payment pages."

  - name: "interval_length"
    type: "integer"
    description: |
      The length of the plan's billing interval in `interval_unit`. For example: A value of `30` with an `interval_unit` of `days` means the plan's billing interval is `30 days`.

  - name: "interval_unit"
    type: "string"
    description-type: "billing interval"
    description: &unit |
      The unit for the plan's {{ attribute.description-type }}. Possible values are:

      - `days`
      - `months`

  - name: "name"
    type: "string"
    description: "This name describes the plan and will appear on the Hosted Payment Page and the subscriber's invoice."

  - name: "object"
    type: "string"
    description: ""

  - name: "setup_fee_accounting_code"
    type: "string"
    description: "Accounting code for invoice line items for the plan's setup fee."

  - name: "state"
    type: "string"
    description: |
      The current state of the plan. Possible values are:

      - `active`
      - `inactive`

  - name: "tax_code"
    type: "string"
    description: |
      Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature:

      - `P0000000` - Physical
      - `D0000000` - Digital
      - Empty string - Unknown

  - name: "tax_exempt"
    type: "boolean"
    description: "Indicates whether the plan is tax exempt."

  - name: "total_billing_cycles"
    type: "integer"
    description: "Automatically terminate subscriptions after a defined number of billing cycles. Number of billing cycles before the plan automatically stops renewing, defaults to null for continuous, automatic renewal."

  - name: "trial_length"
    type: "integer"
    description: "The length of the plan's trial period in `trial_unit`. A value of `0` means `no trial`."

  - name: "trial_unit"
    type: "string"
    description-type: "trial period"
    description: *unit
---