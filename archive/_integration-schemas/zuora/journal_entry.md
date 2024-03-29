---
tap: "zuora"
version: "1"

name: "journalEntry"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Accounts
#
description: |
  The `{{ table.name }}` table contains information about 

replication-method: "Key-based Incremental"


attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The journal entry ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the journal entry was last updated."

  - name: "accountingPeriodId"
    type: "string"
    description: "The ID of the accounting period associated with the journal entry."
    foreign-key: true

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the journal entry."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the journal entry was created."

  - name: "currency"
    type: "string"
    description: "The currency the journal entry is in."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "journalEntryDate"
    type: "date-time"
    description: "The date of the journal entry."

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the journal entry."
    foreign-key-id: "journal-run-id"

  - name: "notes"
    type: "string"
    description: "Additional info about the journal entry."

  - name: "number"
    type: "string"
    description: "The number of the journal entry in the format `JE-XXXXXXXX`. For example: `JE-00000001`"

  - name: "status"
    type: "string"
    description: |
      The status of the journal entry. Possible values are:

      - `Created`
      - `Cancelled`

  # - name: "transactionCount"
  #   type: 
  #   description: 

  # - name: "transactionType"
  #   type: "string"
  #   description: 

  - name: "transferDate"
    type: "date-time"
    description: "The date that the value of `transferredToAccounting` changed to `Yes`. This field will be `NULL` otherwise."

  - name: "transferredBy"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who changed the value of `transferredToAccounting` to `Yes`. This field will be `NULL` otherwise."
---