---
tap: "netsuite"
# version: "1.0"

name: "FairValuePrice"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/FairValuePrice.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "currency"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "dimensionList"
    type: "anything"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fairValue"
    type: "number, string"
    description: ""

  - name: "fairValueFormula"
    type: "anything"
    description: ""

  - name: "fairValueRangePolicy"
    type: "anything"
    description: ""

  - name: "highValue"
    type: "number, string"
    description: ""

  - name: "highValuePercent"
    type: "number, string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isVsoePrice"
    type: "boolean, string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "itemRevenueCategory"
    type: "anything"
    description: ""

  - name: "lowValue"
    type: "number, string"
    description: ""

  - name: "lowValuePercent"
    type: "number, string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "units"
    type: "anything"
    description: ""

  - name: "unitsType"
    type: "anything"
    description: ""
---
