---
tap: "codat"
version: "1"
key: ""

name: "bank_account_transactions"
doc-link: "https://docs.codat.io/docs/bank-transactions"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/bank_account_transactions.json"
description: |
  The {{ table.name }} table contains information about transactions for a specified company and bank account in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Gets bank transactions for a given bank account ID"
    doc-link: "https://docs.codat.io/reference/bankaccounts#bankaccounts_getaccounttransactions"

attributes:
  - name: "_transactionIndex"
    type: "integer"
    primary-key: true
    description: "The transaction index number."
    foreign-key-id: "transaction-index-id"
  - name: "bankAccountId"
    type: "string"
    primary-key: true
    description: "The bank account ID."
    foreign-key-id: "bank-account-id"  
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"
      
  - name: "amount"
    type: "number"
    description: ""
  - name: "balance"
    type: "number"
    description: ""
  - name: "date"
    type: "string"
    description: ""
  - name: "description"
    type: "string"
    description: ""
  - name: "modifiedDate"
    type: "string"
    description: ""
  - name: "reconciled"
    type: "boolean"
    description: ""
  - name: "sourceModifiedDate"
    type: "string"
    description: ""
  - name: "transactionType"
    type: "string"
    description: ""
---
