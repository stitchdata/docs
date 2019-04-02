---
tap: "netsuite"
# version: "1.0"

name: "ItemAccountMapping"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemAccountMapping.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "varies"
    description: ""

  - name: "accountingBook"
    type: "varies"
    description: ""

  - name: "customDimension"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "destinationAccount"
    type: "varies"
    description: ""

  - name: "effectiveDate"
    type: "date-time"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "itemAccount"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "sourceAccount"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---
