---
tap: "harvest"
version: "2"

name: "expense_categories"
doc-link: https://help.getharvest.com/api-v2/expenses-api/expenses/expense-categories/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/expense_categories.json
description: |
  The `expense_categories` table contains info about the expense categories in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: List all expense categories
  doc-link: https://help.getharvest.com/api-v2/expenses-api/expenses/expense-categories/#list-all-expense-categories

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The expense category ID."
    foreign-key-id: "expense-category-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the expense category was updated."

  - name: "name"
    type: "string"
    description: "The name of the expense category."

  - name: "unit_name"
    type: "string"
    description: |
      The name of the unit associated with the expense category.

      This column will only contain values for expense categories based on unit values.

  - name: "unit_price"
    type: "number"
    description: |
      The price of the unit associated with the expense category.

      This column will only contain values for expense categories based on unit values.

  - name: "is_active"
    type: "boolean"
    description: "If `true`, the category is active."

  - name: "created_at"
    type: "date-time"
    description: "The time the expense category was created."
---