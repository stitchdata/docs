---
tap: "quickbooks"
version: "1"
key: "payment-method"

name: "payment_methods"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/paymentmethod"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/payment_methods.json"
description: |
  The `{{ table.name }}` table contains info about the methods of payment your company receives for goods. **Note**: Both active and inactive payment methods are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a payment method"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/paymentmethod/#query-a-paymentmethod"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The payment method ID."
    foreign-key-id: "payment-method-id"

  - name: "Active"
    type: "boolean"
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

  - name: "Name"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "Type"
    type: "string"
    description: ""
---