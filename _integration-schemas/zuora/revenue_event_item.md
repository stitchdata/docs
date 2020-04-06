---
tap: "zuora"
version: "1"

name: "revenueEventItem"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Revenue-Events
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about revenue events. A revenue event is a change to a revenue schedule, such as creating the initial schedule, canceling an invoice, or recognizing an undistributed amount.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The revenue event item ID."
    foreign-key-id: "revenue-event-item-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the revenue event item was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the revenue event item."
    foreign-key-id: "account-id"

  - name: "amendmentId"
    type: "string"
    description: "The ID of the amendment associated with the revenue event item."
    foreign-key-id: "amendment-id"

  - name: "amount"
    type: "double"
    description: "The amount of the revenue event item."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the billing contact associated with the account to whom the product/service is billed."
    foreign-key-id: "bill-to-contact-id"

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the revenue event item."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the revenue event item was created."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The default payment method the associated account uses to make payments."
    foreign-key-id: "default-payment-method-id"

  - name: "deferredRevenueAccountingCodeId"
    type: "string"
    description: "The accounting code for deferred revenue."
    foreign-key-id: "deferred-revenue-accounting-code-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "journalEntryId"
    type: "string"
    description: "The journal entry ID associated with the revenue event item."
    foreign-key-id: "journal-entry-id"

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the revenue event item."
    foreign-key-id: "journal-run-id"

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in {{ integration.display_name }}."
    foreign-key-id: "parent-account-id"

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the revenue event item."
    foreign-key-id: "product-id"

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the product rate plan charge associated with the revenue event item."
    foreign-key-id: "product-rate-plan-charge-id"

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with the revenue event item."
    foreign-key-id: "product-rate-plan-id"

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the revenue event item."
    foreign-key-id: "rate-plan-charge-id"

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the revenue event item."
    foreign-key-id: "rate-plan-id"

  - name: "recognizedRevenueAccountingCodeId"
    type: "string"
    description: "The ID of the accounting code used for recognized revenue."
    foreign-key-id: "recognized-revenue-accounting-code-id"

  - name: "revenueChargeSummaryId"
    type: "string"
    description: "The ID of the revenue summary for the subscription charge."
    foreign-key-id: "revenue-charge-summary-id"

  - name: "revenueEventId"
    type: "string"
    description: "The ID of the revenue event associated with the revenue event item."
    foreign-key-id: "revenue-event-id"

  - name: "revenueEventTypeId"
    type: "string"
    description: "The ID of the type of the revenue event."
    foreign-key-id: "revenue-event-type-id"

  - name: "revenueScheduleId"
    type: "string"
    description: "The ID of the revenue schedule associated with the revenue event item. A revenue schedule represents how revenue is recognized over time."
    foreign-key-id: "revenue-schedule-id"

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key-id: "sold-to-contact-id"

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription associated with the revenue event item."
    foreign-key-id: "subscription-id"

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the revenue event item."
---