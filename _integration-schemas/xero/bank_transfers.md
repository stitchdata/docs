---
tap: "xero"
version: "1.0"

name: "bank_transfers"
doc-link: &api-doc https://developer.xero.com/documentation/api/bank-transfers
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/bank_transfers.json
description: |
  The `{{ table.name }}` table contains info about bank transfers. 

replication-method: "Key-based Incremental"

api-method:
  name: getBankTransfers
  doc-link: *api-doc

attributes:
  - name: "BankTransferID"
    type: "string"
    primary-key: true
    description: "The bank transfer ID."
    # foreign-key-id: "bank-transfer-id"

  - name: "CreatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the bank transfer was created, in UTC."

  - name: "FromBankAccount"
    type: "object"
    description: |
      Details about the source bank account.
    subattributes:
      - description: &accounts-table |
          This will contain the same attributes as the `accounts` table. Refer to the [`accounts`](#accounts) table schema for details.

  - name: "ToBankAccount"
    type: "object"
    description: |
      Details about the destination bank account.
    subattributes:
      - description: *accounts-table

  - name: "Amount"
    type: "number"
    description: "The amount that was transferred."

  - name: "Date"
    type: "string"
    description: "The date of the transfer."

  - name: "DateString"
    type: "date-time"
    description: "The date of the transfer."

  - name: "CurrencyRate"
    type: "number"
    description: "The currency rate of the transfer."

  - name: "FromBankTransactionID"
    type: "string"
    description: "The bank transaction ID for the source account."
    foreign-key-id: "bank-transaction-id"

  - name: "ToBankTransactionID"
    type: "string"
    description: "The bank transaction ID for the destination account."
    foreign-key-id: "bank-transaction-id"

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the bank transfer has an attachment."

  - name: "CreatedDateUTCString"
    type: "date-time"
    description: "The date the bank transfer was created."
---