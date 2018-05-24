---
tap: "zuora"
version: 1.0

name: "accountingPeriod"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Accounting-Periods
#singer-schema: 
description: |
  The `accountingPeriod` table contains information about the [accounting periods](https://knowledgecenter.zuora.com/CC_Finance/E_Accounting_Periods) in your Zuora account.

  **Note**: To replicate this table, you must have Zuora Finance enabled.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The accounting period ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the accounting period was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the accounting period."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the accounting period was created."

  - name: "endDate"
    type: "date-time"
    description: "The end date of the accounting period."

  - name: "fiscalQuarter"
    type: "string"
    description: "The fiscal quarter of the accounting period."

  - name: "fiscalYear"
    type: "string"
    description: "The fiscal year of the accounting period."

  - name: "name"
    type: "string"
    description: "The name of the accounting period."

  - name: "notes"
    type: "string"
    description: "Additional notes about the accounting period."

  - name: "runTrialBalanceEnd"
    type: "date-time"
    description: "The date that the trial balance was completed."

  - name: "runTrialBalanceErrorMessage"
    type: "string"
    description: "If the `runTrialBalanceStatus` field has an `Error` value, this field will contain the error message for the error."

  - name: "runTrialBalanceStart"
    type: "date-time"
    description: "The date that the trial balance was run."

  - name: "runTrialBalanceStatus"
    type: "string"
    description: |
      The status of the trial balance for the accounting period. Possible values are:

      - `Pending`
      - `Processing`
      - `Completed`
      - `Error`

  - name: "startDate"
    type: "date-time"
    description: "The start date of the accounting period."

  - name: "status"
    type: "string"
    doc-link: https://knowledgecenter.zuora.com/CC_Finance/E_Accounting_Periods#Accounting_Period_Statuses
    description: |
      The status of the accounting period. Possible values are:

      - `Open`
      - `PendingClose`
      - `Closed`

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the accounting period."
---