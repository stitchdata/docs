---
tap: "netsuite"
# version: "1.0"

name: "RevRecTemplate"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/RevRecTemplate.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "amortizationPeriod"
    type: "integer, string"
    description: ""

  - name: "amortizationType"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "initialAmount"
    type: "number, string"
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

  - name: "periodOffset"
    type: "integer, string"
    description: ""

  - name: "recogIntervalSrc"
    type: "varies"
    description: ""

  - name: "recurrenceList"
    type: "varies"
    description: ""

  - name: "recurrenceType"
    type: "varies"
    description: ""

  - name: "revRecOffset"
    type: "integer, string"
    description: ""
---
