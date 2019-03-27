---
tap: "netsuite"
# version: "1.0"

name: "RevRecSchedule"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/RevRecSchedule.json"
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
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "periodOffset"
    type: "integer, string"
    description: ""

  - name: "recogIntervalSrc"
    type: "anything"
    description: ""

  - name: "recurrenceList"
    type: "anything"
    description: ""

  - name: "recurrenceType"
    type: "anything"
    description: ""

  - name: "revRecOffset"
    type: "integer, string"
    description: ""
---
