---
tap: "quickbooks"
version: "1"
key: "account"

name: "accounts"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about the various account types in you {{ integration.display_name }} instance. This table includes all account types: asset, liability, revenue (income), expenses, and equity.

  **Note**: Both active and inactive accounts are included in the data for this table.
 
replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query an account"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account#query-an-account"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "AccountSubType"
    type: "string"
    description: ""

  - name: "AccountType"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "Classification"
    type: "string"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency used for the account."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "CurrentBalance"
    type: "decimal"
    description: ""

  - name: "CurrentBalanceWithSubAccounts"
    type: "decimal"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "FullyQualifiedName"
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

  - name: "ParentRef"
    type: "object"
    description: "If the account is a subaccount, this object will contain the ID of the parent account."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the parent account."
        foreign-key-id: "account-id"

  - name: "SubAccount"
    type: "boolean"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---