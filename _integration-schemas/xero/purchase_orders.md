---
tap: "xero"
version: "1.0"

name: "purchase_orders"
doc-link: &api-doc https://developer.xero.com/documentation/api/purchase-orders
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/purchase_orders.json
description: |
  The `purchase_orders` table contains info about your purchase orders. Purchase orders are requests sent to suppliers for specific goods and services.

replication-method: "Incremental"

api-method:
  name: getPurchaseOrders
  doc-link: *api-doc

attributes:
  - name: "PurchaseOrderID"
    type: "string"
    primary-key: true
    description: "The purchase order ID."

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the purchase order was last updated, in UTC."

  - name: "Date"
    type: "date-time"
    description: "The date the purchase order was issued."

  - name: "DeliveryDate"
    type: "date-time"
    description: "The date the goods are to be delivered."

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts of the line items in the purchase order. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive of tax
      - `NoTax` - Line items have no tax

  - name: "PurchaseOrderNumber"
    type: "string"
    description: "The unique alpha numeric code identifying the purchase order."

  - name: "Reference"
    type: "string"
    description: "An additional reference number for the purchase order."

  - name: "LineItems"
    type: "array"
    description: ""
    array-attributes:

  - name: "BrandingThemeID"
    type: "string"
    description: "The ID of the branding theme applied to the purchase order."
    foreign-key: true

  - name: "CurrencyCode"
    type: "string"
    description: "The currency that the purchase order has been raised in."
    foreign-key: true

  - name: "Status"
    type: "string"
    description: |
      The status of the purchase order. Possible values are:

      - `DRAFT`
      - `SUBMITTED`
      - `AUTHORISED`
      - `BILLED`
      - `DELETED`

  - name: "SentToContact"
    type: "boolean"
    description: "If `true`, the purchase order has been marked as 'sent'."

  - name: "DeliveryAddress"
    type: "string"
    description: "The address the goods are to be delivered to."

  - name: "AttentionTo"
    type: "string"
    description: "The person that the delivery is going to."

  - name: "Telephone"
    type: "string"
    description: "The phone number for the person accepting the delivery."

  - name: "DeliveryInstructions"
    type: "string"
    description: "The delivery instructions, if any."

  - name: "ExpectedArrivalDate"
    type: "date-time"
    description: "The date the goods are expected to arrive."

  - name: "CurrencyRate"
    type: "number"
    description: "The currency rate for a multicurrency purchase order."

  - name: "SubTotal"
    type: "number"
    description: "The total of the purchase order, excluding taxes."

  - name: "TotalTax"
    type: "number"
    description: "The total tax on the purchase order."

  - name: "Total"
    type: "number"
    description: "The total amount of the purchase order, calculated as `SubTotal + TotalTax`."

  - name: "TotalDiscount"
    type: "number"
    description: "The total of discounts applied on the purchase order line items."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the purchase order has an attachment."

  - name: "DeliveryDateString"
    type: "date-time"
    description: ""

  - name: "Type"
    type: "string"
    description: ""

  - name: "DateString"
    type: "date-time"
    description: ""

  - name: "HasErrors"
    type: "boolean"
    description: ""

  - name: "IsDiscounted"
    type: "boolean"
    description: ""

  - name: "ExpectedArrivalDateString"
    type: "date-time"
    description: ""

---