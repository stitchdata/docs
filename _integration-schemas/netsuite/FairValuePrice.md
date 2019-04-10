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
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dimensionList"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "fairValueRangePolicy"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "itemRevenueCategory"
    type: "varies"
    description: ""

  - name: "lowValue"
    type: "number, string"
    description: ""

  - name: "lowValuePercent"
    type: "number, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "units"
    type: "varies"
    description: ""

  - name: "unitsType"
    type: "varies"
    description: ""
---
