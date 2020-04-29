---
tap: "zuora"
version: "1"

name: "journalEntryItem"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Summary-Journal-Entries
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about journal entry items.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The journal entry item ID."
    foreign-key-id: "journal-entry-item-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the journal entry item was last updated."

  - name: "accountingCodeId"
    type: "string"
    description: "The accounting code associated with the journal entry item."
    foreign-key-id: "accounting-code"

  - name: "accountingCodeType"
    type: "string"
    description: |
      The type of the accounting code associated with the journal entry item. Possible values are:

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

  - name: "amount"
    type: "double"
    description: "The amount of the journal entry item in the transaction currency."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the journal entry item."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the journal entry item was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "journalEntryId"
    type: "string"
    description: "The ID of the journal entry associated with the journal entry item."
    foreign-key-id: "journal-entry-id"

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the journal entry item."
    foreign-key-id: "journal-run-id"

  - name: "type"
    type: "string"
    description: "The type of journal entry item."

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the journal entry item."
---