---
tap: "netsuite"
# version: "1.0"

name: "CustomList"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CustomList.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "convertToCustomRecord"
    type: "boolean, string"
    description: ""

  - name: "customValueList"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isMatrixOption"
    type: "boolean, string"
    description: ""

  - name: "isOrdered"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "scriptId"
    type: "string"
    description: ""

  - name: "translationsList"
    type: "varies"
    description: ""
---
