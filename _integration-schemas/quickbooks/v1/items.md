---
tap: "quickbooks"
version: "1"
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

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "AssetAccountRef"
    type: "object"
    description: "Details about the asset account associated with the item."
    subattributes: &account-attributes
      - name: "name"
        type: "string"
        description: ""

      - &account-id
        name: "value"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

  - name: "Description"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExpenseAccountRef"
    type: "object"
    description: ""
    subattributes: *account-attributes

  - name: "FullyQualifiedName"
    type: "string"
    description: ""

  - name: "IncomeAccountRef"
    type: "object"
    description: ""
    subattributes: *account-attributes

  - name: "InvStartDate"
    type: "date-time"
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

  - name: "PurchaseCost"
    type: "integer, decimal"
    description: ""

  - name: "PurchaseDesc"
    type: "string"
    description: ""

  - name: "QtyOnHand"
    type: "integer"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "Taxable"
    type: "boolean"
    description: ""

  - name: "TrackQtyOnHand"
    type: "boolean"
    description: ""

  - name: "Type"
    type: "string"
    description: ""

  - name: "UnitPrice"
    type: "integer"
    description: ""
---