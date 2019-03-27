---
tap: "netsuite"
# version: "1.0"

name: "InventoryNumber"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/InventoryNumber.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "expirationDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "inventoryNumber"
    type: "string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "locationsList"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "units"
    type: "string"
    description: ""
---
