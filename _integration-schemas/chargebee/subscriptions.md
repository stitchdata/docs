---
tap: "chargebee"
version: "1"
key: "subscription"

name: "subscriptions"
doc-link: "https://apidocs.chargebee.com/docs/api/subscriptions"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/subscriptions.json"
description: |
  The `{{ table.name }}` table contains info about the subscriptions your customers have subscribed to. A subscription is a recurring item that customers are billed for, such as a plan or addon. It may also contain discount items.

  **Note**: {{ integration.display_name }} [does not update the `updated_at`](https://apidocs.chargebee.com/docs/api/subscriptions#subscription_updated_at){:target="new"} value when the following attributes on a subscription are modified:

  - `due_invoices_count`
  - `due_since`
  - `total_dues`

  Because of this functionality and Stitch's use of this value as a [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}), updates made to subscriptions where only these attributes are modified may not be detected. You should ensure that another attribute on the subscription is also modified to ensure that the `updated_at` value is updated, which will allow Stitch to detect and replicate the record.

replication-method: "Key-based Incremental"

api-method:
    name: "List subscriptions"
    doc-link: "https://apidocs.chargebee.com/docs/api/subscriptions#list_subscriptions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The subscription ID."
    foreign-key-id: "subscription-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      The time when the subscription was last updated.

      **Note**: {{ integration.display_name }} [does not update this value](https://apidocs.chargebee.com/docs/api/subscriptions#subscription_updated_at){:target="new"} when the following attributes are modified:

      - `due_invoices_count`
      - `due_since`
      - `total_dues`

      Because of this functionality and Stitch's use of this value as a [Replication Key]({{ link.replication.rep-keys | prepend: site.baseurl }}), updates made to subscriptions where only these attributes are modified may not be detected. You should ensure that another attribute on the subscription is also modified to ensure that the `updated_at` value is updated, which will allow Stitch to detect and replicate the record.

  - name: "activated_at"
    type: "date-time"
    description: "The time at which the subscription moved from `in_trial` to `active`."

  - name: "addons"
    type: "array"
    description: "Details about the addon(s) associated with the subscription."
    subattributes:
      - name: "id"
        type: "string"
        description: "The addon ID."
        foreign-key-id: "addon-id"

      - name: "amount"
        type: "integer"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "quantity"
        type: "integer"
        description: "**Applicable only for the quantity based addons.** The quantity."

      - name: "remaining_billing_cycles"
        type: "integer"
        description: "The number of billing cycles this addon will be attached to subscription."

      - name: "trial_end"
        type: "date-time"
        description: "The time at which the trial ends for the addon."

      - name: "unit_price"
        type: "integer"
        description: &addon-unit-price |
          The amount that will override the addon's default price. The plan's billing frequency will not be considered for overriding. E.g. If the plan's billing frequency is every 3 months, and if the price override amount is $10, $10 will be used, and not $30 (i.e $10*3).

  - name: "affiliate_token"
    type: "string"
    description: "A unique tracking token for the subscription."

  - name: "auto_collection"
    type: "string"
    description: |
      Defines whether payments need to be collected automatically for this subscription. Possible values are:

      - `on`
      - `off`

  - name: "base_currency_code"
    type: "string"
    description: "The base currency code for the subscription in ISO 4217 format."

  - name: "billing_period"
    type: "integer"
    description: |
      Defines the billing frequency for the subscription. Used with `billing_period_unit`, this determines how the customer is billed for the subscription.

      For example: If `billing_period_unit: week` and `billing_period: 3`, the customer would be billed every `3 weeks`.

  - name: "billing_period_unit"
    type: "string"
    description: |
      Defines the billing period for the subscription. Used with `billing_period`, this determines how the customer is billed for the subscription.

      For example: If `billing_period_unit: week` and `billing_period: 3`, the customer would be billed every `3 weeks`.

      Possible values are:

      - `day`
      - `week`
      - `month`
      - `year`

  - name: "cancel_reason"
    type: "string"
    description: |
      The possible reason the subscription might be cancelled. Possible values are:

      - `not_paid`
      - `no_card`
      - `fraud_review_failed`
      - `non_compliant_eu_customer`
      - `tax_calculation_failed`
      - `currency_incompatible_with_gateway`
      - `non_compliant_customer`

  - name: "cancelled_at"
    type: "date-time"
    description: "The time at which subscription was cancelled or is set to be cancelled."

  - name: "charged_event_based_addons"
    type: "array"
    description: "A list of event-based addons that have already been charged."
    subattributes:
      - name: "id"
        type: "string"
        description: "The addon ID."
        foreign-key-id: "addon-id"

      - name: "last_charged_at"
        type: "date-time"
        description: "The time when the addon was last charged for the subscription."

      - name: "object"
        type: "string"
        description: ""

  - name: "coupon"
    type: "string"
    description: ""

  - name: "coupons"
    type: "array"
    description: "Details about the coupon(s) associated with the subscription."
    subattributes:
      - name: "applied_count"
        type: "integer"
        description: "The number of times the coupon has been applied for the subscription."

      - name: "apply_till"
        type: "date-time"
        description: "**Applicable for `limited month` coupons.** The date till the coupon is to be applied."

      - name: "coupon_code"
        type: "string"
        description: "The coupon code used to redeem the coupon."

      - name: "coupon_id"
        type: "string"
        description: "The coupon ID."
        foreign-key-id: "coupon-id"

      - name: "object"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: "The time the subscription was created."

  - name: "created_from_ip"
    type: "string"
    description: ""

  - name: "currency_code"
    type: "string"
    description: "The currency code for the subscription in ISO 4217 format."

  - name: "current_term_end"
    type: "date-time"
    description: "The end of the current billing term for the subscription, after which the subscription will be immediately renewed."

  - name: "current_term_start"
    type: "date-time"
    description: "The start of the current billing term for the subscription."

  - name: "custom_fields"
    type: "string"
    description: ""  

  - name: "customer_id"
    type: "string"
    description: "The ID of the customer associated with the subscription."
    foreign-key-id: "customer-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the subscription has been deleted or not."

  - name: "due_invoices_count"
    type: "integer"
    description: "The total number of invoices that are due for payment."

  - name: "due_since"
    type: "date-time"
    description: ""

  - name: "event_based_addons"
    type: "array"
    description: "A list of non-recurring addons associated with the subscription that will be charged on the occurrence of a specified event."
    subattributes:
      - name: "charge_once"
        type: "boolean"
        description: "If enabled, the addon will be charged only at the first occurrence of the event."

      - name: "id"
        type: "string"
        description: "The addon ID."
        foreign-key-id: "addon-id"

      - name: "object"
        type: "string"
        description: ""

      - name: "on_event"
        type: "string"
        description: "The event on which the addon will be charged."

      - name: "quantity"
        type: "integer"
        description: "**Applicable only for the quantity based addons**. The addon quantity."

      - name: "unit_price"
        type: "integer"
        description: *addon-unit-price

  - name: "exchange_rate"
    type: "number"
    description: "The exchange rate used for base currency conversion."

  - name: "gift_id"
    type: "string"
    description: "The ID of the gift associated with the subscription."
    foreign-key-id: "gift-id"

  - name: "has_scheduled_changes"
    type: "boolean"
    description: "If true, there are subscription changes scheduled on next renewal."

  - name: "invoice_notes"
    type: "string"
    description: "The invoice notes for the subscription."

  - name: "meta_data"
    type: "string"
    description: ""

  - name: "mrr"
    type: "integer"
    description: "The monthly recurring revenue for the subscription, in cents."

  - name: "next_billing_at"
    type: "date-time"
    description: "The date on which the next billing occurs."

  - name: "object"
    type: "string"
    description: ""

  - name: "pause_date"
    type: "date-time"
    description: ""

  - name: "payment_source_id"
    type: "string"
    description: "The ID of the payment source associated with the subscription."
    foreign-key-id: "payment-source-id"

  - name: "plan_amount"
    type: "integer"
    description: ""

  - name: "plan_free_quantity"
    type: "integer"
    description: "The units of the item that will be free with the plan associated with the subscription."

  - name: "plan_id"
    type: "string"
    description: "The ID of the plan associated with the subscription."
    foreign-key-id: "plan-id"

  - name: "plan_quantity"
    type: "integer"
    description: "The plan quantity for the subscription."

  - name: "plan_unit_price"
    type: "integer"
    description: "The amount that will override the plan's default price."

  - name: "po_number"
    type: "string"
    description: "The purchase order number associated with the subscription."

  - name: "referral_info"
    type: "object"
    description: "The referral details for the subscription, if applicable."
    subattributes:
      - name: "account_id"
        type: "string"
        description: "The referral account ID."

      - name: "campaign_id"
        type: "string"
        description: "The referral campaign ID."

      - name: "coupon_code"
        type: "string"
        description: "The referral coupon code."

      - name: "destination_url"
        type: "string"
        description: "The destination URL for the campaign."

      - name: "external_campaign_id"
        type: "string"
        description: "The campaign ID in an external reference system."

      - name: "external_reference_id"
        type: "string"
        description: "The reference ID in an external reference system."

      - name: "friend_offer_type"
        type: "string"
        description: |
          The friend offer type for the referral campaign. Possible values are:

          - `none`
          - `coupon`
          - `coupon_code`

      - name: "notify_referral_system"
        type: "string"
        description: |
          Indicates whether referral purchases should be notified to the referral system. Possible values are:

          - `none`
          - `first_paid_conversion`
          - `all_invoices`

      - name: "post_purchase_widget_enabled"
        type: "boolean"
        description: "Indicates if a post purchase widget is enabled for the campaign."

      - name: "referral_code"
        type: "string"
        description: "The referral code."

      - name: "referral_status"
        type: "string"
        description: ""

      - name: "referrer_id"
        type: "string"
        description: "The referrer ID."

      - name: "referrer_reward_type"
        type: "string"
        description: |
          The referrer reward type for the referral campaign. Possible values are:

          - `none`
          - `referral_direct_reward`
          - `custom_promotional_credit`
          - `custom_revenue_percent_based`

      - name: "referral_system"
        type: "string"
        description: ""

      - name: "reward_status"
        type: "string"
        description: |
          The reward status for the referral subscription. Possible values are:

          - `pending`
          - `paid`
          - `invalid`

  - name: "remaining_billing_cycles"
    type: "integer"
    description: "The number of billing cycles the subscription will run."

  - name: "resource_version"
    type: "integer"
    description: "The version number of the subscription. Each update of the subscription results in an incremental change of this value. **Note**: This attribute will be present only if the resource has been updated after 2016-09-28."

  - name: "resume_date"
    type: "date-time"
    description: ""

  - name: "setup_fee"
    type: "integer"
    description: ""

  - name: "shipping_address"
    type: "object"
    description: "The shipping address for the subscription."
    subattributes:
      - name: "city"
        type: "string"
        description: "The city."

      - name: "company"
        type: "string"
        description: "The company."

      - name: "country"
        type: "string"
        description: "The country."

      - name: "email"
        type: "string"
        description: "The email."

      - name: "first_name"
        type: "string"
        description: "The first name."

      - name: "last_name"
        type: "string"
        description: "The last name."

      - name: "line1"
        type: "string"
        description: "The first line of the address."

      - name: "line2"
        type: "string"
        description: "The second line of the address."

      - name: "line3"
        type: "string"
        description: "The third line of the address."

      - name: "phone"
        type: "string"
        description: "The phone number."

      - name: "state"
        type: "string"
        description: "The state or province."

      - name: "state_code"
        type: "string"
        description: "The ISO 3166-2 state/province code without the country prefix. Currently supported for USA, Canada and India."

      - name: "validation_status"
        type: "string"
        description: |
          The address verification status. Possible values are:

          - `not_validated`
          - `valid`
          - `partially_valid`
          - `invalid`

      - name: "zip"
        type: "string"
        description: "The zip or postal code."

  - name: "start_date"
    type: "date-time"
    description: |
      **Applicable only when `status: future`**. The scheduled start time of the future subscription.

  - name: "started_at"
    type: "date-time"
    description: |
      The time when the subscription started. This value will be `null` for future subscriptions.

  - name: "status"
    type: "string"
    description: |
      The current status of the subscription. Possible values are:

      - `future`
      - `in_trial`
      - `active`
      - `non_renewing`
      - `paused`
      - `cancelled`

  - name: "total_dues"
    type: "integer"
    description: ""

  - name: "trial_end"
    type: "date-time"
    description: |
      The end of the trial period for the subscription. The presence of this value for future subscriptions (`status: future`) implies the subscription will move to `in_trial` when the subscription starts.

  - name: "trial_start"
    type: "date-time"
    description: |
      The start of the trial period for the subscription. The presence of this value for future subscriptions (`status: future`) implies the subscription will move to `in_trial` when the subscription starts.  
---