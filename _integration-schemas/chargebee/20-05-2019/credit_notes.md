---
tap: "chargebee"
version: "20-05-2019"
key: "credit-note"

name: "credit_notes"
doc-link: "https://apidocs.chargebee.com/docs/api/credit_notes"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/credit_notes.json"
description: |
  The `{{ table.name }}` table contains info about the credit notes in your {{ integration.display_name }} account. A credit note is a document that specifies the money owed by a business to a customer.

replication-method: "Key-based Incremental"

api-method:
    name: "List credit notes"
    doc-link: "https://apidocs.chargebee.com/docs/api/credit_notes#list_credit_notes"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The credit note ID."
    foreign-key-id: "credit-note-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the credit note was last updated."

  - name: "allocations"
    type: "array"
    description: "Details about invoice allocations made from the credit note."
    subattributes:
      - name: "allocated_amount"
        type: "integer"
        description: "The amount of the allocation, in cents."

      - name: "allocated_at"
        type: "date-time"
        description: "The time the allocation occurred."

      - name: "invoice_date"
        type: "date-time"
        description: "The closing date of the invoice."

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

  - name: "amount_allocated"
    type: "integer"
    description: "The amount allocated to invoices."

  - name: "amount_available"
    type: "integer"
    description: "The yet to be used credits of this credit note."

  - name: "amount_refunded"
    type: "integer"
    description: "The refunds issued from this credit note."

  - name: "currency_code"
    type: "string"
    description: "The currency code (ISO 4217 format) for the credit note."

  - name: "customer_id"
    type: "string"
    description: "The ID of the customer associated with the credit note."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date the credit note was issued."

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the credit note was deleted or not."

  - name: "discounts"
    type: "array"
    description: "Details about the discounts applied to the credit note."
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

  - name: "line_item_discounts"
    type: "array"
    description: "The list of discount(s) applied for each line item of the invoice."
    subattributes:
      - name: "coupon_id"
        type: "string"
        description: "The coupon ID."
        foreign-key-id: "coupon-id"

      - name: "discount_amount"
        type: "integer"
        description: "The discount amount, in cents."

      - name: "discount_type"
        type: "string"
        description: *discount-line-item

      - name: "line_item_id"
        type: "string"
        description: "The ID of the line item for which the discount is applicable."
        foreign-key-id: "line-item-id"

  - name: "line_item_taxes"
    type: "array"
    description: "The list of taxes applied on line items."
    subattributes:
      - name: "is_non_compliance_tax"
        type: "boolean"
        description: "Indicates the non-compliance tax should not be reported to the tax jurisdiction."

      - name: "is_partial_tax_applied"
        type: "boolean"
        description: "Indicates whether tax is applied only on a portion of the line item or not."

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

      - name: "taxable_amount"
        type: "integer"
        description: "The actual portion of the line item that is taxable, in cents."

  - name: "line_item_tiers"
    type: "array"
    description: "The list of tiers applicable for the line item."
    subattributes:
      - name: "ending_unit"
        type: "integer"
        description: "The upper limit of a range of units for the tier."

      - name: "line_item_id"
        type: "string"
        description: "The line item ID."
        foreign-key-id: "line-item-id"

      - name: "quantity_used"
        type: "integer"
        description: "The number of units purchased in a range."

      - name: "starting_unit"
        type: "integer"
        description: "The lower limit of a range of units for the tier."

      - name: "unit_amount"
        type: "integer"
        description: "The price of the tier if the charge model is `stairstep`, or the price of each unit in the tier if the charge model is `tiered` or `volume`."

  - name: "line_items"
    type: "array"
    description: "The line items in the credit note."
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

  - name: "linked_refunds"
    type: "array"
    description: "Details about refunds issued from the credit note."
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

  - name: "price_type"
    type: "string"
    description: |
      The price type of the credit note. Possible values are:

      - `tax_exclusive`
      - `tax_inclusive`

  - name: "reason_code"
    type: "string"
    description: |
      The reason for issuing the credit note. Possible values include:

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

  - name: "reference_invoice_id"
    type: "string"
    description: "The ID of the invoice against which the credit note is issued."
    foreign-key-id: "invoice-id"

  - name: "refunded_at"
    type: "date-time"
    description: "The time when the credit note was fully used."

  - name: "resource_version"
    type: "integer"
    description: "The version number of the credit note. Each update of the credit note results in an incremental change of this value. **Note**: This attribute will be present only if the credit note has been updated after 2016-09-28."

  - name: "round_off_amount"
    type: "integer"
    description: "The credit note rounded-off amount, in cents."

  - name: "status"
    type: "string"
    description: |
      The status of the credit note. Possible values include:

      - `adjusted`
      - `refunded`
      - `refund_due`
      - `voided`

  - name: "sub_total"
    type: "integer"
    description: "The credit note subtotal, in cents."

  - name: "subscription_id"
    type: "string"
    description: "The ID of the subscription associated with the credit note."
    foreign-key-id: "subscription-id"

  - name: "taxes"
    type: "array"
    description: "The tax lines of the credit note."
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

  - name: "total"
    type: "integer"
    description: "The total credit amount in cents."

  - name: "type"
    type: "string"
    description: |
      The credit note type. Possible values are:

      - `adjustment`
      - `refundable`

  - name: "vat_number"
    type: "string"
    description: "The VAT number of the customer for whom the credit note is raised."

  - name: "voided_at"
    type: "date-time"
    description: "The time when the credit note was voided."
---