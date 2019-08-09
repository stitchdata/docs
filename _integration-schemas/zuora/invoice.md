---
tap: "zuora"
version: 1.0 

name: "invoice"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Invoices
description: |
  The `{{ table.name }}` table contains info about invoices, which are bills to customers.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the invoice was last updated."

  - name: "accountId"
    type: "string"
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "adjustmentAccount"
    type: "double"
    description: "The amount of the invoice adjustments associated with the invoice."

  - name: "amount"
    type: "double"
    description: "The sum of all charges and taxes associated with the invoice."

  - name: "amountWithoutTax"
    type: "double"
    description: "The sum of all charges associated with the invoice, excluding taxes."

  - name: "autoPay"
    type: "boolean"
    description: "If `true`, invoices will be automatically picked up for processing in the corresponding payment run."

  - name: "balance"
    type: "double"
    description: "The remaining balance of the invoice after all payments, adjustments, and refunds are applied."

  - name: "billRunId"
    type: "string"
    description: "The ID of the bill run associated with the invoice."
    foreign-key-id: "billling-run-id"

  - name: "billToContactId"
    type: "string"
    description: "The ID of the person to bill for the invoice."
    foreign-key-id: "bill-to-contact-id"

  - name: "billToContactSnapshotId"
    type: "string"
    description: "The ID of the Bill To contact snapshot."
    foreign-key-id: "bill-to-contact-snapshot-id"

  - name: "comments"
    type: "string"
    description: "Additional info related to the invoice that a {{ integration.display_name }} user added to the invoice."

  - name: "createdById"
    type: "string"
    description: "The user ID of the person who created the invoice."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the invoice was generated."

  - name: "creditBalanceAdjustmentAmount"
    type: "double"
    description: "The currency amount of the adjustment applied to the customer's credit balance."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The ID of the default payment method for the account."
    foreign-key-id: "default-payment-method-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

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
    foreign-key-id: "invoice-number"

  - name: "lastEmailSentDate"
    type: "date-time"
    description: "The date when the invoice was last emailed."

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in {{ integration.display_name }}."
    foreign-key-id: "parent-account-id"

  - name: "paymentAmount"
    type: "double"
    description: "The amount of payments applied to the invoice."

  - name: "postedBy"
    type: "string"
    description: "The user ID of the person who moved the invoice to Posted status."

  - name: "postedDate"
    type: "date-time"
    description: "The date when the invoice was posted."

  - name: "refundAmount"
    type: "double"
    description: "The amount of a refund that was applied against an earlier payment on the invoice."

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key-id: "sold-to-contact-id"

  - name: "soldToContactSnapshotId"
    type: "string"
    description: "The ID of the Sold To contact snapshot."
    foreign-key-id: "sold-to-contact-snapshot-id"

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

  - name: "targetDate"
    type: "date-time"
    description: "The date used to determine which charged are to be billed."

  - name: "taxAmount"
    type: "double"
    description: "The total amount of the taxes applied to the invoice."

  - name: "taxExemptAmount"
    type: "double"
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
    description: "The ID of the {{ integration.display_name }} user who last updated the invoice."
---