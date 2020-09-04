---
tap: "quickbooks"
version: "1"
key: "tax-agency"

name: "tax_agencies"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxagency"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/tax_agencies.json"
description: |
  The `{{ table.name }}` table contains info about the tax-collecting entites defined in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a tax agency"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxagency/#query-a-taxagency"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The tax agency ID."
    foreign-key-id: "tax-agency-id"

  - name: "DisplayName"
    type: "string"
    description: ""

  - name: "domain"
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

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TaxTrackedOnPurchases"
    type: "boolean"
    description: ""

  - name: "TaxTrackedOnSales"
    type: "boolean"
    description: ""
---