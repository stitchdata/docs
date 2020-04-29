---
tap: "zuora"
version: "1"

name: "paymentRun"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Payment-Runs
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about payment runs.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the payment run."
    foreign-key-id: "payment-run-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the account was last updated."

  - name: "batch"
    type: "string"
    description: "The alias name given to a batch."

  - name: "billCycleDay"
    type: "string"
    description: "The day of the billing cycle, the day of the month when a bill run generates invoices for an account."

  - name: "billingRunId"
    type: "string"
    description: "The ID of the billing run associated with the payment run."
    foreign-key-id: "billing-run-id"

  - name: "completedOn"
    type: "date-time"
    description: "The date when the payment run completed."

  - name: "consolidatedPayment"
    type: "boolean"
    description: "If `true`, a single payment will be processed for all receivables due on an account."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the payment run."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the payment run was created."

  - name: "currency"
    type: "string"
    description: "The currency the payment run is in."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "executedOn"
    type: "date-time"
    description: "The date the payment run is executed."

  - name: "number"
    type: "string"
    description: "The number of the payment run."

  - name: "numberOfErrors"
    type: "integer"
    description: "The number of errors encountered by the payment run."

  - name: "numberOfInvoices"
    type: "integer"
    description: "The number of invoices processed by the payment run."

  - name: "numberOfPayments"
    type: "integer"
    description: "The number of payments processed by the payment run."

  - name: "status"
    type: "string"
    description: |
      The status for the payment run. Possible values are:

      - `Pending`
      - `Processing`
      - `Completed`
      - `Error`
      - `Canceled`

  - name: "targetDate"
    type: "date-time"
    description: "The target date of the payment run."

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the payment run."
---