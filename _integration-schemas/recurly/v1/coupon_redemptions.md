"number"---
tap: "recurly"
version: "1.0"

name: "coupon_redemptions"
key: "coupon-redemption"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/coupon_redemptions.json"
description: |
  The `{{ table.name }}` table contains info about the coupon redemptions associated with an [`account`](#accounts).

  **Note**: To replicate this table, you must also have the [`accounts`](#accounts) table set to replicate.

replication-method: "Key-based Incremental"
api-method:
    name: "Show the coupon redemptions for an account"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_account_coupon_redemptions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The coupon redemption ID."
    foreign-key-id: "coupon-redemption-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the coupon redemption was created."

  - name: "account"
    type: "object"
    description: "Details about the account associated with the coupon redemption."
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

  - name: "account_id"
    type: "string"
    description: "The ID of the account associated with the coupon redemption."
    foreign-key-id: "account-id"

  - name: "coupon"
    type: "object"
    description: "Details about the coupon."
    subattributes:
      - name: "applies_to_all_plans"
        type: "boolean"
        description: "Indicates if the coupon is valid for all plans."

      - name: "applies_to_non_plan_charges"
        type: "boolean"
        description: "Indicates if the coupon is valid for one-time, non-plan charges."

      - name: "code"
        type: "string"
        description: "The code the customer enters to redeem the coupon."

      - name: "coupon_type"
        type: "string"
        description: |
          The type of the coupon. Possible values are:

          - `single_code`
          - `bulk`

      - name: "created_at"
        type: "date-time"
        description: "The timestamp when the coupon was created."

      - name: "discount"
        type: "object"
        description: "Details of the discount a coupon applies."
        subattributes:
          - name: "currencies"
            type: "array"
            description: "**Applicable only when `type: fixed`.** The currencies associated with the coupon discount."
            subattributes:
              - name: "amount"
                type: "number"
                description: "The value of the fixed discount that the coupon applies."

              - name: "currency"
                type: "string"
                description: "The three-letter ISO 4217 currency code."

          - name: "percent"
            type: "number"
            description: "**Applicable only when `type: percent`.** The percent of the total that is used to calculate the discount."

          - name: "trial"
            type: "object"
            description: "**Applicable only when `type: free_trial`**. Details about the discount for free trials."
            subattributes:
              - name: "length"
                type: "number"
                description: "The trial length measured in units, specified by `unit`."

              - name: "unit"
                type: "string"
                description: |
                  The temporal unit of the free trial. Possible values are:

                  - `day`
                  - `week`
                  - `month`

          - name: "type"
            type: "string"
            description: |
              The type of discount the coupon applies. Possible values are:

              - `percent`
              - `fixed`
              - `free_trial`

      - name: "duration"
        type: "string"
        description: |
          The duration that the coupon will be applied to invoices for. Possible values are:

          - `forever`
          - `single_use` - The coupon can be applied only to the first invoice.
          - `temporal` - The coupon can be applied to invoices for the duration determined by the `temporal_unit` and `temporal_amount` attributes.

      - name: "expired_at"
        type: "date-time"
        description: "The date and time the coupon was expired early or reached its `max_redemptions`."

      - name: "free_trial_amount"
        type: "number"
        description: "The duration of time the `free_trial_unit` is for."

      - name: "free_trial_unit"
        type: "string"
        description: |
          The description of the unit of time the coupon is for. Used with the `free_trial_amount` attribute to determine the duration of time the coupon is for. Possible values are:

          - `day`
          - `week`
          - `month`

      - name: "hosted_page_description"
        type: "string"
        description: "This description will show up when a customer redeems a coupon on your Hosted Payment Pages, or if you choose to show the description on your own checkout page."

      - name: "id"
        type: "string"
        description: "The coupon ID."
        foreign-key-id: "coupon-id"

      - name: "invoice_description"
        type: "string"
        description: "The description of the coupon as it will appear on invoices."

      - name: "max_redemptions"
        type: "number"
        description: "The maximum number of redemptions for the coupon. The coupon will expire when the maximum redemption is hit."

      - name: "max_redemptions_per_account"
        type: "number"
        description: "The number of times a specific account can redeem the coupon."

      - name: "name"
        type: "string"
        description: "The internal name for the coupon."

      - name: "object"
        type: "string"
        description: ""

      - name: "plans"
        type: "string"
        description: ""

      - name: "plans_names"
        type: "array"
        description: "A list of plan names that the coupon may be applied to."
        subattributes:
          - name: "value"
            type: "anything"
            description: "The plan name."

      - name: "redeem_by"
        type: "date-time"
        description: "the date and time the coupon will expire and can no longer be redeemed."

      - name: "redemption_resource"
        type: "string"
        description: |
          Indicates if the coupon is for all eligible charges on the account or only a specific subscription. Possible values are:

          - `account`
          - `subscription`

      - name: "state"
        type: "string"
        description: |
          The coupon's redemption status. Possible values are:

          - `redeemable`
          - `maxed_out`
          - `expired`

      - name: "temporal_amount"
        type: "number"
        description: "**Applicable when `duration: temporal_amount`**. The duration that the coupon will be applied to invoices for, calculated as an integer multiplied by `temporal_unit`."

      - name: "temporal_unit"
        type: "string"
        description: |
          **Applicable when `duration: temporal_amount`**. The unit of time used to calculate the duration that the coupon will be applied to invoices for. Possible values are:

          - `day`
          - `week`
          - `month`
          - `year`

      - name: "unique_coupon_codes_count"
        type: "number"
        description: "The total number of unique redemptions for the coupon."

      - name: "updated_at"
        type: "date-time"
        description: "The timestamp when the coupon was last updated."

  - name: "currency"
    type: "string"
    description: "The three-letter ISO 4217 currency code of the currency used in the coupon redemption."

  - name: "discounted"
    type: "string"
    description: "The amount that was discounted upon the application of the coupon, formatted with the currency."

  - name: "object"
    type: "string"
    description: "This will be `coupon`."

  - name: "removed_at"
    type: "date-time"
    description: "The date and time the redemption was removed from the account."

  - name: "state"
    type: "string"
    description: |
      The state of the redemption. Possible values are:

      - `active`
      - `inactive`

  - name: "unique_code_template"
    type: "string"
    description: "On a bulk coupon, the template from which unique coupon codes are generated."

  - name: "updated_at"
    type: "date-time"
    description: "The date and time when the redemption was last updated."
---