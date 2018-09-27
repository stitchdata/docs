---
tap: "zuora"
version: 1.0

name: "processedUsage"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Accounts
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about usage.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The processed usage ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the processed usage record was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the processed usage record."
    foreign-key-id: "account-id"

  - name: "amendmentId"
    type: "string"
    description: "The ID of the amendment associated with the processed usage record."
    foreign-key-id: "amendment-id"

  - name: "amount"
    type: "double"
    description: "The amount of the processed usage."

  - name: "billingPeriodEndDate"
    type: "date-time"
    description: "The end date of the billing period associated with the processed usage record."

  - name: "billingPeriodStartDate"
    type: "date-time"
    description: "The start date of the billing period associated with the processed usage record."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the account's billing contact."
    foreign-key-id: "bill-to-contact-id"

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the processed usage record."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the processed usage record was created."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The ID of the default payment method for the account associated with the processed usage record."
    foreign-key-id: "default-payment-method-id"

  - name: "invoiceId"
    type: "string"
    description: "The ID of the invoice to which payment for this record was applied."
    foreign-key-id: "invoice-id"

  - name: "invoiceItemId"
    type: "string"
    description: "The ID of this record on the invoice."
    foreign-key-id: "invoice-item-id"

  # - name: "newUsageId"
  #   type: "string"
  #   description: "[PLACEHOLDER]"

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account associated with `accountId`. This field is used when customer hierarchy is enabled in Zuora."
    foreign-key-id: "parent-account-id"

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the processed usage record."
    foreign-key-id: "product-id"

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the product rate plan charge associated with the processed usage record."
    foreign-key-id: "product-rate-plan-charge-id"

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with the processed usage record."
    foreign-key-id: "product-rate-plan-id"

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the processed usage record."
    foreign-key-id: "rate-plan-charge-id"

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the processed usage record."
    foreign-key-id: "rate-plan-id"

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key-id: "sold-to-contact-id"

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the processed usage record."

  - name: "usageId"
    type: "string"
    description: "The ID of the usage record associated with the processed usage record."
    foreign-key-id: "usage-id"
---