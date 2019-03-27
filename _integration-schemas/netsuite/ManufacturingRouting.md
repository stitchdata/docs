---
tap: "netsuite"
# version: "1.0"

name: "ManufacturingRouting"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ManufacturingRouting.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "autoCalculateLag"
    type: "boolean, string"
    description: ""

  - name: "billOfMaterials"
    type: "anything"
    description: ""

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

  - name: "isDefault"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "locationList"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "routingComponentList"
    type: "anything"
    description: ""

  - name: "routingStepList"
    type: "anything"
    description: ""

  - name: "subsidiary"
    type: "anything"
    description: ""
---
