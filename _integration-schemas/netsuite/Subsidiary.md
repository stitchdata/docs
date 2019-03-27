---
tap: "netsuite"
# version: "1.0"

name: "Subsidiary"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Subsidiary.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "accountingBookDetailList"
    type: "anything"
    description: ""

  - name: "addrLanguage"
    type: "string"
    description: ""

  - name: "allowPayroll"
    type: "boolean, string"
    description: ""

  - name: "checkLayout"
    type: "anything"
    description: ""

  - name: "classTranslationList"
    type: "anything"
    description: ""

  - name: "consol"
    type: "string"
    description: ""

  - name: "country"
    type: "anything"
    description: ""

  - name: "currency"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "edition"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "federalIdNumber"
    type: "string"
    description: ""

  - name: "fiscalCalendar"
    type: "anything"
    description: ""

  - name: "inboundEmail"
    type: "string"
    description: ""

  - name: "interCoAccount"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isElimination"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "legalName"
    type: "string"
    description: ""

  - name: "logo"
    type: "anything"
    description: ""

  - name: "mainAddress"
    type: "anything"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nexusList"
    type: "anything"
    description: ""

  - name: "nonConsol"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "pageLogo"
    type: "anything"
    description: ""

  - name: "parent"
    type: "anything"
    description: ""

  - name: "purchaseOrderAmount"
    type: "number, string"
    description: ""

  - name: "purchaseOrderQuantity"
    type: "number, string"
    description: ""

  - name: "purchaseOrderQuantityDiff"
    type: "number, string"
    description: ""

  - name: "receiptAmount"
    type: "number, string"
    description: ""

  - name: "receiptQuantity"
    type: "number, string"
    description: ""

  - name: "receiptQuantityDiff"
    type: "number, string"
    description: ""

  - name: "returnAddress"
    type: "anything"
    description: ""

  - name: "shippingAddress"
    type: "anything"
    description: ""

  - name: "showSubsidiaryName"
    type: "boolean, string"
    description: ""

  - name: "ssnOrTin"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "state1TaxNumber"
    type: "string"
    description: ""

  - name: "taxFiscalCalendar"
    type: "anything"
    description: ""

  - name: "taxRegistrationList"
    type: "anything"
    description: ""

  - name: "tranPrefix"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---
