---
tap: "codat"
version: "1"
key: "tax-rate"

name: "tax_rates"
doc-link: "https://docs.codat.io/reference/taxrates"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/tax_rates.json"
description: |
  The {{ table.name }} table contains information about tax rates for a given company in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get tax rates"
  doc-link: "https://docs.codat.io/reference/taxrates#taxrates_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The tax rate ID."
    foreign-key-id: "tax-id"

  - name: "modifiedDate"
    type: "string"
    description: "The date the tax rate was last modified."
    replication-key: true

  - name: "code"
    type: "string"
    description: ""

  - name: "components"
    type: "array"
    description: ""
    subattributes:
      - name: "isCompound"
        type: "boolean"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "rate"
        type: "number"
        description: ""

  - name: "effectiveTaxRate"
    type: "number"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""

  - name: "sourceModifiedDate"
    type: "string"
    description: ""

  - name: "totalTaxRate"
    type: "number"
    description: ""
---