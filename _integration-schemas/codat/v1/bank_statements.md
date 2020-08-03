---
tap: "codat"
version: "1"
key: "bank-statement"

name: "bank_statements"
doc-link: "https://docs.codat.io/docs/bank-accounts"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/bank_statements.json"
description: |
  The `{{ table.name }}` table contains info about bank statement report data for a company over a time period.

replication-method: "Key-based Incremental"

replication-key:
  name: "modifiedDate"

api-method:
  name: "List bank statements for a company"
  doc-link: "https://docs.codat.io/reference/bankstatements#bankstatements_listpaged"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The bank statement ID."
    #foreign-key-id: "bank-statement-id"

  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the account."
    foreign-key-id: "company-id"

  - name: "accountName"
    type: "string"
    description: "The name of the bank account."

  - name: "accountNumber"
    type: "string"
    description: "The account number for the bank account."

  - name: "availableBalance"
    type: "number, string"
    description: "The total available balance of the bank account, as reported by the underlying data source."

  - name: "balance"
    type: "number, string"
    description: "The balance of the bank account."

  - name: "currency"
    type: "string"
    description: "The currency of the bank account."

  - name: "details"
    type: "array"
    description: "Details about the transactions contained in the bank statement."
    subattributes:
      - name: "amount"
        type: "number"
        description: "The amount of the line item."

      - name: "balance"
        type: "number"
        description: "The current balance of the bank account, with the line item accounted for."

      - name: "date"
        type: "date-time"
        description: "The date of the transaction."

      - name: "description"
        type: "string"
        description: "A description of the transaction."

      - name: "id"
        type: "string"
        description: "The ID for the bank transaction."

      - name: "reconciled"
        type: "boolean"
        description: "Indicates if the bank account has been reconciled with the accounting platform or not."

  - name: "fromDate"
    type: "date-time"
    description: ""

  - name: "iban"
    type: "string"
    description: "The international bank account number of the account."

  - name: "sortCode"
    type: "string"
    description: "The sort code for the bank account."

  - name: "toDate"
    type: "date-time"
    description: ""
---