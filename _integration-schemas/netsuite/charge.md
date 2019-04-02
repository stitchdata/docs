---
tap: "netsuite"
# version: "1.0"

name: "Charge"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Charge.json"
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

  - name: "amount"
    type: "number, string"
    description: ""

  - name: "billTo"
    type: "varies"
    description: ""

  - name: "billingAccount"
    type: "varies"
    description: ""

  - name: "billingItem"
    type: "varies"
    description: ""

  - name: "chargeDate"
    type: "date-time"
    description: ""

  - name: "chargeType"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "invoice"
    type: "varies"
    description: ""

  - name: "invoiceLine"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "projectTask"
    type: "varies"
    description: ""

  - name: "quantity"
    type: "number, string"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "rule"
    type: "varies"
    description: ""

  - name: "runId"
    type: "string"
    description: ""

  - name: "salesOrder"
    type: "varies"
    description: ""

  - name: "salesOrderLine"
    type: "varies"
    description: ""

  - name: "stage"
    type: "varies"
    description: ""

  - name: "subscriptionLine"
    type: "varies"
    description: ""

  - name: "timeRecord"
    type: "varies"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""

  - name: "transactionLine"
    type: "varies"
    description: ""

  - name: "use"
    type: "varies"
    description: ""
---
