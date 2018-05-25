---
tap: "zuora"
version: 1.0

name: "journalEntry"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Accounts
#singer-schema: 
description: |
  The `journalEntry` table contains information about 

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The account ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the account was last updated."

  - name: "accountingPeriodId"
    type: "string"
    description: "The ID of the accounting period associated with the journal entry."
    foreign-key: true

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the journal entry."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the journal entry was created."

  - name: "currency"
    type: "string"
    description: "The currency the journal entry is in."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "journalEntryDate"
    type: "date-time"
    description: "The date of the journal entry."

  - name: "journalRunId"
    type: "string"
    description: "The ID of the journal run associated with the journal entry."
    foreign-key: true

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
    description: "The ID of the Zuora user who changed the value of `transferredToAccounting` to `Yes`. This field will be `NULL` otherwise."

---