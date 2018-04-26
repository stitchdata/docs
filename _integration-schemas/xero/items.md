---
tap: "xero"
version: "1.0"

name: "items"
doc-link: &api-doc https://developer.xero.com/documentation/api/items
singer-schema:  https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/items.json
description: |
  The `items` table contains info about the [products and services you buy and sell](https://help.xero.com/us/Inventory).

replication-method: "Incremental"

api-method:
  name: getItems
  doc-link: *api-doc

attributes:
  - name: "ItemID"
    type: "string"
    primary-key: true
    description: "The item ID."

  - name: "UpdatedDateUTC"
    type: "string"
    replication-key: true
    description: "The date the item was last updated."

  - name: "Code"
    type: "string"
    description: "The user-defined code for the item."

  - name: "IsSold"
    type: "boolean"
    description: "If `true`, the item is available on sales transactions."

  - name: "IsPurchased"
    type: "boolean"
    description: "If `true`, the item is available for purchase transactions."

  - name: "Description"
    type: "string"
    description: "The sales description of the item."

  - name: "PurchaseDescription"
    type: "string"
    description: "The purchase description of the item."

  - name: "PurchaseDetails"
    type: "object"
    description: "The item's purchase details."
    doc-link: https://developer.xero.com/documentation/api/items#PurchasesSales
    object-attributes:
      - name: "TaxType"
        type: "string"
        description: "The tax type used for the item in purchase transactions."

      - name: "COGSAccountCode"
        type: "string" 
        description: "The cost of goods sold account for the item in purchase transactions."

      - name: "UnitPrice"
        type: "number"
        description: "The unit price of the item in purchase transactions."

      - name: "AccountCode"
        type: "string"
        description: "The default account code for the item in purchase transactions."

  - name: "SalesDetails"
    type: "object"
    description: "The item's sales details."
    doc-link: 
    object-attributes:
      - name: "UnitPrice"
        type: "number"
        description: "The unit price of the item in sales transactions."

      - name: "AccountCode"
        type: "string"
        description: "The default account code for the item in sales transactions."

  - name: "IsTrackedAsInventory"
    type: "boolean"
    description: |
      If `true`, the item is tracked as inventory.

      **Note**: This field will only be `true` if `InventoryAssetAccountCode` and `COGSAccountCode` in Purchase Details are set.

  - name: "InventoryAssetAccountCode"
    type: "string"
    description: "The inventory asset account for the item, if applicable."

  - name: "TotalCostPool"
    type: "number"
    description: "The value of the item on hand, calculated using average cost accounting."

  - name: "QuantityOnHand"
    type: "number"
    description: "The quantity of the item on hand."
---