---
tap: "zuora"
version: 1.0

name: "productRatePlan"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Product-Rate-Plans
description: |
  The `{{ table.name }}` table contains info about product rate plans, or the part of a product that customers can subscribe to.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The product rate plan ID."
    foreign-key-id: "product-rate-plan-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the product rate plan was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the product rate plan."

  - name: "createdDate"
    type: "date-time"
    description: "The date the product rate plan was created."

  - name: "defaultPaymentMethodId"
    type: "string"
    description: "The ID of the default payment method associated with the account."
    foreign-key-id: "default-payment-method-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "description"
    type: "string"
    description: "The description of the product rate plan."

  - name: "effectiveEndDate"
    type: "date-time"
    description: "The date when the product rate plan expires and can't be subscribed to anymore."

  - name: "effectiveStartDate"
    type: "date-time"
    description: "The date when the product rate plan becomes available and can be subscribed to."

  - name: "name"
    type: "string"
    description: "The name of the product rate plan."

  - name: "productId"
    type: "string"
    description: "The ID of the product that contains the product rate plan."
    foreign-key-id: "product-id"

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the product rate plan."
---