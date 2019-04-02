---
tap: "netsuite"
# version: "1.0"

name: "ExpenseCategory"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ExpenseCategory.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "defaultRate"
    type: "number, string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "expenseAcct"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "rateRequired"
    type: "boolean, string"
    description: ""

  - name: "ratesList"
    type: "varies"
    description: ""

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "translationsList"
    type: "varies"
    description: ""
---
