---
tap: "recurly"
version: "1.0"

name: "subscriptions"
key: "subscription"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/subscriptions.json"
description: |
  The `{{ table.name }}` table contains info about the subscriptions in your {{ integration.display_name }} account. Subscriptions are created when your customers subscribe to one of your plans. The customer's subscription tells {{ integration.display_name }} when and how much to bill the customer.

  ### Custom fields

  Stitch's {{ integration.display_name }} integration supports replicating custom fields for subscription objects.

replication-method: "Key-based Incremental"
api-method:
    name: "List a site's subscriptions"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_subscriptions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The subscription ID."
    foreign-key-id: "subscription-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the subscription was last updated."

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

  - name: "activated_at"
    type: "date-time"
    description: "The date and time the subscription was activated."

  - name: "add_ons"
    type: "array"
    description: "Details about the add-ons associated with the subscription."
    subattributes:
      - name: "add_on"
        type: "object"
        description: "Details about the add-on."
        subattributes: &mini-add-on
          - name: "accounting_code"
            type: "string"
            description: "The accounting code for invoice line items for this add-on."

          - name: "code"
            type: "string"
            description: "The unique identifier for the add-on within its plan."

          - name: "id"
            type: "string"
            description: "The add-on ID."
            foreign-key-id: "plan-add-on-id"

          - name: "name"
            type: "string"
            description: "The name of the add-on."

          - name: "object"
            type: "string"
            description: ""

      - name: "created_at"
        type: "date-time"
        description: "The date and time the add-on was added to the subscription."

      - name: "expired_at"
        type: "date-time"
        description: "The date and time the add-on will expire."

      - name: "id"
        type: "string"
        description: "The subscription add-on ID."

      - name: "object"
        type: "string"
        description: ""

      - name: "quantity"
        type: "number"
        description: "The quantity of the add-on."

      - name: "subscription_id"
        type: "string"
        description: "The ID of the subscription associated with the add-on."
        foreign-key-id: "subscription-id"

      - name: "unit_amount"
        type: "number"
        description: "The unit amount of the add-on in the subscription's `currency`."

      - name: "updated_at"
        type: "date-time"
        description: "The date and time the subscription add-on was last updated."

  - name: "add_ons_total"
    type: "number"
    description: "The total price of the add-ons associated with the subscription."

  - name: "auto_renew"
    type: "boolean"
    description: "Indicates whether the subscription renews at the end of its term."

  - name: "bank_account_authorized_at"
    type: "date-time"
    description: ""

  - name: "canceled_at"
    type: "date-time"
    description: ""

  - name: "collection_method"
    type: "string"
    description: |
      The collection method for the subscription. Possible values are:

      - `automatic`
      - `manual`

  - name: "coupon_redemptions"
    type: "array"
    description: "Details about the coupon redemptions associated with the subscription."
    subattributes:
      - name: "coupon"
        type: "object"
        description: ""
        subattributes:
          - name: "code"
            type: "string"
            description: "The code the customer enters to redeem the coupon."

          - name: "coupon_type"
            type: "string"
            description: |
              The type of the coupon. Possible values are:

              - `single_code`
              - `bulk`

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

          - name: "expired_at"
            type: "date-time"
            description: "The date and time the coupon was expired early or reached its `max_redemptions`."

          - name: "id"
            type: "string"
            description: "The coupon ID."
            foreign-key-id: "coupon-id"

          - name: "name"
            type: "string"
            description: "The internal name for the coupon."

          - name: "object"
            type: "string"
            description: ""

          - name: "state"
            type: "string"
            description: |
              The coupon's redemption status. Possible values are:

              - `redeemable`
              - `maxed_out`
              - `expired`

      - name: "created_at"
        type: "date-time"
        description: "The date and time the coupon redemption was created."

      - name: "discounted"
        type: "string"
        description: "The amount that was discounted upon the application of the coupon, formatted with the currency."

      - name: "id"
        type: "string"
        description: "The coupon redemption ID."
        foreign-key-id: "coupon-redemption-id"

      - name: "object"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: |
          The state of the redemption. Possible values are:

          - `active`
          - `inactive`

  - name: "created_at"
    type: "date-time"
    description: "The date and time the subscription was created."

  - name: "currency"
    type: "string"
    description: "The three-letter ISO 4217 currency code associated with the subscription."

  - name: "current_period_ends_at"
    type: "date-time"
    description: "The date the current billing period for the subscription ends."

  - name: "current_period_started_at"
    type: "date-time"
    description: "The date the current billing period for the subscription started."

  - name: "current_term_ends_at"
    type: "date-time"
    description: "The end date when the first billing period ends. This is calculated by a plan's interval and `total_billing_cycles` in a term. Subscription changes with a `timeframe: renewal` will be applied on this date."

  - name: "current_term_started_at"
    type: "date-time"
    description: "The start date of the term when the first billing period starts. The subscription term is the length of time that a customer will be committed to a subscription. A term can span multiple billing periods."

  - name: "custom_fields"
    type: "array"
    description: "A list of custom fields associated with the subscription."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the custom field."

      - name: "value"
        type: "string"
        description: "The value of the custom field."

  - name: "customer_notes"
    type: "string"
    description: "Customer notes associated with the subscription."

  - name: "expiration_reason"
    type: "string"
    description: "The expiration reason associated with the subscription."

  - name: "expires_at"
    type: "date-time"
    description: "The date and time the subscription expired."

  - name: "net_terms"
    type: "number"
    description: "An integer representing the number of days after an invoice's creation that the invoice will become past due. If an invoice's net terms are set to `0`, it is due on receipt and will become past due 24 hours after it’s created. If an invoice is due net `30`, it will become past due at 31 days exactly."

  - name: "object"
    type: "string"
    description: ""

  - name: "paused_at"
    type: "date-time"
    description: "The date and time the subscription was paused. This value will be `null` unless the subscription is paused or will pause at the end of the current billing period."

  - name: "pending_change"
    type: "object"
    description: "Details about any pending changes associated with the subscription."
    subattributes:
      - name: "activate_at"
        type: "date-time"
        description: "The date and time the subscription change was activated."

      - name: "activated"
        type: "boolean"
        description: "Indicates if the subscription is active."

      - name: "add_ons"
        type: "array"
        description: "Details about the add-ons that will be used when the subscription renews."
        subattributes:
          - name: "add_on"
            type: "object"
            anchor-id: 2
            description: "Details about the add-on associated with the subscription change."
            subattributes: *mini-add-on

          - name: "created_at"
            type: "date-time"
            description: "The date and time the add-on associated with the subscription change was created."

          - name: "expired_at"
            type: "date-time"
            description: "The date and time the add-on associated with the subscription change will expire."

          - name: "id"
            type: "string"
            description: "The subscription add-on ID."

          - name: "object"
            type: "string"
            description: ""

          - name: "quantity"
            type: "number"
            description: "The subscription add-on quantity."

          - name: "subscription_id"
            type: "string"
            description: "The subscription ID."
            foreign-key-id: "subscription-id"

          - name: "unit_amount"
            type: "number"
            description: ""

          - name: "updated_at"
            type: "date-time"
            description: "The date and time the add-on associated with the subscription change was last updated."

      - name: "created_at"
        type: "date-time"
        description: "The date and time the subscription change was created."

      - name: "deleted_at"
        type: "date-time"
        description: "The date and time the subscription change was deleted."

      - name: "id"
        type: "string"
        description: "The subscription change ID."

      - name: "object"
        type: "string"
        description: ""

      - name: "plan"
        type: "object"
        description: "Details about the plan associated with the pending change."
        subattributes: &mini-plan
          - name: "code"
            type: "string"
            description: "The unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports."

          - name: "id"
            type: "string"
            description: "The plan ID."
            foreign-key-id: "plan-id"

          - name: "name"
            type: "string"
            description: "The name of the plan."

          - name: "object"
            type: "string"
            description: ""

      - name: "quantity"
        type: "number"
        description: "The subscription quantity."

      - name: "subscription_id"
        type: "string"
        description: "The ID of the subscription that is going to be changed."
        foreign-key-id: "subscription-id"

      - name: "unit_amount"
        type: "number"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: "The date and time the subscription change was last updated."

  - name: "plan"
    type: "object"
    description: "Details about the plan associated with the subscription."
    subattributes: *mini-plan

  - name: "po_number"
    type: "string"
    description: "For manual invoicing, this identifies the PO number associated with the subscription."

  - name: "quantity"
    type: "number"
    description: ""

  - name: "remaining_billing_cycles"
    type: "number"
    description: "The remaining billing cycles in the current term."

  - name: "remaining_pause_cycles"
    type: "number"
    description: "This value will be `null` unless the subscription is paused or will pause at the end of the current billing period."

  - name: "renewal_billing_cycles"
    type: "number"
    description: "If `auto_renew: true`, when a term completes, `total_billing_cycles` takes this value as the length of subsequent terms."

  - name: "shipping_addresses"
    type: "array"
    description: "The shipping address info for the subscription."
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
      The state of the subscription. Possible values are:

      - `active`
      - `canceled`
      - `expired`
      - `failed`
      - `future`
      - `paused`

  - name: "subtotal"
    type: "number"
    description: "The subscription subtotal, before taxes."

  - name: "terms_and_conditions"
    type: "string"
    description: "The terms and conditions for the subscription."

  - name: "total_billing_cycles"
    type: "number"
    description: "The number of cycles/billing periods in a term. When `remaining_billing_cycles: 0`, if `auto_renew: true` the subscription will renew and a new term will begin, otherwise the subscription will expire."

  - name: "trial_ends_at"
    type: "date-time"
    description: "The date the trial for the subscription ended."

  - name: "trial_started_at"
    type: "date-time"
    description: "The date the trial for the subscription started."

  - name: "unit_amount"
    type: "number"
    description: ""

  - name: "uuid"
    type: "string"
    description: "The UUID is useful for matching data with the CSV exports and building URLs into {{ integration.display_name }}'s UI."
---