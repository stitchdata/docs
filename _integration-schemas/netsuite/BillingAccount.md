---
tap: "netsuite"
# version: "1.0"

name: "BillingAccount"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/BillingAccount.json"
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

  - name: "billingSchedule"
    type: "varies"
    description: ""

  - name: "cashSaleForm"
    type: "varies"
    description: ""

  - name: "createdBy"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "customerDefault"
    type: "boolean, string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "frequency"
    type: "varies"
    description: ""

  - name: "idNumber"
    type: "string"
    description: ""

  - name: "inactive"
    type: "boolean, string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "invoiceForm"
    type: "varies"
    description: ""

  - name: "lastBillCycleDate"
    type: "date-time"
    description: ""

  - name: "lastBillDate"
    type: "date-time"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nextBillCycleDate"
    type: "date-time"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---
