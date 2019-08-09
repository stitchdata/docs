---
tap: "zuora"
version: 1.0

name: "revenueChargeSummaryItem"
doc-link: https://live-www.zuora.com/developer/api-reference/#operation/GET_CRSByCRSNumber
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about [charge revenue summaries](https://knowledgecenter.zuora.com/CC_Finance/Revenue_Recognition/G_Revenue_Schedules/M_Charge_Revenue_Summary){:target="new"}, which are summaries of all revenue distributions associated with a subscription charge.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The revenue charge summary item ID."
    foreign-key-id: "revenue-charge-summary-item-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the revenue charge summary item was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the revenue charge summary item."
    foreign-key-id: "account-id"

  - name: "accountingPeriodId"
    type: "string"
    description: "The ID of the accounting period associated with the revenue charge summary item."
    foreign-key-id: "accounting-period-id"

  - name: "amendmentId"
    type: "string"
    description: "The ID of the amendment associated with the revenue charge summary item."
    foreign-key-id: "amendment-id"

  - name: "amount"
    type: "double"
    description: "The revenue schedule amount, which is the sum of all revenue items."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the billing contact associated with the account to whom the product/service is billed."
    foreign-key-id: "bill-to-contact-id"

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the revenue charge summary item."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the revenue charge summary item was created."

  - name: "currency"
    type: "string"
    description: "The currency used."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The default payment method the associated account uses to make payments."
    foreign-key-id: "default-payment-method-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in {{ integration.display_name }}."
    foreign-key-id: "parent-account-id"

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the revenue charge summary item."
    foreign-key-id: "product-id"

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the product rate plan charge associated with the revenue charge summary item."
    foreign-key-id: "product-rate-plan-charge-id"

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with the revenue charge summary item."
    foreign-key-id: "product-rate-plan-id"

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the revenue charge summary item."
    foreign-key-id: "rate-plan-charge-id"

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the revenue charge summary item."
    foreign-key-id: "rate-plan-id"

  - name: "revenueChargeSummaryId"
    type: "string"
    description: "The ID of the revenue summary for the subscription charge."
    foreign-key-id: "revenue-charge-summary-id"

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key-id: "sold-to-contact-id"

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription associated with the revenue charge summary item."
    foreign-key-id: "subscription-id"

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the revenue charge summary item."
---