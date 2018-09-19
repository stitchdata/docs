---
tap: "harvest"
version: "1.0"

name: "expense_categories"
doc-link: http://help.getharvest.com/api-v1/expenses-api/expenses/expense-categories/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/expense_categories.json
description: |
  The `expense_categories` table contains info about the expense categories in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: showAllCategories
  doc-link: http://help.getharvest.com/api-v1/expenses-api/expenses/expense-categories/#show-all-categories

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The expense category ID."

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

  - name: "created_at"
    type: "date-time"
    description: "The time the expense category was created."

  - name: "deactivated"
    type: "boolean"
    description: "Indicates if the expense category has been deactivated."
---