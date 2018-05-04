---
tap: "zuora"
version: 1.0

name: "discountAppliedMetrics"
doc-link: https://knowledgecenter.zuora.com/CD_Reporting/D_Data_Sources_and_Exports/C_Data_Source_Reference/Discount_Applied_Metrics_Data_Sourceadjustments
#singer-schema: 
description: |
  The `discountAppliedMetrics` table contains information about rate plan charges that use either a discount-fixed amount or discount-percentage charge model.

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The credit balance adjustment ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the credit balance adjustment was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the contact."
    foreign-key: true

  - name: "amendmentId"
    type: "string"
    description: "The ID of the subscription amendment associated with this record."
    foreign-key: true

  - name: "billToContactId"
    type: "string"
    description: "The ID of the billing contact associated with the account to whom the product/service is billed."
    foreign-key: true

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the discount application."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the discount application was created."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The default payment method the associated account uses to make payments."
    foreign-key: true

  - name: "discountRatePlanChargeId"
    type: "string"
    description: "The ID of the Rate Plan Charge that represents the discount."
    foreign-key: true

  - name: "mrr"
    type: "string"
    description: "The monthly recurring revenue associated with the account."

  - name: "parentAccountId"
    type: "string"
    description: "The ID of the parent customer account for this account. This field is used when customer hierarchy is enabled in Zuora."
    foreign-key: true

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the discount application."
    foreign-key: true

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the product rate plan charge associated with the discount application."
    foreign-key: true

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with the discount application."
    foreign-key: true

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the discount application."
    foreign-key: true

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the discount application."
    foreign-key: true

  - name: "soldToContactId"
    type: "string"
    description: "The ID of the person who bought the subscription associated with the account."
    foreign-key: true

  - name: "startDate"
    type: "date-time"
    description: "The earliest date that the discount applies."

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription to which the rate plan is associated."
    foreign-key: true

  - name: "tcv"
    type: "string"
    description: "The total contract value of the discount."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the discount application."

---