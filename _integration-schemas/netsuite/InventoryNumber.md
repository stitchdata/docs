---
tap: "netsuite"
version: "1.0"

name: "InventoryNumber"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/inventorynumber.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/InventoryNumber.json"
description: |
  The `{{ table.name }}` table contains info about the serial or lot numbers in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "inventory-number"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "inventory-number-id"

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "expirationDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "inventoryNumber"
    type: "string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "locationsList"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "units"
    type: "string"
    description: ""
---