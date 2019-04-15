---
tap: "netsuite"
version: "1.0"

name: "CostCategory"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/costcategory.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CostCategory.json"
description: |
  The `{{ table.name }}` table contains info about cost categories, which are used to classify different types of costs associated with items.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Setup"
  name: "Accounting Lists"

feature-requirements:
  - tab: &iai "Items & Inventory"
    name: "Standard Costing"
    description: ", or"

  - tab: *iai
    name: "Landed Cost"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "cost-category-id"

  - name: "account"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "itemCostType"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""
---