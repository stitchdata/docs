---
tap: "netsuite-suite-analytics"
version: "1"
key: "budget"

name: "budget"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/budget.html"
description: |
  The `{{ table.name }}` table contains info about the budgets in your {{ integration.display_name }} account. A budget records the expected values of income and expenses for your business. Budgets can be created for specific customers, items, departments, classes, locations, or any combination of these criteria. 

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "budget_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The budget ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "budget-id"

  - name: "account_id"
    type: "integer"
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "accounting_book_id"
    type: "integer"
    description: "The accounting book ID."
    foreign-key-id: "accounting-book-id"

  - name: "accounting_period_id"
    type: "integer"
    description: "The accounting period."
    foreign-key-id: "accounting-period-id"

  - name: "amount"
    type: "number"
    description: "The budget amount."

  - name: "budget_date"
    type: "date-time"
    description: "The date of the budget."

  - name: "category_id"
    type: "integer"
    description: "The budget category ID."
    foreign-key-id: "budget-category-id"

  - name: "class_id"
    type: "integer"
    description: "The class of the budget."
    foreign-key-id: "class-id"

  - name: "customer_id"
    type: "integer"
    description: "The customer associated with the budget."
    foreign-key-id: "customer-id"

  - name: "department_id"
    type: "integer"
    description: "The department associated with the budget."
    foreign-key-id: "department-id"

  - name: "item_id"
    type: "integer"
    description: "The item associated with the budget."
    foreign-key-id: "item-id"

  - name: "location_id"
    type: "integer"
    description: "The location associated with the budget."
    foreign-key-id: "location-id"

  - name: "subsidiary_id"
    type: "integer"
    description: "The subsidiary associated with the budget."
    foreign-key-id: "subsidiary-id"
---