---
tap: "netsuite"
version: "1.0"

name: "SalesTaxItem"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/salestaxitem.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/SalesTaxItem.json"
description: |
  The `{{ table.name }}` table contains info about the sales tax items in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Tax Items"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "sales-tax-item-id"

  - name: "available"
    type: "varies"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "county"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "displayName"
    type: "string"
    description: ""

  - name: "eccode"
    type: "boolean, string"
    description: ""

  - name: "effectiveFrom"
    type: "date-time"
    description: ""

  - name: "excludeFromTaxReports"
    type: "boolean, string"
    description: ""

  - name: "exempt"
    type: "boolean, string"
    description: ""

  - name: "export"
    type: "boolean, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "includeChildren"
    type: "boolean, string"
    description: ""

  - name: "isDefault"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "itemId"
    type: "string"
    description: ""

  - name: "nexusCountry"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "purchaseAccount"
    type: "varies"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "reverseCharge"
    type: "boolean, string"
    description: ""

  - name: "saleAccount"
    type: "varies"
    description: ""

  - name: "service"
    type: "boolean, string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "taxAccount"
    type: "varies"
    description: ""

  - name: "taxAgency"
    type: "varies"
    description: ""

  - name: "taxType"
    type: "varies"
    description: ""

  - name: "validUntil"
    type: "date-time"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---