---
tap: "harvest"
version: "1"

name: "expenses"
doc-link: http://help.getharvest.com/api-v1/expenses-api/expenses/add-update-expenses/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/expenses.json
description: |
  The `expenses` table contains info about the expenses recorded in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: showAnExpense
  doc-link: http://help.getharvest.com/api-v1/expenses-api/expenses/add-update-expenses/#show-an-expense

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The expense ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the expense was updated."

  - name: "total_cost"
    type: "number"
    description: "The total cost of the expense."

  - name: "units"
    type: "number"
    description: "The number of units contained in the expense, if calculated by unit price. Ex: `40` (miles)"

  - name: "created_at"
    type: "date-time"
    description: "The time the expense was created."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the expense."

  - name: "expense_category_id"
    type: "integer"
    description: "The ID of the expense category associated with the expense."
    # foreign-keys:
    #   - table: "expense_category"
    #     attribute: "id"

  - name: "user_id"
    type: "integer"
    description: "The ID of the user associated with the expense."

  - name: "spent_at"
    type: "string"
    description: "The date when the expense was entered."

  - name: "is_closed"
    type: "boolean"
    description: "Indicates if the expense has been closed."

  - name: "notes"
    type: "string"
    description: "Expense entry notes."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the expense. Note: only billable expenses can be invoiced."
    # foreign-keys:
    #   - table: "invoices"
    #     attribute: "id"

  - name: "billable"
    type: "boolean"
    description: "Indicates if the expense is billable."

  - name: "company_id"
    type: "integer"
    description: "The ID of the company associated with the expense."

  - name: "has_receipt"
    type: "boolean"
    description: "Indicates if the expense has a receipt."

  - name: "receipt_url"
    type: "string"
    description: "If `has_receipt` is `true`, this field will contain the URL of the receipt."

  - name: "is_locked"
    type: "boolean"
    description: "Indicates if the expense has been locked."

  - name: "locked_reason"
    type: "string"
    description: "If `is_locked` is `true`, this field will contain the reason the expense has been locked."
---