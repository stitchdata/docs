---
tap: "zuora"
version: "1"

name: "journalRun"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Journal-Runs
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about journal runs.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The journal run ID."
    foreign-key-id: "journal-run-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the journal run was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the journal run."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the journal run was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "executedOn"
    type: "date-time"
    description: "The date the journal run was executed."

  - name: "number"
    type: "string"
    description: "The number of the journal run."

  - name: "segmentationRuleName"
    type: "string"
    description: "The name of the GL segmentation rule used in the journal run."

  - name: "status"
    type: "string"
    description: |
      The status of the journal run. Possible values are:

      - `Pending`
      - `Processing`
      - `Completed`
      - `Error`
      - `CancelInProgress`
      - `Cancelled`
      - `DeleteInProgress`

  - name: "targetEndDate"
    type: "date-time"
    description: "The target end date of the journal run."

  - name: "targetStartDate"
    type: "date-time"
    description: "The target start date of the journal run."

  - name: "totalJournalEntryCount"
    type: "integer"
    description: "The total number of journal entries in the journal run."

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the journal run."
---