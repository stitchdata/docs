---
tap: "netsuite"
# version: "1.0"

name: "Paycheck"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Paycheck.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "varies"
    description: ""

  - name: "account"
    type: "varies"
    description: ""

  - name: "address"
    type: "string"
    description: ""

  - name: "balance"
    type: "number, string"
    description: ""

  - name: "batchNumber"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "entity"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "payContribList"
    type: "varies"
    description: ""

  - name: "payDeductList"
    type: "varies"
    description: ""

  - name: "payDisburseList"
    type: "varies"
    description: ""

  - name: "payEarnList"
    type: "varies"
    description: ""

  - name: "payExpList"
    type: "varies"
    description: ""

  - name: "payFrequency"
    type: "string"
    description: ""

  - name: "payPtoList"
    type: "varies"
    description: ""

  - name: "paySummaryList"
    type: "varies"
    description: ""

  - name: "payTaxList"
    type: "varies"
    description: ""

  - name: "payTimeList"
    type: "varies"
    description: ""

  - name: "periodEnding"
    type: "date-time"
    description: ""

  - name: "postingPeriod"
    type: "varies"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tranDate"
    type: "date-time"
    description: ""

  - name: "tranId"
    type: "string"
    description: ""

  - name: "userAmount"
    type: "number, string"
    description: ""

  - name: "workplace"
    type: "varies"
    description: ""
---
