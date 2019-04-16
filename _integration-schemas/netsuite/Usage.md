---
tap: "netsuite"
# version: "1.0"

name: "Usage"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Usage.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "customForm"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "subscriptionPlan"
    type: "varies"
    description: ""

  - name: "usageDate"
    type: "date-time"
    description: ""

  - name: "usageQuantity"
    type: "number, string"
    description: ""

  - name: "usageSubscription"
    type: "varies"
    description: ""

  - name: "usageSubscriptionLine"
    type: "varies"
    description: ""
---
