---
tap: "harvest"
version: "2"

name: "expenses"
doc-link: https://help.getharvest.com/api-v2/expenses-api/expenses/expenses/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/expenses.json
description: |
  The `expenses` table contains info about the expenses recorded in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all expenses
  doc-link: https://help.getharvest.com/api-v2/expenses-api/expenses/expenses#list-all-expenses

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The expense ID."
    # foreign-key-id: "expense-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the expense was updated."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client associated with the expense."
    foreign-key-id: "client-id"

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the expense."
    foreign-key-id: "project-id"

  - name: "expense_category_id"
    type: "integer"
    description: "The ID of the category associated with the expense."
    foreign-key-id: "expense-category-id"

  - name: "user_id"
    type: "integer"
    description: "The ID of the user that recorded the expense."
    foreign-key-id: "user-id"

  - name: "user_assignment_id"
    type: "integer"
    description: "The user assignment ID."

  - name: "receipt_url"
    type: "string"
    description: "The URL of the receipt associated with the expense."

  - name: "receipt_file_name"
    type: "string"
    description: "The file name of the receipt."

  - name: "receipt_file_size"
    type: "integer"
    description: "The size of the receipt file."

  - name: "receipt_content_type"
    type: "string"
    description: "The content type of the receipt file."

  - name: "invoice_id"
    type: "integer"
    description: "The ID of the invoice associated with the expense."
    foreign-key-id: "invoice-id"

  - name: "notes"
    type: "string"
    description: "Notes used to describe the expense."

  - name: "billable"
    type: "boolean"
    description: "If `true`, the expense is billable."

  - name: "is_closed"
    type: "boolean"
    description: "If `true`, the expense has been closed."

  - name: "is_locked"
    type: "boolean"
    description: "If `true`, the expense has either been invoiced, approved, or the person/project related to the expense is archived."

  - name: "is_billed"
    type: "boolean"
    description: "If `true`, the expense has been marked as invoiced."

  - name: "locked_reason"
    type: "string"
    description: "The explanation for why the expense has been locked."

  - name: "spent_date"
    type: "date-time"
    description: "The date the expense occurred."

  - name: "created_at"
    type: "date-time"
    description: "The time the expense was created."

  - name: "total_cost"
    type: "number"
    description: "The total cost of the expense."

  - name: "units"
    type: "number"
    description: "The number of units contained in the expense, if calculated by unit price. Ex: `40` (miles)"
---