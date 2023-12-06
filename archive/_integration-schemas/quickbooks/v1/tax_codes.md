---
tap: "quickbooks"
version: "1"
key: "tax-code"

name: "tax_codes"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxcode"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/tax_codes.json"
description: |
  The `{{ table.name }}` table contains info about the tax codes defined in your {{ integration.display_name }} instance. **Note**: Both active and inactive tax codes are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a tax code"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxcode"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The tax code ID."
    foreign-key-id: "tax-code-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "Description"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "Hidden"
    type: "boolean"
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

  - name: "PurchaseTaxRateList"
    type: "object"
    description: ""
    subattributes: &tax-rate-detail
      - name: "TaxRateDetail"
        type: "array"
        description: ""
        subattributes:
          - name: "TaxOrder"
            type: "integer"
            description: ""

          - name: "TaxRateRef"
            type: "object"
            description: "Details about the tax rate associated with the tax code."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: "The tax rate ID."
                foreign-key-id: "tax-rate-id"

          - name: "TaxTypeApplicable"
            type: "string"
            description: ""

  - name: "SalesTaxRateList"
    type: "object"
    description: ""
    subattributes: *tax-rate-detail

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TaxGroup"
    type: "boolean"
    description: ""

  - name: "Taxable"
    type: "boolean"
    description: ""
---