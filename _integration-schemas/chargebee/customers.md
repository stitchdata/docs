---
tap: "chargebee"
version: "1"
key: "customers"

name: "customers"
doc-link: "https://apidocs.chargebee.com/docs/api/customers"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the customers in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List customers"
    doc-link: "https://apidocs.chargebee.com/docs/api/customers#list_customers"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the customer was last updated."

  - name: "allow_direct_debit"
    type: "boolean"
    description: "Indicates whether the customer can pay via direct debit or not."

  - name: "auto_collection"
    type: "string"
    description: |
      Indicates whether payments need to be automatically collected for the customer. Possible values are:

      - `on`: When an invoice is created, an automatic attempt to charge the customer's payment method is made.
      - `off`: Automatic collection of charges will not be made.

  - name: "backup_payment_source_id"
    type: "string"
    description: ""
    
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
    foreign-key-id: "payment-source-id"

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

  - name: "vat_number"
    type: "string"
    description: "The VAT number for the customer."

  - name: "vat_number_status"
    type: "string"
    description: ""
    
  - name: "vat_number_validated_time"
    type: "date-time"
    description: ""  

  - name: "entity_code"
    type: "string"
    description: ""
    
  - name: "exempt_number"
    type: "string"
    description: ""  

  - name: "created_from_ip"
    type: "string"
    description: ""  

  - name: "is_location_valid"
    type: "boolean"
    description: ""  

  - name: "custom_fields"
    type: "string"
    description: ""
    
  - name: "customer_type"
    type: "string"
    description: ""

  - name: "exemption_details"
    type: "string"
    description: ""

  - name: "fraud_flag"
    type: "string"
    description: ""

  - name: "meta_data"
    type: "string"
    description: ""
    
  - name: "registered_for_gst"
    type: "boolean"
    description: ""    
---