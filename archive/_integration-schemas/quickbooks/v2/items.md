---
tap: "quickbooks"
version: "2"
key: "item"

name: "items"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/item"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/items.json"
description: |
  The `{{ table.name }}` table contains info about the items your company buys, sells, or re-sells. This includes all item types in {{ integration.display_name }}, such as `Inventory`, `Group`, `Service` and `Noninventory`.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query an item"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/item/#query-an-item"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The item ID."
    foreign-key-id: "item-id"

  - name: "AbatementRate"
    type: "decimal"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "AssetAccountRef"
    type: "object"
    description: "Details about the asset account associated with the item."
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "ClassRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "Description"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExpenseAccountRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "FullyQualifiedName"
    type: "string"
    description: ""

  - name: "IncomeAccountRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "InvStartDate"
    type: "date-time"
    description: ""

  - name: "ItemCategoryType"
    type: "string"
    description: ""

  - name: "Level"
    type: "integer"
    description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "ParentRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "PrefVendorRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "PurchaseCost"
    type: "integer, decimal"
    description: ""

  - name: "PurchaseDesc"
    type: "string"
    description: ""

  - name: "PurchaseTaxCodeRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "PurchaseTaxIncluded"
    type: "boolean"
    description: ""

  - name: "QtyOnHand"
    type: "integer"
    description: ""

  - name: "ReorderPoint"
    type: "number"
    description: ""

  - name: "ReverseChargeRate"
    type: "decimal"
    description: ""

  - name: "SalesTaxIncluded"
    type: "boolean"
    description: ""

  - name: "SalesTaxCodeRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "ServiceType"
    type: "string"
    description: ""

  - name: "Sku"
    type: "string"
    description: ""

  - name: "Source"
    type: "string"
    description: ""

  - name: "SubItem"
    type: "boolean"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "Taxable"
    type: "boolean"
    description: ""

  - name: "TaxClassificationRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "TrackQtyOnHand"
    type: "boolean"
    description: ""

  - name: "Type"
    type: "string"
    description: ""

  - name: "UnitPrice"
    type: "decimal"
    description: ""

  - name: "UQCDisplayText"
    type: "string"
    description: ""

  - name: "UQCId"
    type: "string"
    description: ""
---