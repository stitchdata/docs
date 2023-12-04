---
tap: "zuora"
version: "1"

name: "productRatePlanChargeTier"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Product-Rate-Plan-Charge-Tiers
description: |
  The `{{ table.name }}` table contains pricing info for product rate plan charges.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The product rate plan charge tier ID."
    foreign-key-id: "product-rate-plan-charge-tier-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the product rate plan charge tier was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the product rate plan charge tier."

  - name: "createdDate"
    type: "date-time"
    description: "The date the product rate plan charge tier was created."

  - name: "currency"
    type: "string"
    description: "The code for the currency used by the tier's price."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "endingUnit"
    type: "number"
    description: "The end number of a range of units for the tier."

  - name: "price"
    type: "number"
    description: |
      This value will be either:

      - The price of the tier, if the charge is a flat fee
      - The price of each unit in the tier, if the charge model is tiered pricing

  - name: "priceFormat"
    type: "string"
    description: |
      The pricing type of the tier, for tiered and volume pricing models only. Possible values are:

      - `FlatFee`
      - `PerUnit`

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the product rate plan charge associated with the tier."
    foreign-key-id: "product-rate-plan-charge-id"

  - name: "productRatePlanId"
    type: "string"
    description: "The ID of the product rate plan associated with the tier."
    foreign-key-id: "product-rate-plan-id"

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the tier."
    foreign-key-id: "rate-plan-charge-id"

  - name: "ratePlanId"
    type: "string"
    description: "The ID of the rate plan associated with the tier."
    foreign-key-id: "rate-plan-id"

  - name: "startingUnit"
    type: "number"
    description: "The starting number of a range of units for the tier."

  - name: "tier"
    type: "integer"
    description: "A unique number that identifies the tier that the price applies to."

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the product rate plan charge tier."
---