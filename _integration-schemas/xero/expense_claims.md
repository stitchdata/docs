---
tap: "xero"
version: "1.0"

name: "expense_claims"
doc-link: &api-doc https://developer.xero.com/documentation/api/expense-claims
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/expense_claims.json
description: |
  The `{{ table.name }}` table contains info about expense claims.

replication-method: "Key-based Incremental"

api-method:
  name: getExpenseClaims
  doc-link: *api-doc

attributes:
  - name: "ExpenseClaimID"
    type: "string"
    primary-key: true
    description: "The expense claim ID."
    # foreign-key-id: "expense-claim-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date when the expense claim was last updated, in UTC."

  - name: "User"
    type: ""
    description: |
      Details about the user(s) who submitted the expense claim.

      {{ integration.subtable-note | flatify | replace:"table_name","users" }}

  - name: "Receipts"
    type: ""
    description: |
      Details about the receipt(s) associated with the expense claim.

      {{ integration.subtable-note | flatify | replace:"table_name","receipts" }}

  - name: "Payments"
    type: ""
    description: |
      Details about the payment(s) associated with the expense claim.

      {{ integration.subtable-note | flatify | replace:"table_name","payments" }}

  - name: "Status"
    type: "string"
    description: |
      The current status of the expense claim. Possible values are:

      - `SUBMITTED`
      - `AUTHORISED`
      - `PAID`

  - name: "Total"
    type: "number"
    description: "The total of the expense claim being paid."

  - name: "AmountDue"
    type: "number"
    description: "The amount due to be paid for the expense claim."

  - name: "AmountPaid"
    type: "number"
    description: "The amount still to pay for an expense claim."

  - name: "PaymentDueDate"
    type: "date-time"
    description: "The date when the expense claim is due to be paid."

  - name: "ReportingDate"
    type: "date-time"
    description: "The date when the expense claim will be reported in Xero."
---