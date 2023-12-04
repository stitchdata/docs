---
tap: "quickbooks"
version: "1"
key: "tax-rate"

name: "tax_rates"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxrate"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/tax_rates.json"
description: |
  The `{{ table.name }}` table contains info about the tax rates defined in your {{ integration.display_name }} instance. **Note**: Both active and inactive tax rates are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a tax rate"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxrate#query-a-taxrate"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The tax rate ID."
    foreign-key-id: "tax-rate-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "AgencyRef"
    type: "object"
    description: "Details about the tax agency associated with the tax rate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tax agency ID."
        foreign-key-id: "tax-agency-id"

  - name: "Description"
    type: "string"
    description: ""

  - name: "DisplayType"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "EffectiveTaxRate"
    type: "object"
    description: ""
    subattributes:
      - name: "RateValue"
        type: "number"
        description: ""

      - name: "EndDate"
        type: "string"
        description: ""

      - name: "EffectiveDate"
        type: "string"
        description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "RateValue"
    type: "decimal"
    description: ""

  - name: "SpecialTaxType"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---