---
tap: "codat"
version: "1"
key: "bank-statement-line"

name: "bank_statement_lines"
doc-link: "https://docs.codat.io/docs/bank-transactions"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/bank_statement_lines.json"
description: |
  The `{{ table.name }}` table contains info about lines included in bank statements.

replication-method: "Full Table"

api-method:
  name: "List bank statements for a company"
  doc-link: "https://docs.codat.io/reference/bankstatements#bankstatements_listpaged"

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

  - name: "_lineIndex"
    type: "integer"
    primary-key: true
    description: "The index of the line in the bank statement."

  - name: "amount"
    type: "number"
    description: ""

  - name: "balance"
    type: "number"
    description: ""

  - name: "date"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "reconciled"
    type: "boolean"
    description: ""
---