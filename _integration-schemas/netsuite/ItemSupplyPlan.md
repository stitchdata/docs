---
tap: "netsuite"
version: "1.0"

name: "ItemSupplyPlan"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/itemsupplyplan.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemSupplyPlan.json"
description: |
  The `{{ table.name }}` table contains info about the item supply plans in your {{ integration.display_name }} account. An item supply plan lists the purchase orders or work orders required to ensure that item quantity meets expected demand.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-supply-plan"

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