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
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "defaultRate"
    type: "number, string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "expenseAcct"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "rateRequired"
    type: "boolean, string"
    description: ""

  - name: "ratesList"
    type: "anything"
    description: ""

  - name: "subsidiaryList"
    type: "anything"
    description: ""

  - name: "translationsList"
    type: "anything"
    description: ""
---
