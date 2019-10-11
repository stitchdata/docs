---
tap: "chargebee"
version: "1.0"
key: "invoice"

name: "invoices"
doc-link: "https://apidocs.chargebee.com/docs/api/invoices"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about the invoices in your {{ integration.display_name }} account. Invoices are statements containing charges, adjustments, and any discounts for a subscription specific to a term.

replication-method: "Key-based Incremental"

api-method:
    name: "List invoices"
    doc-link: "https://apidocs.chargebee.com/docs/api/invoices#list_invoices"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
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
---