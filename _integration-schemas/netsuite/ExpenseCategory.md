---
tap: "netsuite"
version: "1.0"

name: "ExpenseCategory"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/expensecategory.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ExpenseCategory.json"
description: |
  The `{{ table.name }}` table contains info about the expense categories in your {{ integration.display_name }} account. 

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Expense Categories"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "expense-category-id"

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "defaultRate"
    type: "number, string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "expenseAcct"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "rateRequired"
    type: "boolean, string"
    description: ""

  - name: "ratesList"
    type: "varies"
    description: ""

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "translationsList"
    type: "varies"
    description: ""
---