---
tap: "netsuite"
version: "1.0"

name: "Subsidiary"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/subsidiary.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Subsidiary.json"
description: |
  The `{{ table.name }}` table contains info about the subsidiary records in your {{ integration.display_name }} account. A subsidiary represents a separate company within your global organization.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "subsidiary"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "subsidiary-id"

  - name: "accountingBookDetailList"
    type: "varies"
    description: ""

  - name: "addrLanguage"
    type: "string"
    description: ""

  - name: "allowPayroll"
    type: "boolean, string"
    description: ""

  - name: "checkLayout"
    type: "varies"
    description: ""

  - name: "classTranslationList"
    type: "varies"
    description: ""

  - name: "consol"
    type: "string"
    description: ""

  - name: "country"
    type: "varies"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "inboundEmail"
    type: "string"
    description: ""

  - name: "interCoAccount"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "mainAddress"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nexusList"
    type: "varies"
    description: ""

  - name: "nonConsol"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "pageLogo"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "shippingAddress"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "taxRegistrationList"
    type: "varies"
    description: ""

  - name: "tranPrefix"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---