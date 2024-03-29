---
tap: "zuora"
version: "1"

name: "creditBalanceAdjustment"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/credit balance adjustments
#
description: |
  The `{{ table.name }}` table contains information about [credit balance adjustments](https://knowledgecenter.zuora.com/CB_Billing/G_Credit_Balances){:target="new"}, or the application of credit balances to invoices, payments, and refunds.

replication-method: "Key-based Incremental"


attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The credit balance adjustment ID."
    # foreign-key-id: "credit-balance-adjustment-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the credit balance adjustment was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the contact."
    foreign-key-id: "account-id"

  - name: "accountingCode"
    type: "string"
    description: "The accounting code associated with the adjustment."
    foreign-key-id: "accounting-code"

  - name: "accountingPeriodId"
    type: "string"
    description: "The ID of the accounting period associated with the adjustment."
    foreign-key-id: "accounting-period-id"

  - name: "accountReceivableAccountingCodeId"
    type: "string"
    description: "The ID of the account's receivable accounting code associated with the adjustment."
    foreign-key-id: "account-receivable-accounting-code-id"

  - name: "adjustmentDate"
    type: "date-time"
    description: "The date when the adjustment was applied."

  - name: "amount"
    type: "double"
    description: "The amount of the adjustment."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the billing contact associated with the account to whom the product/service is billed."
    foreign-key-id: "bill-to-contact-id"

  - name: "cancelledOn"
    type: "date-time"
    description: "The date when the adjustment was canceled."

  - name: "cashOnAccountAccountingCodeId"
    type: "string"
    description: "The accounting code for customer cash on account."
    foreign-key-id: "cash-on-account-accounting-code-id"

  - name: "comment"
    type: "string"
    description: "Any comments about the adjustment."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the credit balance adjustment."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the credit balance adjustment was created."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The default payment method the associated account uses to make payments."
    foreign-key-id: "default-payment-method-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "invoiceId"
    type: "string"
    description: "The ID of the invoice to which the adjustment is applied."
    foreign-key-id: "invoice-id"

  - name: "journalEntryId"
    type: "string"
    description: "The journal entry ID associated with the adjustment."
    foreign-key-id: "journal-entry-id"

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the adjustment."
    foreign-keyid: "journal-run-id"

  - name: "number"
    type: "string"
    description: "A unique identifier for the adjustment, generated by {{ integration.display_name }}."

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in {{ integration.display_name }}."
    foreign-key-id: "parent-account-id"

  - name: "paymentId"
    type: "string"
    description: "The ID of the payment associated with the adjustment."
    foreign-key-id: "payment-id"

  - name: "paymentMethodId"
    type: "string"
    description: "The ID of the payment method associated with the adjustment."
    foreign-key-id: "payment-method-id"

  - name: "paymentMethodSnapshotId"
    type: "string"
    description: "The ID of the payment method snapshot associated with the adjustment."
    foreign-key-id: "payment-method-snapshot-id"

  - name: "reasonCode"
    type: "string"
    description: "The code identifying the reason for the adjustment."

  - name: "referenceId"
    type: "string"
    description: "The ID of the payment that the adjustment is for."
    foreign-key-id: "reference-id"

  - name: "refundId"
    type: "string"
    description: "The ID of the refund associated with the adjustment."
    foreign-key-id: "refund-id"

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key-id: "sold-to-contact-id"

  - name: "sourceTransactionId"
    type: "string"
    description: |
      The ID of the object that the adjustment was applied to.

      Depending on the type of transaction (`sourceTransactionType` value), this field will be a foreign key to either the `invoice`, `payment`, or `refund` table.
    foreign-key-id: "source-transaction-id"

  - name: "sourceTransactionNumber"
    type: "string"
    description: |
      The number of the object that the adjustment was applied to.

      Depending on the type of transaction (`sourceTransactionType` value), this field will be a foreign key to either the `invoice`, `payment`, or `refund` table.
    foreign-key-id: "source-transaction-number"

  - name: "sourceTransactionType"
    type: "string"
    description: |
      The source of the adjustment. Possible values are:

      - `Invoice`
      - `Payment`
      - `Refund`

  - name: "status"
    type: "string"
    description: |
      The status of the adjustment. Possible values are:

      - `Processed`
      - `Canceled`

  - name: "transferredToAccounting"
    type: "string"
    description: |
      The status of the adjustment being transferred to an external accounting system, such as NetSuite. Possible values are:

      - `Processing`
      - `Yes`
      - `Error`
      - `Ignore`

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the credit balance adjustment."
---