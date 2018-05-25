---
tap: "zuora"
version: 1.0

name: "revenueEventItemInvoiceItemAdjustment"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Revenue-Events
#singer-schema: 
description: |
  The `revenueEventItemInvoiceItemAdjustment` table contains information about revenue event items that are associated with invoice item adjustments.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice item adjustment ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the invoice item adjustment was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the invoice item adjustment."
    foreign-key: true

  - name: "accountingPeriodId"
    type: "string"
    description: "The ID of the accounting period associated with the invoice item adjustment."
    foreign-key: true

  - name: "amendmentId"
    type: "string"
    description: "The ID of the amendment associated with the invoice item adjustment."
    foreign-key: true

  - name: "amount"
    type: "double"
    description: "The amount of the invoice item adjustment."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the billing contact associated with the account to whom the product/service is billed."
    foreign-key: true

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the invoice item adjustment."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the invoice item adjustment was created."

  - name: "currency"
    type: "string"
    description: "The currency used."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The default payment method the associated account uses to make payments."
    foreign-key: true

  - name: "deferredRevenueAccountingCodeId"
    type: "string"
    description: "The accounting code for deferred revenue."
    foreign-key: true

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "invoiceId"
    type: "string"
    description: "The ID of the invoice to which the payment is applied."
    foreign-key: true

  - name: "invoiceItemId"
    type: "string"
    description: "The ID of the invoice line item associated with the invoice item adjustment."
    foreign-key: true

  - name: "invoiceItemAdjustmentId"
    type: "string"
    description: "The ID of the invoice line item adjustment associated with the record."

  - name: "journalEntryId"
    type: "string"
    description: "The journal entry ID associated with the invoice item adjustment."
    foreign-key: true

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the invoice item adjustment."
    foreign-key: true

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in Zuora."
    foreign-key: true

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the invoice item adjustment."
    foreign-key: true

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the product rate plan charge associated with the invoice item adjustment."
    foreign-key: true

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with the invoice item adjustment."
    foreign-key: true

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the invoice item adjustment."
    foreign-key: true

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the invoice item adjustment."
    foreign-key: true

  - name: "recognizedRevenueAccountingCodeId"
    type: "string"
    description: "The ID of the accounting code used for recognized revenue."
    foreign-key: true

  - name: "revenueChargeSummaryId"
    type: "string"
    description: "The ID of the revenue summary for the subscription charge."
    foreign-key: true

  - name: "revenueEventInvoiceItemAdjustmentId"
    type: "string"
    description: "The ID of the revenue event associated with the invoice adjustment."
    foreign-key: true

  - name: "revenueEventInvoiceId"
    type: "string"
    description: "The ID of the revenue event associated with the invoice item."
    foreign-key: true

  - name: "revenueEventTypeId"
    type: "string"
    description: "The ID of the type of the revenue event that triggered a change to the revenue schedule."
    foreign-key: true

  - name: "revenueScheduleInvoiceItemAdjustmentId"
    type: "string"
    description: "The ID of the revenue schedule associated with the invoice item adjustment. A revenue schedule represents how revenue is recognized over time."
    foreign-key: true

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key: true

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription associated with the invoice item adjustment."
    foreign-key: true

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the invoice item adjustment."

---