---
tap: "clubspeed"
version: "1"

name: "discount_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/discount_types.json"
description: |
  The `{{ table.name }}` table contains info about discount types.

replication-method: "Full Table"

attributes:
  - name: "discountId"
    type: "integer"
    primary-key: true
    description: "The discount ID."
    foreign-key-id: "discount-id" 

  - name: "amount"
    type: "number"
    description: "The amount of the discount. Refer to `calculateType` for usage."

  - name: "calculateType"
    type: "integer"
    description: |
      The calculation type for the discount, which determines how `amount` is calculated. Possible values are:

      - `1` - Amount
      - `2` - Percentage

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the discount has been soft deleted."

  - name: "description"
    type: "string"
    description: "The description for the discount."

  - name: "enabled"
    type: "boolean"
    description: "Indicates whether the discount is currently enabled."

  - name: "needApproved"
    type: "boolean"
    description: "Indicates whether the discount should require manager approval."

  - name: "productClassId"
    type: "integer"
    description: "The product class that is applicable for the discount."
    foreign-key-id: "product-class-id"
---