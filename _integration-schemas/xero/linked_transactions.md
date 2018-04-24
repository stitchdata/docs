---
tap: "xero"
version: "1.0"

name: "linked_transactions"
doc-link: &api-doc https://developer.xero.com/documentation/api/linked-transactions
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/linked_transactions.json
description: |
  The `linked_transactions` table contains info about linked transactions. Linked transactions are transactions where line items from a purchase transaction to a customer and a sales transaction.

# Use the UpdatedDateUTC field (formatted as an rfc3339 string) as a bookmark. Since this API endpoint does not support filtering by UpdatedDateUTC within a request, the Tap should request all data for this endpoint and filter out entries with earlier update_at values before writing out records, and write out a bookmark value corresponding to the greatest UpdatedDateUTC value it encounters.

# Unclear if this will count towards row usage. 

replication-method: "Incremental"

api-method:
  name: getLinkedTransactions
  doc-link: *api-doc

attributes:
  - name: "LinkedTransactionID"
    type: "string"
    primary-key: true
    description: "The linked transaction ID."

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the linked transaction was last updated, in UTC."

  - name: "Status"
    type: "string"
    description: |
      The status of the linked transaction, which is derived from the statuses of the source and target transactions. Possible values are:

      - `DRAFT` - The source transaction is in a draft status. The linked transaction hasn't been allocated to the target transaction.
      - `APPROVED` - The source transaction is in an authorised status. The linked transaction hasn't been allocated to the target transaction.
      - `ONDRAFT` - The linked transaction has been allocated to the target transaction in draft status.
      - `BILLED` - The linked transaction has been allocated to the target transaction in authorised status.
      - `VOIDED` - The source transaction has been voided.

  - name: "Type"
    type: "string"
    description: "The type of the linked transaction. This value will always be `BILLABLEEXPENSE`."

  - name: "SourceTransactionID"
    type: "string"
    description: |
      The ID of the source transaction, or the purchase component of a billable expense. The value this field contains varies depending on the value of `SourceTransactionTypeCode`:

      - `ACCPAY` - The source transaction was an invoice. The ID in this field will be equivalent to `invoices.InvoiceId`.
      - `SPEND` The source transaction was a bank transaction. The ID in this field will be equivalent to `bank_transaction.BankTransactionId`.

  - name: "SourceLineItemID"
    type: "string"
    description: "The ID of the associated line item from the source transaction."

  - name: "SourceTransactionTypeCode"
    type: "string"
    description: |
      The type of the source transaction. Possible values are:

      - `ACCPAY` - The source transaction was an invoice.
      - `SPEND` The source transaction was a bank transaction.

  - name: "ContactID"
    type: "string"
    description: "The ID of the contact on the target transaction, i.e. the customer that the expense is being billed to."
    foreign-key: true

  - name: "TargetTransactionID"
    type: "string"
    description: |
      The ID of the target transaction, or the sale component of a billable expense.

      **Note**: Only invoices with `Type: ACCREC` can be target transactions.
    foreign-key: true

  - name: "TargetLineItemID"
    type: "string"
    description: "The ID of the line item on the target transaction."
    foreign-key: true
---