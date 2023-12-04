---
tap: "chargebee"
version: "20-05-2019"
key: "event"

name: "events"
doc-link: "https://apidocs.chargebee.com/docs/api/events"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about the events that have occurred on your {{ integration.display_name }} site. Event records contain data about affected resources and additional details, such as when the change occurred. This can be used to create a log of events for a record and analyze how it has changed over time.

replication-method: "Key-based Incremental"

api-method:
    name: "List events"
    doc-link: "https://apidocs.chargebee.com/docs/api/events#list_events"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The event ID."
    foreign-key-id: "event-id"

  - name: "occurred_at"
    type: "date-time"
    replication-key: true
    description: "The time the event occurred."

  - name: "api_version"
    type: "string"
    description: "The Chargebee API Version used for rendering this event content. Possible values are `v1` or `v2`."

  - name: "content"
    type: "object"
    description: |
      The data associated with the event. The attributes in this object will vary depending on the event type. Refer to [{{ integration.display_name }}'s documentation](https://apidocs.chargebee.com/docs/api/events#event_types){:target="new"} for a list of possible event types.
    subattributes:
      - name: "coupon"
        type: "object"
        description: |
          Applicable when `events.event_type` is one of the following:

          - `coupon_created`
          - `coupon_updated`
          - `coupon_deleted`
          - `coupon_set_created`
          - `coupon_set_updated`
          - `coupon_set_deleted`
          - `coupon_codes_added`
          - `coupon_codes_deleted`
          - `coupon_codes_updated`
        subattributes:
          - name: "id"
            type: "string"
            description: "The coupon ID."
            foreign-key-id: "coupon-id"

          - name: "addon_constraint"
            type: "string"
            description: |
              The addons the coupon can be applied to. Possible values are:

              - `none`
              - `all`
              - `specific`
              - `not_applicable`

          - name: "apply_discount_on"
            type: "string"
            description: ""

          - name: "apply_on"
            type: "string"
            description: |
              The invoice items for which this coupon needs to be applied. Possible values are:

              - `invoice_amount`: The coupon will be applied to the total invoice amount.
              - `each_specified_item`: the discount will be applied to each specified plan and addon item.

          - name: "archived_at"
            type: "date-time"
            description: "The time when the coupon was archived."

          - name: "created_at"
            type: "date-time"
            description: "The time when the coupon was created."

          - name: "discount_amount"
            type: "number"
            description: "When `discount_type: fixed_amount`, this value will be the discount value in cents."

          - name: "discount_percentage"
            type: "number"
            description: "When `discount_type: percentage`, this value will be the discount value percentage."

          - name: "discount_type"
            type: "string"
            description: |
              The type of discount. Possible values are:

              - `fixed_amount`
              - `percentage`

          - name: "duration_month"
            type: "integer"
            description: |
              When `duration_type: limited_period`, this value will be the duration in months the coupon can be applied.

          - name: "duration_type"
            type: "string"
            description: |
              The duration the coupon is applicable. Possible values are:

              - `one_time`
              - `forever`
              - `limited_period`

          - name: "max_redemptions"
            type: "integer"
            description: "The maximum number of times the coupon can be redeemed."

          - name: "name"
            type: "string"
            description: "The display name used in web interface for identifying the coupon."

          - name: "object"
            type: "string"
            description: ""

          - name: "plan_constraint"
            type: "string"
            description: |
              The plans the coupon can be applied to. Possible values are:

              - `none`
              - `all`
              - `specific`
              - `not_applicable`

          - name: "redemptions"
            type: "integer"
            description: "The number of times the coupon has been redeemed."

          - name: "resource_version"
            type: "integer"
            description: "The version number of the coupon. Each update of the coupon results in an incremental change of this value. **Note**: This attribute will be present only if the coupon has been updated after 2016-09-28."

          - name: "status"
            type: "string"
            description: |
              The status of the coupon. Possible values are:

              - `active`
              - `expired`
              - `archived`
              - `deleted`

          - name: "updated_at"
            type: "date-time"
            description: "The time the coupon was last updated."

      - name: "customer"
        type: "object"
        description: |
          Applicable when `events.event_type` is one of the following:

          - `card_added`
          - `card_updated`
          - `card_expiry_reminder`
          - `card_expired`
          - `card_deleted`
          - `customer_created`
          - `customer_changed`
          - `customer_deleted`
          - `customer_moved_out`
          - `customer_moved_in`
          - `hierarchy_created`
          - `hierarchy_deleted`
          - `promotional_credits_added`
          - `promotional_credits_deducted`
          - `subscription_created`
          - `subscription_started`
          - `subscription_trial_end_reminder`
          - `subscription_activated`
          - `subscription_changed`
          - `subscription_cancellation_scheduled`
          - `subscription_cancellation_reminder`
          - `subscription_cancelled`
          - `subscription_reactivated`
          - `subscription_renewed`
          - `subscription_scheduled_cancellation_removed`
          - `subscription_changes_scheduled`
          - `subscription_scheduled_changes_removed`
          - `subscription_shipping_address_updated`
          - `subscription_deleted`
          - `subscription_paused`
          - `subscription_pause_scheduled`
          - `subscription_scheduled_pause_removed`
          - `subscription_resumed`
          - `subscription_resumption_scheduled`
          - `subscription_scheduled_resumption_removed`
          - `subscription_renewal_reminder`
          - `payment_source_added`
          - `payment_source_updated`
          - `payment_source_deleted`
          - `payment_succeeded`
          - `payment_failed`
          - `payment_refunded`
          - `payment_initiated`
          - `refund_initiated`
          - `virtual_bank_account_added`
          - `virtual_bank_account_updated`
          - `virtual_bank_account_deleted`
        subattributes:
          - name: "id"
            type: "string"
            description: "The customer ID."
            foreign-key-id: "customer-id"

          - name: "allow_direct_debit"
            type: "boolean"
            description: "Indicates whether the customer can pay via direct debit or not."

          - name: "auto_collection"
            type: "string"
            description: |
              Indicates whether payments need to be automatically collected for the customer. Possible values are:

              - `on`: When an invoice is created, an automatic attempt to charge the customer's payment method is made.
              - `off`: Automatic collection of charges will not be made.

          - name: "balances"
            type: "array"
            description: "The list of balances for the customer."
            subattributes:
              - name: "currency_code"
                type: "string"
                description: "The currency code in ISO 4217 for the balance."

              - name: "excess_payments"
                type: "integer"
                description: "The total unused payments associated with the customer."

              - name: "promotional_credits"
                type: "integer"
                description: "The promotional credits balance for the customer."

              - name: "refundable_credits "
                type: "integer"
                description: "The refundable credits balance for the customer."

              - name: "unbilled_charges"
                type: "integer"
                description: "The total unbilled charges for the customer."

          - name: "billing_address"
            type: "object"
            description: "The billing address for the customer."
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

          - name: "billing_date"
            type: "boolean"
            description: "**Applicable when calendar billing (with customer specific billing date support) is enabled**. When set, renewals of all the monthly and yearly subscriptions of this customer will be aligned to this date."

          - name: "billing_date_mode"
            type: "string"
            description: |
              Indicates whether this customer's `billing_date` value is derived as per configurations or its specifically set (overriden). When specifically set, the `billing_date` will not be reset even when all of the monthly/yearly subscriptions are cancelled.

              Possible values are:

              - `using_defaults`: The `billing_date` value is set based on configured defaults.
              - `manually_set`: The `billing_date` is specifically set.

          - name: "billing_day_of_week"
            type: "boolean"
            description: |
              **Applicable when calendar billing (with customer specific billing date support) is enabled**. When set, renewals of all the weekly subscriptions of this customer will be aligned to this week day.

              Possible values are:

              - `monday`
              - `tuesday`
              - `wednesday`
              - `thursday`
              - `friday`
              - `saturday`
              - `sunday`

          - name: "billing_day_of_week_mode"
            type: "string"
            description: |
              Indicates whether this customer's `billing_day_of_week` value is derived as per configurations or its specifically set (overriden). When specifically set, the `billing_day_of_week` will not be reset even when all of the weekly subscriptions are cancelled.

              Possible values are:

              - `using_defaults`: The `billing_day_of_week` value is set based on configured defaults.
              - `manually_set`: The `billing_day_of_week` is specifically set.

          - name: "card_status"
            type: "string"
            description: ""

          - name: "cf_company_id"
            type: "integer"
            description: ""

          - name: "company"
            type: "string"
            description: "The name of the company associated with the customer."

          - name: "consolidated_invoicing"
            type: "boolean"
            description: "**Applicable when consolidated invoicing is enabled**. Indicates whether invoice consolidation should happen during subscription renewals. Needs to be set only if this value is different from the defaults configured."

          - name: "contacts"
            type: "array"
            description: "A list of contacts associated with the customer."
            subattributes:
              - name: "email"
                type: "string"
                description: "The contact's email."

              - name: "enabled"
                type: "boolean"
                description: "Indicates whether the contacted is enabled (`true`) or disabled (`false`)."

              - name: "first_name"
                type: "string"
                description: "The first name of the contact."

              - name: "id"
                type: "string"
                description: "The contact ID."

              - name: "label"
                type: "string"
                description: "The label/tag provided for the contact."

              - name: "last_name"
                type: "string"
                description: "The last name of the contact."

              - name: "object"
                type: "string"
                description: ""

              - name: "phone"
                type: "string"
                description: "The phone number of the contact."

              - name: "send_account_email"
                type: "string"
                description: "Indicates whether account emails are enabled for the contact."

              - name: "send_billing_email"
                type: "string"
                description: "Indicates whether billing emails are enabled for the contact."

          - name: "created_at"
            type: "date-time"
            description: "The time the customer was created."

          - name: "deleted"
            type: "boolean"
            description: "Indicates whether the customer has been deleted or not."

          - name: "email"
            type: "string"
            description: "The customer's email address."

          - name: "excess_payments"
            type: "integer"
            description: "The total unused payments associated with the customer."

          - name: "first_name"
            type: "string"
            description: "The first name of the customer."

          - name: "invoice_notes"
            type: "string"
            description: "Invoice notes associated with the customer."

          - name: "last_name"
            type: "string"
            description: "The last name of the customer."

          - name: "locale"
            type: "string"
            description: "Determines which region-specific language {{ integration.display_name }} uses to communicate with the customer."

          - name: "net_term_days"
            type: "integer"
            description: "The number of days within which the customer has to make payment for invoices."

          - name: "object"
            type: "string"
            description: ""

          - name: "payment_method"
            type: "object"
            description: "The primary payment source for the customer."
            subattributes:
              - name: "gateway"
                type: "string"
                description: |
                  The name of the gateway the payment is associated with. Refer to [{{ integration.display_name }}'s documentation](https://apidocs.chargebee.com/docs/api/customers#customer_payment_method_gateway){:target="new"} for a full list of possible values.
                doc-link: "https://apidocs.chargebee.com/docs/api/customers#customer_payment_method_gateway"

              - name: "gateway_account_id"
                type: "string"
                description: "The gateway account the payment method is stored with."

              - name: "object"
                type: "string"
                description: ""

              - name: "reference_id"
                type: "string"
                description: |
                  The reference ID.

                  - For **Amazon** and **PayPal**, this will be the billing agreement ID.
                  - For **GoCardless direct debit**, this will be the mandate ID.
                  - For **card payments**, this will be the ID provided by the gateway/card vault for the specific payment method.

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

          - name: "phone"
            type: "string"
            description: "The customer's phone number."

          - name: "pii_cleared"
            type: "string"
            description: |
              Indicates whether the customer's personal info has been cleared. Possible values are:

              - `active`
              - `scheduled_for_clear`
              - `cleared`

          - name: "preferred_currency_code"
            type: "string"
            description: "**Applicable if the {{ integration.display_name }} Multicurrency feature is enabled.** The currency code of the customer's preferred currency (ISO 4217 format)."

          - name: "primary_payment_source_id"
            type: "string"
            description: "The ID of the primary payment source for the customer."

          - name: "promotional_credits"
            type: "integer"
            description: "The promotional credits balance of the customer."

          - name: "referral_urls"
            type: "array"
            description: "A list of referral URLs for the customer."
            subattributes:
              - name: "created_at"
                type: "date-time"
                description: "The time the referral URL was created."

              - name: "external_customer_id"
                type: "string"
                description: "The ID of the external customer in the referral system."

              - name: "referral_account_id"
                type: "string"
                description: "The ID of the referral account."

              - name: "referral_campaign_id"
                type: "string"
                description: "The ID of the referral campaign."

              - name: "referral_external_account_id"
                type: "string"
                description: "The ID of the external referral account."

              - name: "referral_sharing_url"
                type: "string"
                description: "The referral sharing URL for the customer."

              - name: "referral_system"
                type: "string"
                description: |
                  The URL for the referral system account. Possible values are:

                  - `referral_candy`
                  - `referral_saasquatch`
                  - `friendbuy`

              - name: "updated_at"
                type: "date-time"
                description: "The time the referral URL was last updated."

          - name: "refundable_credits"
            type: "integer"
            description: "The refundable credits balance of the customer."

          - name: "resource_version"
            type: "integer"
            description: "The version number of the customer. Each update of the customer results in an incremental change of this value. **Note**: This attribute will be present only if the customer has been updated after 2016-09-28."

          - name: "taxability"
            type: "string"
            description: |
              Indicates if the customer is liable for tax. Possible values are:

              - `taxable`
              - `exempt`

          - name: "unbilled_charges"
            type: "integer"
            description: "The total unbilled charges for the customer."

          - name: "updated_at"
            type: "date-time"
            description: "The time the customer was last updated."

          - name: "vat_number"
            type: "string"
            description: "The VAT number for the customer."

      - name: "invoice"
        type: "object"
        description: |
          Applicable when `events.event_type` is one of the following:

          - `invoice_generated`
          - `invoice_updated`
          - `invoice_deleted`
          - `pending_invoice_created`
          - `pending_invoice_updated`
          - `payment_failed`
          - `payment_initiated`
          - `payment_refunded`
          - `refund_initiated`
          - `subscription_created`
          - `subscription_started`
          - `subscription_activated`
          - `subscription_changed`
          - `subscription_cancelled`
          - `subscription_reactivated`
          - `subscription_renewed`
          - `subscription_paused`
          - `subscription_resumed`
        subattributes:
          - name: "id"
            type: "string"
            description: "The invoice ID."
            foreign-key-id: "invoice-id"

          - name: "updated_at"
            type: "date-time"
            description: "The time the invoice was last updated."

          - name: "adjustment_credit_notes"
            type: "array"
            description: "Details about the adjustments created for the invoice."
            subattributes: &credit-note
              - name: "cn_date"
                type: "date-time"
                description: "The date at which the credit note was created."

              - name: "cn_id"
                type: "string"
                description: "The credit note ID."
                foreign-key-id: "credit-note-id"

              - name: "cn_reason_code"
                type: "string"
                description: &cn-reason-code |
                  The reason for the credit note. Possible values are:

                  - `write_off`
                  - `subscription_change`
                  - `subscription_cancellation`
                  - `subscription_pause`
                  - `chargeback`
                  - `product_unsatisfactory`
                  - `service_unsatisfactory`
                  - `order_change`
                  - `order_cancellation`
                  - `waiver`
                  - `other`
                  - `fraudulent`

              - name: "cn_status"
                type: "string"
                description: &cn-status |
                  The status of the credit note. Possible values are:

                  - `adjusted`
                  - `refunded`
                  - `refund_due`
                  - `voided`

              - name: "cn_total"
                type: "integer"
                description: "The total amount of the credit note."

          - name: "amount_adjusted"
            type: "integer"
            description: "The total adjusted amount made against the invoice."

          - name: "amount_due"
            type: "integer"
            description: "The total amount to be collected, include the invoice's payments in progress."

          - name: "amount_paid"
            type: "integer"
            description: "The total payments received for the invoice."

          - name: "amount_to_collect"
            type: "integer"
            description: "The total amount to be collected."

          - name: "applied_credits"
            type: "array"
            description: "The refundable credits applied on the invoice."
            subattributes:
              - name: "applied_amount"
                type: "integer"
                description: "The applied amount, in cents."

              - name: "applied_at"
                type: "date-time"
                description: "The time the credit was applied."

              - name: "cn_date"
                type: "date-time"
                description: "The date the credit was created."

              - name: "cn_id"
                type: "string"
                description: "The credit ID."
                foreign-key-id: "credit-note-id"

              - name: "cn_reason_code"
                type: "string"
                description: *cn-reason-code

              - name: "cn_status"
                type: "string"
                description: *cn-status

          - name: "base_currency_code"
            type: "string"
            description: ""

          - name: "billing_address"
            type: "object"
            description: "The billing address for the invoice."
            subattributes: &address
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

          - name: "credits_applied"
            type: "integer"
            description: "The total credits applied against the invoice."

          - name: "currency_code"
            type: "string"
            description: "The currency code (ISO 4217 format) for the invoice."

          - name: "customer_id"
            type: "string"
            description: "The ID of the customer the invoice is for."
            foreign-key-id: "customer-id"

          - name: "date"
            type: "date-time"
            description: |
              Closing date of the invoice. Typically this is the date on which invoice is generated. If "wait & notify to send invoices enabled for usage based billing" is enabled in {{ integration.display_name }}, this will not be the same as date on which invoice was actually sent to customer.

          - name: "deleted"
            type: "boolean"
            description: "Indicates if the invoice has been deleted or not."

          - name: "discounts"
            type: "array"
            description: "Details about the discounts applied to the invoice."
            subattributes:
              - name: "amount"
                type: "integer"
                description: "The discount amount, in cents."

              - name: "description"
                type: "string"
                description: "The description of the discount line item."

              - name: "entity_id"
                type: "string"
                description: "The ID of the entity the discount amount is based on. This value will only be present if `entity_type` is `item_level_coupon` or `document_level_coupon`."
                foreign-key-id: "coupon-id"

              - name: "entity_type"
                type: "string"
                description: &discount-line-item |
                  The type of the discount line item. Possible values are:

                  - `item_level_coupon`: Represents item-level coupons applied to the invoice.
                  - `document_level_coupon`: Represents document-level coupons applied to the document.
                  - `promotional_credits`: Represents promotional credits in the invoice.
                  - `prorated_credits`: Represents credit adjustments in the invoice.

          - name: "due_date"
            type: "date-time"
            description: "The due date of the invoice."

          - name: "dunning_status"
            type: "string"
            description: |
              The current dunning status of the invoice. Possible values are:

              - `in_progress`
              - `exhausted`
              - `stopped`
              - `success`

          - name: "exchange_rate"
            type: "number"
            description: ""

          - name: "expected_payment_date"
            type: "date-time"
            description: "The expected payment date recorded for the invoice."

          - name: "first_invoice"
            type: "boolean"
            description: "Indicates if this is the first invoice raised for the subscription. If this is a non-recurring invoice, it indicates if this is the first invoice for the customer."

          - name: "has_advance_charges"
            type: "boolean"
            description: "Indicates if there are any advanced charges present in the invoice."

          - name: "is_gifted"
            type: "boolean"
            description: "Indicates if the invoice is gifted or not."

          - name: "issued_credit_notes"
            type: "array"
            description: "A list of credit notes issued for the invoice."
            subattributes: *credit-note

          - name: "line_item_discounts"
            type: "array"
            description: "The list of discounts applied for each line item in the invoice."
            subattributes:
              - name: "coupon_id"
                type: "string"
                description: "The coupon ID."
                foreign-key-id: "coupon-id"

              - name: "discount_amount"
                type: "integer"
                description: "The amount of the discount."

              - name: "discount_type"
                type: "string"
                description: |
                  The type of discount. Possible values are:

                  - `fixed_amount`
                  - `percentage`

              - name: "line_item_id"
                type: "string"
                description: "The ID of the line item the discount was applied to."
                foreign-key-id: "line-item-id"

          - name: "line_item_taxes"
            type: "array"
            description: "The list of taxes applied on line items."
            subattributes:
              - name: "line_item_id"
                type: "string"
                description: "The ID of the line item for which the tax is applicable."
                foreign-key-id: "line-item-id"

              - name: "tax_amount"
                type: "integer"
                description: "The tax amount, in cents."

              - name: "tax_juris_code"
                type: "string"
                description: "The tax jurisdiction code."

              - name: "tax_juris_name"
                type: "string"
                description: "The name of the tax jurisdiction."

              - name: "tax_juris_type"
                type: "string"
                description: |
                  The type of tax jurisdiction. Possible values are:

                  - `country`
                  - `federal`
                  - `state`
                  - `county`
                  - `city`
                  - `special`
                  - `unincorporated` (Combined tax of state and country)
                  - `other`

              - name: "tax_name"
                type: "string"
                description: "The name of the tax applied."

              - name: "tax_rate"
                type: "number"
                description: "The rate of tax used to calculate the tax amount."

          - name: "line_items"
            type: "array"
            description: "The line items in the invoice."
            subattributes:
              - name: "amount"
                type: "integer"
                description: "The total amount of the line item, calculated as `unit_amount x quantity`."

              - name: "date_from"
                type: "date-time"
                description: "The start date of the line item."

              - name: "date_to"
                type: "date-time"
                description: "The end date of the line item."

              - name: "description"
                type: "string"
                description: "The description of the line item."

              - name: "discount_amount"
                type: "integer"
                description: "The discount amount applied to the line item, in cents."

              - name: "entity_id"
                type: "string"
                description: |
                  The ID of the entity the line item is based on.

              - name: "entity_type"
                type: "string"
                description: |
                  The modelled entity (plan, addon, etc.) this line item is based on. Possible values are:

                  - `plan_setup`: The line item is based on a plan setup charge. The `entity_id` will specify the plan ID ([`plans: id`](#plans)).
                  - `plan`: The line item is based on a plan entity. The `entity_id` will specify the plan ID ([`plans: id`](#plans)).
                  - `addon`: The line item is based on an addon entity. The `entity_id` will specify the addon ID ([`addons: id`](#addons)).
                  - `adhoc`: The line item is not modelled. The `entity_id` attribute will be `null`.

              - name: "id"
                type: "string"
                description: "The line item ID."
                foreign-key-id: "line-item-id"

              - name: "is_taxed"
                type: "boolean"
                description: "Indicates whether the line item is taxed or not."

              - name: "item_level_discount_amount"
                type: "integer"
                description: "The item level discount amount for the line item, in cents."

              - name: "pricing_model"
                type: "string"
                description: |
                  Indicates how the charges for the line item are calculated. Possible values are:

                  - `flat_fee`: Charges single price on a recurring basis.
                  - `per_unit`: Charges the price for each unit of the plan for the subscription on a recurring basis.
                  - `tiered`: Charges different per unit price for the quantity purchased from every tier.
                  - `volume`: Charges the per unit price for the total quantity purchased based on the tier under which it falls.
                  - `stairstep`: Charges a price for a range.

              - name: "quantity"
                type: "integer"
                description: "The quantity of the recurring item, represented by the line item."

              - name: "subscription_id"
                type: "string"
                description: "The ID of the subscription associated with the line item."
                foreign-key-id: "subscription-id"

              - name: "tax_amount"
                type: "integer"
                description: "The tax amount of the line item, in cents."

              - name: "tax_exempt_reason"
                type: "string"
                description: |
                  The reason or category for why the line item is excluded from the taxable amount. Possible values are:

                  - `tax_not_configured`
                  - `region_non_taxable`
                  - `export`
                  - `customer_exempt`
                  - `zero_rated`
                  - `reverse_charge`
                  - `high_value_physical_good`

              - name: "tax_rate"
                type: "number"
                description: "The rate of tax used to calculate tax for the line item."

              - name: "unit_amount"
                type: "integer"
                description: "The unit amount of the line item, in cents."

          - name: "linked_orders"
            type: "array"
            description: "A list of orders associated with the invoice."
            subattributes:
              - name: "batch_id"
                type: "string"
                description: "The batch ID."

              - name: "created_at"
                type: "date-time"
                description: "the time the order was created."

              - name: "fulfillment_status"
                type: "string"
                description: "The fulfillment status of an order as reflected in the shipping/order management application. Typical statuses include `Shipped`, `Awaiting Shipment`, `Not fulfilled`, etc."

              - name: "id"
                type: "string"
                description: "The order ID."

              - name: "reference_id"
                type: "string"
                description: "This attribute can be used to map the orders in the shipping/order management application to the orders in {{ integration.display_name }}. The `reference_id` generally is same as the order id in the third party application."

              - name: "status"
                type: "string"
                description: |
                  The status of the order. Possible values include:

                  - `new`
                  - `processing`
                  - `complete`
                  - `cancelled`
                  - `voided`
                  - `queued`
                  - `awaiting_shipment`
                  - `on_hold`
                  - `delivered`
                  - `shipped`
                  - `partially_delivered`
                  - `returned`

          - name: "linked_payments"
            type: "array"
            description: "The list of payment transactions for the invoice."
            subattributes:
              - name: "applied_amount"
                type: "integer"
                description: "The transaction amount applied to the invoice."

              - name: "applied_at"
                type: "date-time"
                description: "The time the amount was applied."

              - name: "txn_amount"
                type: "integer"
                description: "The total amount of the transaction."

              - name: "txn_date"
                type: "date-time"
                description: "The date the transaction occured."

              - name: "txn_id"
                type: "string"
                description: "the transaction ID."
                foreign-key-id: "transaction-id"

              - name: "txn_status"
                type: "string"
                description: |
                  The status of the transaction. Possible values are:

                  - `in_progress`
                  - `success`
                  - `voided`
                  - `failure`
                  - `timeout`
                  - `needs_attention`

          - name: "net_term_days"
            type: "integer"
            description: "The number of days within which the invoice has to be paid."

          - name: "new_sales_amount"
            type: "integer"
            description: ""

          - name: "next_retry_at"
            type: "date-time"
            description: "A timestamp indicating when the next attempt to collect payment for this invoice will occur."

          - name: "notes"
            type: "array"
            description: |
              The list of notes associated with the invoice. If entity_type & entity_id are not present, then it is general notes (i.e Notes input provided under **Customize Invoice** action in {{ integration.display_name }} web interface).
            subattributes:
              - name: "entity_id"
                type: "string"
                description: "The entity ID."

              - name: "entity_type"
                type: "string"
                description: |
                  The type of entity the note belongs to. Possible values are:

                  - [`plan`](#plans)
                  - [`addon`](#addons)
                  - [`coupon`](#coupons)
                  - [`subscription`](#subscriptions)
                  - [`customer`](#customers)

              - name: "note"
                type: "string"
                description: "The content of the note."

          - name: "object"
            type: "string"
            description: ""

          - name: "paid_at"
            type: "date-time"
            description: "The time the invoice was paid."

          - name: "po_number"
            type: "string"
            description: "The number of the purchase order associated with the invoice."

          - name: "price_type"
            type: "string"
            description: |
              The price type of the invoice. Possible values are:

                - `tax_exclusive`
                - `tax_inclusive`

          - name: "recurring"
            type: "boolean"
            description: "Indicates if the invoice belongs to a subscription or not."

          - name: "resource_version"
            type: "integer"
            description: "The version number of the invoice. Each update of the invoice results in an incremental change of this value. **Note**: This attribute will be present only if the invoice has been updated after 2016-09-28."

          - name: "round_off_amount"
            type: "integer"
            description: "The invoice rounded-off amount, in cents."

          - name: "shipping_address"
            type: "object"
            description: "The shipping address for the invoice."
            subattributes: *address

          - name: "status"
            type: "string"
            description: |
              The status of the invoice. Possible values are:

              - `paid`
              - `posted`
              - `payment_due`
              - `not_paid`
              - `voided`
              - `pending`

          - name: "sub_total"
            type: "integer"
            description: "The subtotal of the invoice, in cents."

          - name: "subscription_id"
            type: "string"
            description: "The ID of the subscription associated with the invoice."
            foreign-key-id: "subscription-id"

          - name: "tax"
            type: "integer"
            description: "The total tax amount for the invoice, in cents."

          - name: "taxes"
            type: "array"
            description: ""
            subattributes:
              - name: "amount"
                type: "integer"
                description: "The tax amount, in cents."

              - name: "description"
                type: "string"
                description: "The description of the tax item."

              - name: "name"
                type: "string"
                description: "The name of the tax applied. For example: `GST`"

          - name: "term_finalized"
            type: "boolean"
            description: "Indicates if the invoice line item terms are finalized or not."

          - name: "total"
            type: "integer"
            description: "The total invoiced amount, in cents."

          - name: "vat_number"
            type: "string"
            description: "The VAT number."

          - name: "voided_at"
            type: "date-time"
            description: "The time the invoice was voided."

          - name: "write_off_amount"
            type: "integer"
            description: "The amount written off against the invoice, in cents."

      - name: "plan"
        type: "object"
        description: |
          Applicable when `events.event_type` is one of the following:

          - `plan_created`
          - `plan_updated`
          - `plan_deleted`

        subattributes:
          - name: "billing_cycles"
            type: "integer"
            description: "The number of billing cycles the subscription is active."

          - name: "charge_model"
            type: "string"
            description: |
              Defines how the recurring charges for the subscription are calculated. Possible values are:

              - `flat_fee`
              - `per_unit`
              - `tiered`
              - `volume`
              - `stairstep`

          - name: "description"
            type: "string"
            description: "The description of the plan to show in hosted pages and the customer portal."

          - name: "free_quantity"
            type: "integer"
            description: "The free quantity the subscriptions of the plan will have. Only quantities more than this value will be charged for the subscription."

          - name: "id"
            type: "string"
            description: "The plan ID."
            foreign-key-id: "plan-id"

          - name: "invoice_notes"
            type: "string"
            description: "Invoice notes associated with the subscription."

          - name: "name"
            type: "string"
            description: "The display name of the plan."

          - name: "period"
            type: "integer"
            description: |
              Defines the billing frequency for the plan. Used with `period_unit` to create a billing schedule for the plan.

              For example: If `period_unit: week` and `period: 3`, billing would occur every `3 weeks`.

          - name: "period_unit"
            type: "string"
            description: |
              The time unit for the billing period. Used with `period` to create a billing schedule for the plan.

              For example: If `period_unit: week` and `period: 3`, billing would occur every `3 weeks`.

              Possible values are:

              - `day`
              - `week`
              - `month`
              - `year`

          - name: "price"
            type: "integer"
            description: "The price of the plan."

          - name: "redirect_url"
            type: "string"
            description: "The URL to redirect on successful checkout."

          - name: "setup_cost"
            type: "integer"
            description: "The one-time setup fee charged as part of the first invoice for the plan."

          - name: "sku"
            type: "string"
            description: "Ssed as Product name/code in your third party accounting application. {{ integration.display_name }} will use it as an alternate name in your accounting application."

          - name: "status"
            type: "string"
            description: |
              The plan state. Possible values are:

              - `active`
              - `archived`

          - name: "tax_profile_id"
            type: "string"
            description: "The ID of the tax profile for the plan."

          - name: "taxable"
            type: "boolean"
            description: "Indicates if the plan is taxable or not."

          - name: "trial_period"
            type: "integer"
            description: |
              The free time window for the customer to try the product. Used with `trial_period_unit` to create the free trial period.

              For example: If `trial_period: day` and `trial_period_unit: 14`, the trial period would be `14 days`.

          - name: "trial_period_unit"
            type: "string"
            description: |
              The time unit for the trial period. Used with `trial_period` to create the free trial period.

              For example: If `trial_period: day` and `trial_period_unit: 14`, the trial period would be `14 days`.

              Possible values are:

              - `day`
              - `month`

          - name: "updated_at"
            type: "date-time"
            description: "The time the plan was last updated."

      - name: "subscription"
        type: "object"
        description: |
          Applicable when `events.event_type` is one of the following:

          - `customer_deleted`
          - `payment_succeeded`
          - `payment_failed`
          - `payment_refunded`
          - `payment_initiated`
          - `refund_initiated`
          - `subscription_created`
          - `subscription_started`
          - `subscription_trial_end_reminder`
          - `subscription_activated`
          - `subscription_changed`
          - `subscription_cancellation_scheduled`
          - `subscription_cancellation_reminder`
          - `subscription_cancelled`
          - `subscription_reactivated`
          - `subscription_renewed`
          - `subscription_scheduled_cancellation_removed`
          - `subscription_changes_scheduled`
          - `subscription_scheduled_changes_removed`
          - `subscription_shipping_address_updated`
          - `subscription_deleted`
          - `subscription_paused`
          - `subscription_pause_scheduled`
          - `subscription_scheduled_pause_removed`
          - `subscription_resumed`
          - `subscription_resumption_scheduled`
          - `subscription_scheduled_resumption_removed`
          - `subscription_renewal_reminder`
        subattributes:
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

          - name: "currency_code"
            type: "string"
            description: "The currency code for the subscription in ISO 4217 format."

          - name: "current_term_end"
            type: "date-time"
            description: "The end of the current billing term for the subscription, after which the subscription will be immediately renewed."

          - name: "current_term_start"
            type: "date-time"
            description: "The start of the current billing term for the subscription."

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

          - name: "has_scheduled_changes"
            type: "boolean"
            description: "If true, there are subscription changes scheduled on next renewal."

          - name: "id"
            type: "string"
            description: "The subscription ID."
            foreign-key-id: "subscription-id"

          - name: "invoice_notes"
            type: "string"
            description: "The invoice notes for the subscription."

          - name: "mrr"
            type: "integer"
            description: "The monthly recurring revenue for the subscription, in cents."

          - name: "next_billing_at"
            type: "date-time"
            description: "The date on which the next billing occurs."

          - name: "object"
            type: "string"
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

          - name: "trial_end"
            type: "date-time"
            description: |
              The end of the trial period for the subscription. The presence of this value for future subscriptions (`status: future`) implies the subscription will move to `in_trial` when the subscription starts.

          - name: "trial_start"
            type: "date-time"
            description: |
              The start of the trial period for the subscription. The presence of this value for future subscriptions (`status: future`) implies the subscription will move to `in_trial` when the subscription starts.

          - name: "updated_at"
            type: "date-time"
            description: "The time the subscription was last updated."

      - name: "transaction"
        type: "object"
        description: |
          Applicable when `events.event_type` is one of the following:

          - `authorization_succeeded`
          - `authorization_voided`
          - `payment_succeeded`
          - `payment_failed`
          - `payment_refunded`
          - `payment_initiated`
          - `refund_initiated`
          - `transaction_created`
          - `transaction_updated`
          - `transaction_deleted`
        subattributes:
            - name: "amount"
              type: "integer"
              description: "The amount for the transaction."

            - name: "amount_unused"
              type: "integer"
              description: "**Applicable only for payments.** The unused amount present for the transaction."

            - name: "base_currency_code"
              type: "string"
              description: ""

            - name: "currency_code"
              type: "string"
              description: "The currency code for the transaction, in ISO 4217 format."

            - name: "customer_id"
              type: "string"
              description: "The ID of the customer associated with the transaction."
              foreign-key-id: "customer-id"

            - name: "date"
              type: "date-time"
              description: "The date the transaction occurred."

            - name: "deleted"
              type: "boolean"
              description: "Indicates if the transaction has been deleted."

            - name: "error_code"
              type: "string"
              description: "The error code received from the payment gateway on failure."

            - name: "error_text"
              type: "string"
              description: "The error message received from the payment gateway on failure."

            - name: "exchange_rate"
              type: "number"
              description: ""

            - name: "fraud_flag"
              type: "string"
              description: |
                Indicates whether or not the transaction has been identified as fraudulent. Possible values are:

                - `safe`
                - `suspicious`
                - `fraudulent`

            - name: "fraud_reason"
              type: "string"
              description: "A short description why the transaction was marked as fraudulent or suspicious."

            - name: "gateway"
              type: "string"
              description: "The name of the gateway used to process the transaction."

            - name: "gateway_account_id"
              type: "string"
              description: "The account ID of the gateway used to process the transaction."

            - name: "id"
              type: "string"
              description: "The transaction ID."
              foreign-key-id: "transaction-id"

            - name: "id_at_gateway"
              type: "string"
              description: "The ID with which the transaction is referred in the `gateway`."

            - name: "linked_credit_notes"
              type: "array"
              description: "**Applicable only for refund transactions.** The list of credit notes the transaction is associated with."
              subattributes:
                - name: "applied_amount"
                  type: "integer"
                  description: "The transaction amount applied to the invoice."

                - name: "applied_at"
                  type: "date-time"
                  description: "The time the credit note was applied."

                - name: "cn_date"
                  type: "date-time"
                  description: "The date the credit note was created."

                - name: "cn_id"
                  type: "string"
                  description: "The credit note ID."
                  foreign-key-id: "credit-note-id"

                - name: "cn_reason_code"
                  type: "string"
                  description: |
                    The reason for the credit note. Possible values are:

                    - `write_off`
                    - `subscription_change`
                    - `subscription_cancellation`
                    - `subscription_pause`
                    - `chargeback`
                    - `product_unsatisfactory`
                    - `service_unsatisfactory`
                    - `order_change`
                    - `order_cancellation`
                    - `waiver`
                    - `other`
                    - `fraudulent`

                - name: "cn_reference_invoice_id"
                  type: "string"
                  description: "The invoice ID."
                  foreign-key-id: "invoice-id"

                - name: "cn_status"
                  type: "string"
                  description: |
                    The status of the credit note. Possible values are:

                    - `adjusted`
                    - `refunded`
                    - `refund_due`
                    - `voided`

                - name: "cn_total"
                  type: "integer"
                  description: "The total amount of the credit note."

            - name: "linked_invoices"
              type: "array"
              description: "**Applicable only for payment transactions.** The list of invoices the transaction has been applied to."
              subattributes:
                - name: "applied_amount"
                  type: "integer"
                  description: "The transaction amount applied to the invoice."

                - name: "applied_at"
                  type: "date-time"
                  description: "The time at which the transaction was applied."

                - name: "invoice_date"
                  type: "date-times"
                  description: "The date the invoice was issued."

                - name: "invoice_id"
                  type: "string"
                  description: "The invoice ID."
                  foreign-key-id: "invoice-id"

                - name: "invoice_status"
                  type: "string"
                  description: |
                    The current status of the invoice. Possible values are:

                    - `paid`
                    - `posted`
                    - `payment_due`
                    - `not_paid`
                    - `voided`
                    - `pending`

                - name: "invoice_total"
                  type: "integer"
                  description: "The total amount of the invoice."

            - name: "linked_refunds"
              type: "array"
              description: "**Applicable only for payment transactions.** The list of refunds issued for the payment transaction."
              subattributes:
                - name: "txn_amount"
                  type: "integer"
                  description: "The total amount of the transaction."

                - name: "txn_date"
                  type: "date-time"
                  description: "The date the transaction occured."

                - name: "txn_id"
                  type: "string"
                  description: "the transaction ID."
                  foreign-key-id: "transaction-id"

                - name: "txn_status"
                  type: "string"
                  description: |
                    The status of the transaction. Possible values are:

                    - `in_progress`
                    - `success`
                    - `voided`
                    - `failure`
                    - `timeout`
                    - `needs_attention`

            - name: "masked_card_number"
              type: "string"
              description: "**Applicable only when `payment_method: card`.** The masked card number used for the transaction."

            - name: "object"
              type: "string"
              description: ""

            - name: "payment_method"
              type: "string"
              description: |
                The payment method for the transaction. Possible values are:

                - `card`
                - `cash`
                - `check`
                - `chargeback`
                - `bank_transfer`
                - `amazon_payments`
                - `paypal_express_checkout`
                - `direct_debit`
                - `alipay`
                - `unionpay`
                - `apple_pay`
                - `wechat_pay`
                - `ach_credit`
                - `other`

            - name: "payment_source_id"
              type: "string"
              description: "The ID of the payment source used for the transaction."
              foreign-key-id: "payment-source-id"

            - name: "reference_number"
              type: "string"
              description: "The reference number for the transaction."

            - name: "reference_transaction_id"
              type: "string"
              description: "**Applicable only when `type` is `refund` or `payment_reversal`.** The reference payment ID."
              foreign-key-id: "transaction-id"

            - name: "refunded_txn_id"
              type: "string"
              description: "**Applicable only when `type: refund`**. The ID of the original transaction that was refunded."
              foreign-key-id: "transaction-id"

            - name: "resource_version"
              type: "integer"
              description: "The version number of the transaction. Each update of the transaction results in an incremental change of this value. **Note**: This attribute will be present only if the credit note has been updated after 2016-09-28."

            - name: "reversal_txn_id"
              type: "string"
              description: "**Applicable only when `type: payment_reversal`**. The ID of the original transaction that was reversed."

            - name: "settled_at"
              type: "date-time"
              description: "The time at which the final status of the transaction has been marked."

            - name: "status"
              type: "string"
              description: |
                The status of the transaction. Possible values are:

                - `in_progress`
                - `success`
                - `voided`
                - `failure`
                - `timeout`
                - `needs_attention`

            - name: "subscription_id"
              type: "string"
              description: "The ID of the subscription associated with the transaction."
              foreign-key-id: "subscription-id"

            - name: "type"
              type: "string"
              description: |
                The type of the transaction. Possible values are:

                - `authorization`
                - `payment`
                - `refund`
                - `payment_reversal`

            - name: "updated_at"
              type: "date-time"
              description: "The time the transaction was last updated."

            - name: "validated_at"
              type: "date-time"
              description: ""

  - name: "event_type"
    type: "string"
    description: |
      The event type. Refer to [{{ integration.display_name }}'s documentation](https://apidocs.chargebee.com/docs/api/events#event_types){:target="new"} for a full list of possible event types.
    doc-link: "https://apidocs.chargebee.com/docs/api/events#event_types"

  - name: "object"
    type: "string"
    description: ""

  - name: "source"
    type: "string"
    description: |
      The source of the event. Possible values are:

      - `admin_console`
      - `api`
      - `scheduled_job`
      - `hosted_page`
      - `portal`
      - `system`
      - `none`
      - `js_api`
      - `migration`
      - `bulk_operation`
      - `external_service`

  - name: "user"
    type: "string"
    description: "The event created by the user."

  - name: "webhook_status"
    type: "string"
    description: |
      The current status of the webhook for this event. Possible values are:

      - `not_configured`
      - `scheduled`
      - `succeeded`
      - `re_scheduled`
      - `failed`
      - `skipped`
      - `not_applicable`
    doc-link: "https://apidocs.chargebee.com/docs/api/events#event_webhooks"
---