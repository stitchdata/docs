---
tap: "xero"
version: "1.0"

name: "receipts"
doc-link: &api-doc https://developer.xero.com/documentation/api/receipts
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/receipts.json
description: |
  The `receipts` table contains info about invoice receipts, which are receipts sent to customers after an invoice has been received.

replication-method: "Incremental"

api-method:
  name: getReceipts
  doc-link: *api-doc

attributes:
  - name: "ReceiptID"
    type: "string"
    primary-key: true
    description: "The receipt ID."

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the receipt was last updated, in UTC."

  - name: "Date"
    type: "date-time"
    description: "The date of the receipt."

  - name: "Contact"
    type: 
    description: ""

  - name: "LineItems"
    type: "array"
    description: ""

  - name: "User"
    type: 
    description: ""

  - name: "Reference"
    type: "string"
    description: "An additional reference number for the receipt."

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts of the line items in the receipt. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive of tax
      - `NoTax` - Line items have no tax

  - name: "SubTotal"
    type: "number"
    description: "The subtotal of the receipt."

  - name: "TotalTax"
    type: "number"
    description: "The total tax on the receipt."

  - name: "Total"
    type: "number"
    description: "The total amount of the receipt, calculated as `SubTotal + TotalTax`."

  - name: "Status"
    type: "string"
    description: |
      The status of the receipt. Possible values are:

      - `DRAFT`
      - `SUBMITTED` - Receipt has been submitted as part of an expense claim
      - `AUTHORISED`
      - `DECLINED`

  - name: "ReceiptNumber"
    type: "integer"
    description: "A Xero-generated sequence number for the receipt in a current claim for a given user."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the receipt has an attachment."

  - name: "Url"
    type: "string"
    description: "The URL link to a source document."

  - name: "ID"
    type: "string"
    description: ""

  - name: "ValidationErrors"
    type: 
    description: ""

  - name: "Attachments"
    type: 
    description: ""
---