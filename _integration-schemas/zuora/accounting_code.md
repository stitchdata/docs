---
tap: "zuora"
version: "1"

name: "accountingCode"
doc-link: https://live-www.zuora.com/developer/api-reference/#operation/GET_AllAccountingCodes
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about the accounting codes in your {{ integration.display_name }} instance. Accounting codes are used to categorize transactions for accounting purposes.

  **Note**: To replicate this table, you must have {{ integration.display_name }} Finance enabled.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The accounting code ID."
    foreign-key: "accounting-code-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the accounting code was last updated."

  - name: "category"
    type: "string"
    description: |
      The category associated with the accounting code. Possible values are:

      - `Assets`
      - `Liabilities`
      - `Equity`
      - `Revenue`
      - `Expenses`

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the accounting code."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the accounting code was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "glAccountName"
    type: "string"
    description: "The name of the account in your general ledger."

  - name: "glAccountNumber"
    type: "string"
    description: "The account number in your general ledger."

  - name: "name"
    type: "string"
    description: "The name of the accounting code."

  - name: "notes"
    type: "string"
    description: "Additional notes about the accounting code."

  - name: "status"
    type: "string"
    description: |
      The status of the accounting code. Possible values are:

      - `Active`
      - `Inactive`

  - name: "type"
    type: "string"
    description: |
      The accounting code type. Possible values are:

      - `AccountsReceivable`
      - `On-Account Receivable`
      - `Cash`
      - `OtherAssets`
      - `CustomerCashOnAccount`
      - `DeferredRevenue`
      - `SalesTaxPayable`
      - `OtherLiabilities`
      - `SalesRevenue`
      - `SalesDiscounts`
      - `OtherRevenue`
      - `OtherEquity`
      - `BadDebt`
      - `OtherExpenses`

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the accounting code."
---