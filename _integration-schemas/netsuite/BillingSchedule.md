---
tap: "netsuite"
# version: "1.0"

name: "BillingSchedule"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/BillingSchedule.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "applyToSubtotal"
    type: "boolean, string"
    description: ""

  - name: "billForActuals"
    type: "boolean, string"
    description: ""

  - name: "dayPeriod"
    type: "integer, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "frequency"
    type: "varies"
    description: ""

  - name: "inArrears"
    type: "boolean, string"
    description: ""

  - name: "initialAmount"
    type: "string"
    description: ""

  - name: "initialTerms"
    type: "varies"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isPublic"
    type: "boolean, string"
    description: ""

  - name: "milestoneList"
    type: "varies"
    description: ""

  - name: "monthDom"
    type: "integer, string"
    description: ""

  - name: "monthDow"
    type: "varies"
    description: ""

  - name: "monthDowim"
    type: "varies"
    description: ""

  - name: "monthMode"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numberRemaining"
    type: "integer, string"
    description: ""

  - name: "project"
    type: "varies"
    description: ""

  - name: "recurrenceDowMaskList"
    type: "varies"
    description: ""

  - name: "recurrenceList"
    type: "varies"
    description: ""

  - name: "recurrencePattern"
    type: "varies"
    description: ""

  - name: "recurrenceTerms"
    type: "varies"
    description: ""

  - name: "repeatEvery"
    type: "varies"
    description: ""

  - name: "scheduleType"
    type: "varies"
    description: ""

  - name: "seriesStartDate"
    type: "date-time"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""

  - name: "yearDom"
    type: "integer, string"
    description: ""

  - name: "yearDow"
    type: "varies"
    description: ""

  - name: "yearDowim"
    type: "varies"
    description: ""

  - name: "yearDowimMonth"
    type: "varies"
    description: ""

  - name: "yearMode"
    type: "varies"
    description: ""

  - name: "yearMonth"
    type: "varies"
    description: ""
---
