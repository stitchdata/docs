---
tap: "netsuite"
# version: "1.0"

name: "Term"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Term.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "dateDriven"
    type: "boolean, string"
    description: ""

  - name: "dayDiscountExpires"
    type: "integer, string"
    description: ""

  - name: "dayOfMonthNetDue"
    type: "integer, string"
    description: ""

  - name: "daysUntilExpiry"
    type: "integer, string"
    description: ""

  - name: "daysUntilNetDue"
    type: "integer, string"
    description: ""

  - name: "discountPercent"
    type: "number, string"
    description: ""

  - name: "discountPercentDateDriven"
    type: "number, string"
    description: ""

  - name: "dueNextMonthIfWithinDays"
    type: "integer, string"
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

  - name: "preferred"
    type: "boolean, string"
    description: ""
---
