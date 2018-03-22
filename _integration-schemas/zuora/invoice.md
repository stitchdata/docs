---
tap: "zuora"
version: 1.0 

name: "invoice"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Invoices
description: |
  The `invoice` table contains info about invoices, which are bills to customers.

  ### Custom Fields
  
  In addition to the attributes listed below, our Zuora integration will also replicate any custom fields.

replication-method: "Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice ID."
    ## foreign-keys:
    ##   - table-name: "invoiceItem"
    ##     attribute: "invoiceId"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the invoice was last updated."

  - name: "accountId"
    type: "string"
    description: "The account ID."
    ## foreign-keys:
    ##   - table-name: "account"
    ##     attribute: "id"

    ##   - table-name: "contact"
    ##     attribute: "accountId"

    ##   - table-name: "payment"
    ##     attribute: "accountId"

    ##   - table-name: "refund"
    ##     attribute: "accountId"

  - name: "adjustmentAccount"
    type: "decimal"
    description: "The amount of the invoice adjustments associated with the invoice."

  - name: "amount"
    type: "decimal"
    description: "The sum of all charges and taxes associated with the invoice."

  - name: "amountWithoutTax"
    type: "decimal"
    description: "The sum of all charges associated with the invoice, excluding taxes."

  - name: "autoPay"
    type: "boolean"
    description: "If `true`, invoices will be automatically picked up for processing in the corresponding payment run."

  - name: "balance"
    type: "decimal"
    description: "The remaining balance of the invoice after all payments, adjustments, and refunds are applied."

  - name: "billRunId"
    type: "string"
    description: "The ID of the bill run associated with the invoice."

  - name: "billToContactSnapshotId"
    type: "string"
    description: "The ID of the Bill To contact snapshot."

  - name: "comments"
    type: "string"
    description: "Additional info related to the invoice that a Zuora user added to the invoice."

  - name: "createdById"
    type: "string"
    description: "The user ID of the person who created the invoice."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the invoice was generated."

  - name: "creditBalanceAdjustmentAmount"
    type: "decimal"
    description: "The currency amount of the adjustment applied to the customer's credit balance."

  - name: "dueDate"
    type: "date-time"
    description: "The date by which the payment for the invoice is due."

  - name: "includesOneTime"
    type: "boolean"
    description: "If `true`, the invoice includes one-time charges."

  - name: "includesRecurring"
    type: "boolean"
    description: "If `true`, the invoice contains recurring charges."

  - name: "includesUsage"
    type: "boolean"
    description: "If `true`, the invoice contains usage charges."

  - name: "invoiceDate"
    type: "date-time"
    description: "The date on which to generate the invoice."

  - name: "invoiceNumber"
    type: "string"
    description: "The unique identification number for the invoice."

  - name: "lastEmailSentDate"
    type: "date-time"
    description: "The date when the invoice was last emailed."

  - name: "paymentAmount"
    type: "decimal"
    description: "The amount of payments applied to the invoice."

  - name: "postedBy"
    type: "string"
    description: "The user ID of the person who moved the invoice to Posted status."

  - name: "postedDate"
    type: "date-time"
    description: "The date when the invoice was posted."

  - name: "refundAmount"
    type: "decimal"
    description: "The amount of a refund that was applied against an earlier payment on the invoice."

  - name: "source"
    type: "string"
    description: "The source of the invoice."

  - name: "sourceId"
    type: "string"
    description: "The ID of the value in the `source` field."

  - name: "status"
    type: "string"
    description: |
      The status of the invoice in the system. This is not the status of the invoice payment, but the invoice itself.

      Possible values are:

      - `Draft`
      - `Posted`
      - `Canceled`

  - name: "soldToContactSnapshotId"
    type: "string"
    description: "The ID of the Sold To contact snapshot."

  - name: "targetDate"
    type: "date-time"
    description: "The date used to determine which charged are to be billed."

  - name: "taxAmount"
    type: "decimal"
    description: "The total amount of the taxes applied to the invoice."

  - name: "taxExemptAmount"
    type: "decimal"
    description: "The total amount of the invoice that is tax exempt."

  - name: "transferredToAccounting"
    type: "string"
    description: |
      Indicates if the invoice was transferred to an external accounting system, such as NetSuite. Possible values are:

      - `Processing`
      - `Yes`
      - `Error`
      - `Ignore`

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the invoice."
---