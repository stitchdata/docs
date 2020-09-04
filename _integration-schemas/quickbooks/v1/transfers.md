---
tap: "quickbooks"
version: "1"
key: "transfer"

name: "transfers"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/transfer"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/transfers.json"
description: |
  The `{{ table.name }}` table contains info about account transfers from your company's {{ integration.display_name }} chart of accounts.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a transfer"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/transfer#query-a-transfer"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The transfer ID."
    foreign-key-id: "transfer-id"

  - name: "Amount"
    type: "decimal"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the transfer is in."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
    description: ""

  - name: "FromAccountRef"
    type: "object"
    description: "Details about the account the funds were transferred from."
    subattributes: &account-attributes
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

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

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "ToAccountRef"
    type: "object"
    description: ""
    subattributes: *account-attributes

  - name: "TxnDate"
    type: "date-time"
    description: ""
---