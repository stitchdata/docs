---
tap: "netsuite"
# version: "1.0"

name: "ItemSupplyPlan"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemSupplyPlan.json"
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

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "location"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "orderList"
    type: "anything"
    description: ""

  - name: "subsidiary"
    type: "anything"
    description: ""

  - name: "units"
    type: "anything"
    description: ""
---
