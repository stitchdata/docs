---
tap: "zuora"
version: 1.0

name: "ratePlanChargeTier"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Rate-Plan-Charge-Tiers
description: |
  The `ratePlanChargeTier` table contains pricing info for rate plan charges.

replication-method: "Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The rate plan charge tier ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the rate plan charge tier was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the rate plan charge tier."

  - name: "createdDate"
    type: "date-time"
    description: "The date the rate plan charge tier was created."

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

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the subscription or amendment rate plan charge associated with the tier."
    ## foreign-keys:
    ##   - table-name: "ratePlanCharge"
    ##     attribute: "id"

  - name: "startingUnit"
    type: "number"
    description: "The starting number of a range of units for the tier."

  - name: "tier"
    type: "integer"
    description: "A unique number that identifies the tier that the price applies to."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the rate plan charge tier."
---