---
tap: "codat"
version: "1"
key: "item"

name: "items"
doc-link: "https://docs.codat.io/reference/items"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/items.json"
description: |
  The {{ table.name }} table contains information about items for a given company in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get items"
  doc-link: "https://docs.codat.io/reference/items#items_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The item ID."
    foreign-key-id: "item-id"

  - name: "modifiedDate"
    type: "string"
    description: "The date the item was last modified."
    replication-key: true  

  - name: "billItem"
    type: "object"
    description: ""
    subattributes: &ref-items
      - name: "accountRef"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "account-id"

      - name: "description"
        type: "string"
        description: ""

      - name: "taxRateRef"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "tax-id"

      - name: "unitPrice"
        type: "number"
        description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "invoiceItem"
    type: "object"
    description: ""
    subattributes: *ref-items

  - name: "isBillItem"
    type: "boolean"
    description: ""

  - name: "isInvoiceItem"
    type: "boolean"
    description: ""

  - name: "itemStatus"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "sourceModifiedDate"
    type: "string"
    description: ""
---