---
tap: "netsuite"
version: "1.0"

name: "ItemSupplyPlan"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/itemsupplyplan.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemSupplyPlan.json"
description: |
  The `{{ table.name }}` table contains info about the item supply plans in your {{ integration.display_name }} account. An item supply plan lists the purchase orders or work orders required to ensure that item quantity meets expected demand.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Item Supply Plan"

feature-requirements:
  - tab: "Items & Inventory"
    name: "Demand Planning"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "item-supply-plan-id"

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "orderList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "units"
    type: "varies"
    description: ""
---