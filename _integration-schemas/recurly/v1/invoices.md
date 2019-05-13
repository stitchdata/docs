---
tap: "recurly"
version: "1.0"

name: "invoices"
key: "invoice"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about the invoices for a {{ integration.display_name }} site. An invoice relates charges, credits, and payments together. When a subscription is created or renewed or a charge is created on the account, {{ integration.display_name }} will sum the charges, discount or tax as appropriate, and send the invoice out for collection.

replication-method: "Key-based Incremental"
api-method:
    name: "List a site's invoices"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_invoices"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: &id "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the invoice was last updated."

  - name: "account"
    type: "object"
    anchor-id: 1
    description: "Details about the account associated with the invoice."
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

  - name: "address"
    type: "object"
    description: "Details about the address associated with the invoice."
    subattributes:
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

      - name: "name_on_account"
        type: "string"
        description: "The name on the account."

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

  - name: "balance"
    type: "number"
    description: "The outstanding balance remaining on this invoice."

  - name: "closed_at"
    type: "date-time"
    description: "The date the invoice was marked paid or failed."

  - name: "collection_method"
    type: "string"
    description: |
      The collection method for the invoice. Possible values are:

      - `automatic` - A corresponding transaction is run using the account's billing info at the same time the invoice is created.
      - `manual` - A corresponding transaction is not created, and the merchant must enter a manual payment transaction or have the customer pay with an automatic method.

  - name: "created_at"
    type: "date-time"
    description: "The date and time the invoice was created."

  - name: "credit_payments"
    type: "array"
    description: "Details about the credit payments associated with the invoice."
    subattributes:
      - name: "account"
        type: "object"
        anchor-id: 2
        description: "Details about the account associated with the credit payment."
        subattributes: &mini-account
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

      - name: "action"
        type: "string"
        description: |
          The action for which the credit was created. Possible values are:

          - `payment`
          - `refund`
          - `reduction`
          - `write_off`

      - name: "amount"
        type: "number"
        description: "The total credit payment applied to the charge invoice."

      - name: "applied_to_invoice"
        type: "object"
        description: "Details about the invoice the credit payment was applied to."
        subattributes: &mini-invoice
          - name: "id"
            type: "string"
            description: *id
            foreign-key-id: "invoice-id"

          - name: "number"
            type: "string"
            description: &number "The invoice number."

          - name: "object"
            type: "string"
            description: &object "This will be `invoice`."

          - name: "state"
            type: "string"
            description: &state |
              The state of the invoice. Possible values are:

              - `pending`
              - `processing`
              - `past_due`
              - `paid`
              - `failed`

          - name: "type"
            type: "string"
            description: &type |
              The type of the invoice. Possible values are:

              - `charge`
              - `credit`
              - `legacy`

      - name: "created_at"
        type: "date-time"
        description: "The date and time the credit payment was created."

      - name: "currency"
        type: "string"
        description: &currency "The three-letter ISO 4217 currency code."

      - name: "id"
        type: "string"
        description: "The credit payment ID."

      - name: "object"
        type: "string"
        description: ""

      - name: "original_credit_payment_id"
        type: "string"
        description: "For credit payments with `action: refund`, this is the credit payment that was refunded."

      - name: "original_invoice"
        type: "object"
        description: "Details about the original invoice associated with the credit payment."
        subattributes: *mini-invoice

      - name: "refund_transaction"
        type: "object"
        description: "Details about the refund transaction the credit payment is associated with."
        subattributes:
          - name: "amount"
            type: "number"
            description: &amount "The amount of the transaction."

          - name: "account"
            type: "object"
            anchor-id: 3
            description: "Details about the account associated with the refund transaction."
            subattributes: *mini-account

          - name: "avs_check"
            type: "string"
            description: &avs-check "The result from checking the overall AVS on the processed transaction."

          - name: "billing_address"
            type: "object"
            description: "The billing address detail for the account."
            anchor-id: 1
            subattributes: &billing-address
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

              - name: "name_on_account"
                type: "string"
                description: "The name on the account."

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

          - name: "collected_at"
            type: "date-time"
            description: &collected-at "If collected, the date and time the transaction was collected. Otherwise, the time the transaction was created."

          - name: "collection_method"
            type: "string"
            description: &collection-method |
              The method by which payment for the transaction was collected. Possible values are:

              - `automatic`
              - `manual`

          - name: "created_at"
            type: "date-time"
            description: &created-at "The date and time the transaction was created."

          - name: "currency"
            type: "string"
            description: *currency

          - name: "customer_message"
            type: "string"
            description: &customer_message "For declined transactions, the message displayed to the customer."

          - name: "customer_message_locale"
            type: "string"
            description: &customer_message_locale "The language code used to display the `customer_message`."

          - name: "cvv_check"
            type: "string"
            description: &cvv_check "When processed, the result from checking the CVV/CVC value on the transaction."

          - name: "gateway_approval_code"
            type: "string"
            description: &gateway_approval_code "The transaction approval code from the payment gateway."

          - name: "gateway_message"
            type: "string"
            description: &gateway_message "The transaction message from the payment gateway."

          - name: "gateway_reference"
            type: "string"
            description: &gateway_reference "The transaction reference number from the payment gateway."

          - name: "gateway_response_code"
            type: "string"
            description: &gateway_response_code "The gateway error code for declined transactions (`success: false`)."

          - name: "gateway_response_time"
            type: "number"
            description: &gateway_response_time "The time, in seconds, for the gateway to process the transaction."

          - name: "gateway_response_values"
            type: "object"
            description: &gateway_response_values "The response values from the payment gateway."

          - name: "id"
            type: "string"
            description: &transaction-id "The transaction ID."
            foreign-key-id: "transaction-id"

          - name: "invoice"
            type: "object"
            description: &invoice-details "Details about the invoice associated with the transaction."
            anchor-id: 1
            subattributes: *mini-invoice

          - name: "ip_address_country"
            type: "string"
            description: &ip_address_country "The country, based on `ip_address_v4`."

          - name: "ip_address_v4"
            type: "string"
            description: &ip_address_v4 |
              The IP address provided when the billing information was collected:

              - When a customer entered billing info into Recurly.JS or a hosted payment page.
              - When the merchant enters billing info using the API.

          - name: "object"
            type: "string"
            description: ""

          - name: "origin"
            type: "string"
            description: &origin |
              The origin of the transaction. Possible values are:

              - `api`
              - `hpp`
              - `merchant`
              - `recurly_admin`
              - `recurlyjs`
              - `recurring`
              - `transparent`
              - `force_collect`
              - `refunded_externally`
              - `chargeback`

          - name: "original_transaction_id"
            type: "string"
            description: &original_transaction_id "If the transaction is a refund, this will be the ID of the original transaction."
            foreign-key-id: "transaction-id"

          - name: "payment_gateway"
            type: "object"
            description: &payment_gateway_desc "Details about the payment gateway used to process the transaction."
            anchor-id: 1
            subattributes: &payment_gateway
              - name: "id"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

              - name: "object"
                type: "string"
                description: ""

              - name: "type"
                type: "string"
                description: ""

          - name: "payment_method"
            type: "object"
            description: &payment_method_desc "The payment method used in the transaction."
            anchor-id: 1
            subattributes: &payment_method
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

          - name: "refunded"
            type: "boolean"
            description: &refunded "Indicates if part or all of the transaction was refunded."

          - name: "status"
            type: "string"
            description: &status |
              The current transaction status. Possible values are:

              - `pending`
              - `scheduled`
              - `processing`
              - `success`
              - `void`
              - `declined`
              - `error`
              - `chargeback`

          - name: "status_code"
            type: "string"
            description: ""

          - name: "status_message"
            type: "string"
            description: &status_message "For declined transactions (`success: false`), the message displayed to the merchant."

          - name: "subscription_ids"
            type: "array"
            anchor-id: 1
            description: &subscription_ids_desc "If the transaction refunds one or more subscriptions, this will be a list of the subscription IDs that were refunded."
            subattributes: &subscription_ids
              - name: "value"
                type: "string"
                description: "The subscription ID."
                foreign-key-id: "subscription-id"

          - name: "success"
            type: "boolean"
            description: &success "Indicates if the transaction completed successfully."

          - name: "type"
            type: "string"
            description: &type |
              The type of the transaction. Possible values include:

              - `authorization` – Verifies billing information and places a hold on money in the customer's account.
              - `capture` – Captures funds held by an authorization and completes a purchase.
              - `purchase` – Combines the authorization and capture in one transaction.
              - `refund` – Returns all or a portion of the money collected in a previous transaction to the customer.
              - `verify` – A $0 or $1 transaction used to verify billing information which is immediately voided.

          - name: "uuid"
            type: "string"
            description: &uuid "The UUID is useful for matching data with the CSV exports and building URLs into {{ integration.display_name }}'s UI."

          - name: "voided_at"
            type: "date-time"
            description: &voided_at "The date and time the transaction was voided."

          - name: "voided_by_invoice"
            type: "object"
            anchor-id: 1
            description: &voided_by_invoice "Details about the invoice that voided the transaction."
            subattributes: *mini-invoice

      - name: "updated_at"
        type: "date-time"
        description: "The date and time the credit payment was last updated."

      - name: "uuid"
        type: "string"
        description: *uuid

      - name: "voided_at"
        type: "date-time"
        description: "The date and time the credit payment was voided."

  - name: "currency"
    type: "string"
    description: *currency

  - name: "customer_notes"
    type: "string"
    description: "The customer notes text specified in Invoice Settings."

  - name: "discount"
    type: "number"
    description: "The total amount of discounts applied on the invoice."

  - name: "due_at"
    type: "date-time"
    description: "The date and time the invoice is due."

  - name: "line_items"
    type: "object"
    description: &line-items "Details about the line items in the invoice."
    subattributes:
      - name: "data"
        type: "array"
        description: *line-items
        subattributes:
          - name: "accounting_code"
            type: "string"
            description: "The internal accounting code for the line item."

          - name: "account"
            type: "object"
            anchor-id: 4
            description: "Details about the account associated with the line item."
            subattributes: *account

          - name: "add_on_code"
            type: "string"
            description: "If the line item is a charge or credit for an add-on, this is its code."

          - name: "add_on_id"
            type: "string"
            description: "If the line item is a charge or credit for an add-on this is its ID."
            foreign-key-id: "plan-add-on-id"

          - name: "amount"
            type: "number"
            description: "The total amount of the line item, calculated as `(quantity * unit_amount) - (discount + tax)`."

          - name: "created_at"
            type: "date-time"
            description: "The date and time the line item was created."

          - name: "credit_applied"
            type: "number"
            description: "The amount of credit from this line item that was applied to the invoice."

          - name: "credit_reason_code"
            type: "string"
            description: |
              When `type: credit`, this will be the reason the credit was given. Possible values include:

              - `general`
              - `service`
              - `promotional`
              - `refund`
              - `gift_card`
              - `write_off`

          - name: "currency"
            type: "string"
            description: *currency

          - name: "description"
            type: "string"
            description: "The description of the line item."

          - name: "discount"
            type: "number"
            description: "The discount applied to the line item."

          - name: "end_date"
            type: "date-time"
            description: "If this date is provided, it indicates the end of a time range."

          - name: "id"
            type: "string"
            description: "The line item ID."

          - name: "invoice_id"
            type: "string"
            description: "Once the line item has been invoiced this will be the invoice's ID."
            foreign-key-id: "invoice-id"

          - name: "invoice_number"
            type: "string"
            description: "Once the line item has been invoiced this will be the invoice's number. If VAT taxation and the Country Invoice Sequencing feature are enabled, invoices will have country-specific invoice numbers for invoices billed to EU countries (ex: FR1001). Non-EU invoices will continue to use the site-level invoice number sequence."

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
              The origin of the invoice to return. Possible values are:

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
            description: "If the line item is a charge or credit for a plan or add-on, this is the plan's code."

          - name: "plan_id"
            type: "string"
            description: "If the line item is a charge or credit for a plan or add-on, this is the plan's ID."
            foreign-key-id: "plan-id"

          - name: "previous_line_item_id"
            type: "string"
            description: "This field will only have a value if the line item is a credit created from a previous credit, or if the credit was created from a charge refund."

          - name: "product_code"
            type: "string"
            description: "For plan related line items this will be the plan's code, for add-on related line items it will be the add-on's code."

          - name: "proration_rate"
            type: "number"
            description: |
              When a line item has been prorated, this is the rate of the proration. Proration rates were made available for line items created after March 30, 2017. For line items created prior to that date, the proration rate will be `null`, even if the line item was prorated.

          - name: "quantity"
            type: "number"
            description: "This number will be multiplied by the unit amount to compute the subtotal before any discounts or taxes."

          - name: "refund"
            type: "boolean"
            description: "Indicates if the line item has been refunded."

          - name: "refunded_quantity"
            type: "number"
            description: "For refund charges, the quantity being refunded. For non-refund charges, the total quantity refunded (possibly over multiple refunds)."

          - name: "shipping_addresses"
            type: "array"
            description: "The shipping address info for the line item."
            subattributes: &shipping-addresses
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
            description: "If an end date is present, this is value indicates the beginning of a billing time range. If no end date is present it indicates billing for a specific date."

          - name: "state"
            type: "string"
            description: |
              The state of the line item. Possible values are:

              - `pending` - Pending line items are charges or credits on an account that have not been applied to an invoice yet.
              - `invoiced` - Invoiced line items will always have an `invoice_id` value.

          - name: "subscription_id"
            type: "string"
            description: "The subscription ID associated with the line item."
            foreign-key-id: "subscription-id"

          - name: "subtotal"
            type: "number"
            description: "The subtotal for the line item, calculated as `quantity * unit_amount`."

          - name: "tax"
            type: "number"
            description: "The tax amount for the line item."

          - name: "tax_code"
            type: "string"
            description: |
              Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system. If you are using Recurly’s EU VAT feature:

              - `P0000000` - Indicates physical
              - `D0000000` - Indicates digital
              - Empty string - Indicates unknown

          - name: "tax_exempt"
            type: "boolean"
            description: "Indicates if the line item is tax exempt."

          - name: "tax_info"
            type: "object"
            description: "Details about the tax applied to the line item."
            subattributes: &tax-info
              - name: "rate"
                type: "number"
                description: "The tax rate."

              - name: "region"
                type: "string"
                description: "Provides the tax region applied on an invoice. For U.S. Sales Tax, this will be the two-letter state code. For EU VAT this will be the two-letter country code. For all country level tax types, this will display the regional tax, like VAT, GST, or PST."

              - name: "type"
                type: "string"
                description: "Provides the tax type as `vat` for EU VAT, `usst` for U.S. Sales Tax, or the two-letter country code for country level tax types like Canada, Australia, New Zealand, Israel, and all non-EU European countries."

          - name: "taxable"
            type: "boolean"
            description: "Indicates if the line item is taxable."

          - name: "type"
            type: "string"
            description: |
              The type of the line item. Possible values include:

              - `charge` - A positive line item that debits the account.
              - `credit` - A negative line item that credits the account.

          - name: "unit_amount"
            type: "number"
            description: "The unit amount. This value will be positive for a charge and negative for a credit."

          - name: "updated_at"
            type: "date-time"
            description: "The date and time the line item was last updated."

          - name: "uuid"
            type: "string"
            description: *uuid

      - name: "has_more"
        type: "boolean"
        description: ""

      - name: "next"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

  - name: "net_terms"
    type: "number"
    description: |
      An integer representing the number of days after an invoice's creation that the invoice will become past due. If set to `0`, the invoice is due on receipt and will become due 24 hours after its creation. If set to `30`, it will become past due at exactly 31 days.

  - name: "number"
    type: "string"
    description: "If VAT taxation and the Country Invoice Sequencing feature are enabled, invoices will have country-specific invoice numbers for invoices billed to EU countries (ex: FR1001). Non-EU invoices will continue to use the site-level invoice number sequence."

  - name: "object"
    type: "string"
    description: "This will be `invoice`."

  - name: "origin"
    type: "string"
    description: |
      The event that created the invoice. Possible values are:

      - `purchase`
      - `line_item_refund`
      - `open_amount_refund`
      - `renewal`
      - `immediate_change`
      - `termination`
      - `credit`
      - `gift_card`
      - `write_off`

  - name: "paid"
    type: "number"
    description: ""

  - name: "po_number"
    type: "string"
    description: "For manual invoicing, the PO number associated with the subscription."

  - name: "previous_invoice_id"
    type: "string"
    description: ""

  - name: "refundable_amount"
    type: "number"
    description: ""

  - name: "state"
    type: "string"
    description: *state

  - name: "subscription_ids"
    type: "array"
    description: "If the invoice is charging or refunding one or more subscriptions, this will be a list of the associated subscription IDs."
    subattributes:
      - name: "value"
        type: "string"
        description: "The subscription ID."
        foreign-key-id: "subscription-id"

  - name: "subtotal"
    type: "number"
    description: "The summation of charges, discounts, and credits, before tax."

  - name: "tax"
    type: "number"
    description: "The total tax on the invoice."

  - name: "tax_info"
    type: "object"
    description: "Details about the tax applied to the invoice."
    subattributes: *tax-info

  - name: "terms_and_conditions"
    type: "string"
    description: "This will default to the Terms and Conditions text specified on the Invoice Settings page in your {{ integration.display_name }} admin. This specifies custom notes to add or override Terms and Conditions."

  - name: "total"
    type: "number"
    description: "The final total on this invoice. The summation of invoice charges, discounts, credits, and tax."

  - name: "transactions"
    type: "array"
    description: "Details about the transactions associated with the invoice."
    subattributes:
      - name: "amount"
        type: "number"
        description: *transaction-amt

      - name: "avs_check"
        type: "string"
        description: *avs_check

      - name: "account"
        type: "object"
        anchor-id: 4
        description: "Details about the account associated with the transaction."
        subattributes: *account

      - name: "billing_address"
        type: "object"
        anchor-id: 2
        description: "The billing address associated with the transaction."
        subattributes: *billing-address

      - name: "collected_at"
        type: "date-time"
        description: *collected_at

      - name: "collection_method"
        type: "string"
        description: *collection_method

      - name: "created_at"
        type: "date-time"
        description: *created_at

      - name: "currency"
        type: "string"
        description: *currency

      - name: "customer_message"
        type: "string"
        description: *customer_message

      - name: "customer_message_locale"
        type: "string"
        description: *customer_message_locale

      - name: "cvv_check"
        type: "string"
        description: *cvv_check

      - name: "gateway_approval_code"
        type: "string"
        description: *gateway_approval_code

      - name: "gateway_message"
        type: "string"
        description: *gateway_message

      - name: "gateway_reference"
        type: "string"
        description: *gateway_reference

      - name: "gateway_response_code"
        type: "string"
        description: *gateway_response_code

      - name: "gateway_response_time"
        type: "number"
        description: *gateway_response_time

      - name: "gateway_response_values"
        type: "object"
        description: *gateway_response_values

      - name: "id"
        type: "string"
        description: "The transaction ID."
        foreign-key-id: "transaction-id"

      - name: "invoice"
        type: "object"
        anchor-id: 2
        description: "Details about the invoice associated with the transaction."
        subattributes: *mini-invoice

      - name: "ip_address_country"
        type: "string"
        description: *ip_address_country

      - name: "ip_address_v4"
        type: "string"
        description: *ip_address_v4

      - name: "object"
        type: "string"
        description: ""

      - name: "origin"
        type: "string"
        description: *origin

      - name: "original_transaction_id"
        type: "string"
        description: *original_transaction_id

      - name: "payment_gateway"
        type: "object"
        anchor-id: 2
        description: *payment_gateway_desc
        subattributes: *payment_gateway

      - name: "payment_method"
        type: "object"
        anchor-id: 2
        description: *payment_method_desc
        subattributes: *payment_method

      - name: "refunded"
        type: "boolean"
        description: *refunded

      - name: "status"
        type: "string"
        description: *status

      - name: "status_code"
        type: "string"
        description: ""

      - name: "status_message"
        type: "string"
        description: ""

      - name: "subscription_ids"
        type: "array"
        anchor-id: 2
        description: *subscription_ids_desc
        subattributes: *subscription_ids

      - name: "success"
        type: "boolean"
        description: *success

      - name: "type"
        type: "string"
        description: *type

      - name: "uuid"
        type: "string"
        description: *uuid

      - name: "voided_at"
        type: "date-time"
        description: *voided_at

      - name: "voided_by_invoice"
        type: "object"
        anchor-id: 2
        description: *voided_by_invoice
        subattributes: *mini-invoice

  - name: "type"
    type: "string"
    description: |
      The type of the invoice. Possible values are:

      - `charge`
      - `credit`
      - `legacy`

  - name: "vat_number"
    type: "string"
    description: "The VAT registration number for the customer on this invoice. This will come from the VAT Number field in the Billing Info or the Account Info depending on your tax settings and the invoice collection method."

  - name: "vat_reverse_charge_notes"
    type: "string"
    description: "VAT Reverse Charge Notes only appear if you have EU VAT enabled or are using your own Avalara AvaTax account and the customer is in the EU, has a VAT number, and is in a different country than your own. This will default to the VAT Reverse Charge Notes text specified on the Tax Settings page in your Recurly admin, unless custom notes were created with the original subscription."
---