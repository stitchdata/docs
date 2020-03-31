---
tap: "chargebee"
version: "1"
key: "orders"

name: "orders"
doc-link: "https://apidocs.chargebee.com/docs/api/orders"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/orders.json"
description: "The `{{ table.name }}` table contains info about the orders in your {{ integration.display_name }} account. The **Order Management** feature must be enabled to sync this table. For more information, refer to the [{{ integration.display_name }} docs](https://www.chargebee.com/docs/orders.html)."

replication-method: "Key-based Incremental"

api-method:
    name: "List orders"
    doc-link: "https://apidocs.chargebee.com/docs/api/orders#list_orders"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The order ID."
    foreign-key-id: "order-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the order was last updated."
    replication-key: true

  - name: "amount_adjusted"
    type: "integer"
    description: "The amount the order was adjusted."

  - name: "amount_paid"
    type: "integer"
    description: "The total amount paid for the order."

  - name: "batch_id"
    type: "string"
    description: "The unique ID to identify a group of orders."

  - name: "billing_address"
    type: "object"
    description: "The billing address of the order."
    subattributes:
      - name: "city"
        type: "string"
        description: "The city."
      - name: "company"
        type: "string"
        description: "The company name."
      - name: "country"
        type: "string"
        description: "The country."
      - name: "email"
        type: "string"
        description: "The email of the billed client."
      - name: "first_name"
        type: "string"
        description: "The first name of the billed client."
      - name: "last_name"
        type: "string"
        description: "The last name of the billed client."
      - name: "line1"
        type: "string"
        description: "The first line of the address."
      - name: "line2"
        type: "string"
        description: "The second line of the address"
      - name: "line3"
        type: "string"
        description: "The third line of the address."
      - name: "object"
        type: "string"
        description: ""
      - name: "phone"
        type: "string"
        description: "The phone number of the billed client."
      - name: "state"
        type: "string"
        description: "The state."
      - name: "state_code"
        type: "string"
        description: "The state code."
      - name: "validation_status"
        type: "string"
        description: "The address verification status."
      - name: "zip"
        type: "string"
        description: "The zip code."

  - name: "cancellation_reason"
    type: "string"
    description: "The reason for the order cancellation."

  - name: "cancelled_at"
    type: "date-time"
    description: "The date the order was cancelled."

  - name: "created_at"
    type: "date-time"
    description: "The date the order was created."

  - name: "created_by"
    type: "string"
    description: "The source or user that created the order."

  - name: "currency_code"
    type: "string"
    description: "The currency code of the invoice."

  - name: "customer_id"
    type: "string"
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "deleted"
    type: "boolean"
    description: "Indication of wheteher or not the resource has been deleted."

  - name: "delivered_at"
    type: "date-time"
    description: "The date the order was delivered."

  - name: "discount"
    type: "integer"
    description: "The total discount on the order."

  - name: "document_number"
    type: "string"
    description: "The serial number of the order."

  - name: "fulfillment_status"
    type: "string"
    description: |
      The fulfillment status of the order. Typical values are:
      - `Shipped`
      - `Awaiting Shipment`
      - `Not fulfilled`

  - name: "gift_id"
    type: "string"
    description: "The gift ID if the order is a gift."
    foreign-key-id: "gift-id"

  - name: "gift_note"
    type: "string"
    description: "The gift message added during the purchase."

  - name: "invoice_id"
    type: "string"
    description: "The invoice number."
    foreign-key-id: "invoice-id"

  - name: "invoice_round_off_amount"
    type: "integer"
    description: "The total round off taken from the invoice level."

  - name: "is_gifted"
    type: "boolean"
    description: "Indication of whether this order is a gift or not."

  - name: "line_item_discounts"
    type: "array"
    description: "The list of discounts applied to the order."
    subattributes:
      - name: "coupon_id"
        type: "string"
        description: "The coupon ID."
        foreign-key-id: "coupon-id"
      - name: "discount_amount"
        type: "integer"
        description: "The discount amount."
      - name: "discount_type"
        type: "string"
        description: "The type of discount."
      - name: "line_item_id"
        type: "string"
        description: "The reference ID of the item that the discount is applied to."
        foreign-key-id: "line-item-id"

  - name: "line_item_taxes"
    type: "array"
    description: "The list of taxes applied on the order's line items."
    subattributes:
      - name: "is_non_compliance_tax"
        type: "boolean"
        description: "Indicates the non-compliance tax that should not be reported to the jurisdiction."
      - name: "is_partial_tax_applied"
        type: "boolean"
        description: "Indicates whether or not tax is applied on a portion of the line item amount."
      - name: "line_item_id"
        type: "string"
        description: "The reference ID of the item where tax is applicable."
      - name: "tax_amount"
        type: "integer"
        description: "The tax amount."
      - name: "tax_juris_code"
        type: "string"
        description: "The tax jurisdiction code."
      - name: "tax_juris_name"
        type: "string"
        description: "The tax jurisdiction name."
      - name: "tax_juris_type"
        type: "string"
        description: "The type of tax jurisdiction."
      - name: "tax_name"
        type: "string"
        description: "The name of the tax applied."
      - name: "tax_rate"
        type: "integer"
        description: "The tax rate."
      - name: "taxable_amount"
        type: "integer"
        description: "The actual portion of the line item amount that is taxable."

  - name: "linked_credit_notes"
    type: "array"
    description: "The credit notes linked to the order."
    subattributes:
      - name: "amount"
        type: "integer"
        description: "The order amount."
      - name: "amount_adjusted"
        type: "integer"
        description: "The total amount adjusted on the order."
      - name: "amount_refunded"
        type: "integer"
        description: "The total refundable credits issued on the order."
      - name: "id"
        type: "string"
        description: "The credit note ID."
        foreign-key-id: "credit-note-id"
      - name: "status"
        type: "string"
        description: "The credit note status."
      - name: "type"
        type: "string"
        description: |
          The credit note type. Possible values are:
          - `adjustment`
          - `refundable`

  - name: "note"
    type: "string"
    description: "The custom note for the order."

  - name: "order_date"
    type: "date-time"
    description: "The date that the order will be processed."

  - name: "order_line_items"
    type: "array"
    description: "The list of line items in the order."
    subattributes:
      - name: "amount"
        type: "integer"
        description: "The subtotal of the order line item."
      - name: "amount_adjusted"
        type: "integer"
        description: "The total amount adjusted on the invoice."
      - name: "amount_paid"
        type: "integer"
        description: "The total amount paid on the invoice."
      - name: "description"
        type: "string"
        description: "The line item description."
      - name: "discount_amount"
        type: "integer"
        description: "The discount given on the order line item."
      - name: "entity_id"
        type: "string"
        description: "The identifier of the modelled entity this line item is based on."
      - name: "entity_type"
        type: "string"
        description: |
          The specified modelled entity this line item is based on. Possible values are:
          - `plan_setup`
          - `plan`
          - `addon`
          - `adhoc`
      - name: "fulfillment_amount"
        type: "integer"
        description: "The amount that is going to get fulfilled for this order."
      - name: "fulfillment_quantity"
        type: "integer"
        description: "The quantity that is going to get fulfilled for this order."
      - name: "id"
        type: "string"
        description: "The order line item ID."
      - name: "invoice_id"
        type: "string"
        description: "The invoice of the line item."
      - name: "invoice_line_item_id"
        type: "string"
        description: "The invoice line item ID associated with this order line item."
      - name: "is_shippable"
        type: "boolean"
        description: "Specifies whether or not the charge is applicable for shipping."
      - name: "item_level_discount_amount"
        type: "integer"
        description: "The item level discount amount."
      - name: "refundable_credits"
        type: "integer"
        description: "The total amount of refundable credits."
      - name: "refundable_credits_issued"
        type: "integer"
        description: "The total refundable credits issued on the invoice."
      - name: "sku"
        type: "string"
        description: "The SKU for the delivery."
      - name: "status"
        type: "string"
        description: |
          The status of the order. Possible values are
            - `queued`
            - `awaiting_shipment`
            - `on_hold`
            - `delivered`
            - `shipped`
            - `partially_delivered`
            - `returned`
            - `cancelled`
      - name: "tax_amount"
        type: "integer"
        description: "The total amount of tax applied on the line item."
      - name: "unit_price"
        type: "integer"
        description: "The unit price."

  - name: "order_type"
    type: "string"
    description: |
      The order type. Possible values are:
      - `manual`
      - `system_generated`

  - name: "paid_on"
    type: "date-time"
    description: "The date the invoice was paid."

  - name: "payment_status"
    type: "string"
    description: |
      The payment status of the order. Possible values are:
      - `not_paid`
      - `paid`

  - name: "price_type"
    type: "string"
    description: |
      The price type of the order. Possible values are:
      - `tax_exclusive`
      - `tax_inclusive`

  - name: "reference_id"
    type: "string"
    description: "The reference ID."

  - name: "refundable_credits"
    type: "integer"
    description: "The total amount that can be issued as credits for the order."

  - name: "refundable_credits_issued"
    type: "integer"
    description: "The total amount issued as credits on behalf of the order."

  - name: "resource_version"
    type: "integer"
    description: "The version number of the resource."

  - name: "rounding_adjustement"
    type: "integer"
    description: "Rounding adjustment."

  - name: "shipment_carrier"
    type: "string"
    description: "The shipment carrier."

  - name: "shipped_at"
    type: "date-time"
    description: "The date the order was shipped."

  - name: "shipping_address"
    type: "object"
    description: "The shipping address for the order."
    subattributes:
      - name: "city"
        type: "string"
        description: "The city."
      - name: "company"
        type: "string"
        description: "The name of the company."
      - name: "country"
        type: "string"
        description: "The country."
      - name: "email"
        type: "string"
        description: "The email of the shipment recipient."
      - name: "first_name"
        type: "string"
        description: "The first name of the recipient."
      - name: "last_name"
        type: "string"
        description: "The last name of the recipient."
      - name: "line1"
        type: "string"
        description: "Line 1 of the address."
      - name: "line2"
        type: "string"
        description: "Line 2 of the address."
      - name: "line3"
        type: "string"
        description: "Line 3 of the address."
      - name: "phone"
        type: "string"
        description: "The phone numger of the recipient."
      - name: "state"
        type: "string"
        description: "The state."
      - name: "state_code"
        type: "string"
        description: "The state code."
      - name: "validation_status,"
        type: "string"
        description: |
          The address verification status. Possible values are:
          - `not_validated`
          - `valid`
          - `partially_valid`
          - `invalid`
      - name: "zip"
        type: "string"
        description: "The zip code."

  - name: "shipping_cut_off_date"
    type: "date-time"
    description: "The time after an order becomes unservicable."

  - name: "shipping_date"
    type: "date-time"
    description: "The date the order will be delivered."

  - name: "status"
    type: "string"
    description: |
      The status of the order. Possible values are:
      - `new`
      - `processing`
      - `complete`
      - `cancelled`

  - name: "status_update_at"
    type: "date-time"
    description: "The time the order was last updated."

  - name: "sub_total"
    type: "integer"
    description: "The order's subtotal."

  - name: "subscription_id"
    type: "string"
    description: "The subscription ID linked to the order."
    foreign-key-id: "subscription-id"

  - name: "tax"
    type: "integer"
    description: "The total tax for the order."

  - name: "total"
    type: "integer"
    description: "The amount charged for the order."

  - name: "tracking_id"
    type: "string"
    description: "The tracking ID of the order."
---
