---
tap: "codat"
version: "1"
key: "bank-account"

name: "bank_accounts"
doc-link: "https://docs.codat.io/docs/bank-accounts"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/bank_accounts.json"
description: |
  The `{{ table.name }}` table contains informaiton about bank accounts for a given company in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "getBankAccounts"
  doc-link: "https://docs.codat.io/reference/bankaccounts#bankaccounts_listaccountspaged"

attributes:
  - name: "accountName"
    type: "string"
    primary-key: true
    description: "The account name."
    foreign-key-id: "account-name"

  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "connectionId"
    type: "string"
    primary-key: true
    description: "The connection ID."  
    foreign-key-id: "connection-id"
    
  - name: "accountNumber"
    type: "string"
    description: ""
    
  - name: "availableBalance"
    type: "number"
    description: ""

  - name: "balance"
    type: "number"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "fromDate"
    type: "string"
    description: ""

  - name: "iban"
    type: "string"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "modifiedDate"
    type: "string"
    description: ""

  - name: "overdraftLimit"
    type: "number"
    description: ""

  - name: "sortCode"
    type: "string"
    description: ""

  - name: "sourceModifiedDate"
    type: "string"
    description: ""

  - name: "toDate"
    type: "string"
    description: ""
---