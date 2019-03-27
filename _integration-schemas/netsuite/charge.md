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
    type: "anything"
    description: ""

  - name: "amount"
    type: "number, string"
    description: ""

  - name: "billTo"
    type: "anything"
    description: ""

  - name: "billingAccount"
    type: "anything"
    description: ""

  - name: "billingItem"
    type: "anything"
    description: ""

  - name: "chargeDate"
    type: "date-time"
    description: ""

  - name: "chargeType"
    type: "anything"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "department"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "invoiceLine"
    type: "anything"
    description: ""

  - name: "location"
    type: "anything"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "projectTask"
    type: "anything"
    description: ""

  - name: "quantity"
    type: "number, string"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "rule"
    type: "anything"
    description: ""

  - name: "runId"
    type: "string"
    description: ""

  - name: "salesOrder"
    type: "anything"
    description: ""

  - name: "salesOrderLine"
    type: "anything"
    description: ""

  - name: "stage"
    type: "anything"
    description: ""

  - name: "subscriptionLine"
    type: "anything"
    description: ""

  - name: "timeRecord"
    type: "anything"
    description: ""

  - name: "transaction"
    type: "anything"
    description: ""

  - name: "transactionLine"
    type: "anything"
    description: ""

  - name: "use"
    type: "anything"
    description: ""
---
