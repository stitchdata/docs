---
tap: "zuora"
version: 1.0 

name: "ratePlan"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Rate-Plans
description: |
  The `{{ table.name }}` table contains info about rate plans, which is a price or collection of prices for services.

  #### Custom fields {#rate-plan-custom-fields}

  In addition to the attributes listed below, our {{ integration.display_name }} integration will also replicate any custom fields.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The rate plan ID."
    foreign-key-id: "rate-plan-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date that the rate plan was last updated."

  - name: "amendmentId"
    type: "string"
    description: "The ID of the amendment associated with the rate plan."
    foreign-key-id: "amendment-id"

  - name: "amendmentType"
    type: "string"
    description: "The type of amendment associated with the rate plan."

  - name: "billToContactId"
    type: "string"
    description: "The ID of the person to bill for the account associated with the rate plan."
    foreign-key-id: "bill-to-contact-id"

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the rate plan."

  - name: "createdDate"
    type: "date-time"
    description: "The date that the rate plan was last updated."

  - name: "name"
    type: "string"
    description: "The name of the rate plan."

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the associated product rate plan."
    foreign-key-id: "product-rate-plan-id"

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription that the rate plan belongs to."
    foreign-key-id: "subscription-id"

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the rate plan."
---