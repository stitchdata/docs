---
tap: "netsuite"
# version: "1.0"

name: "ItemDemandPlan"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemDemandPlan.json"
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

  - name: "demandPlanCalendarType"
    type: "anything"
    description: ""

  - name: "demandPlanMatrix"
    type: "anything"
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

  - name: "item"
    type: "anything"
    description: ""

  - name: "location"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "month"
    type: "anything"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "subsidiary"
    type: "anything"
    description: ""

  - name: "units"
    type: "anything"
    description: ""

  - name: "year"
    type: "integer, string"
    description: ""
---
