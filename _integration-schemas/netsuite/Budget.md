---
tap: "netsuite"
version: "1.0"

name: "Budget"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/budget.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Budget.json"
description: |
  The `{{ table.name }}` table contains info about the budgets in your {{ integration.display_name }} account. A budget records the expected values of income and expenses for your business. Budgets can be created for specific customers, items, departments, classes, locations, or any combination of these criteria. 

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "budget"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "budget-id"

  - name: "_class"
    type: "varies"
    description: ""

  - name: "account"
    type: "varies"
    description: ""

  - name: "amount"
    type: "number, string"
    description: ""

  - name: "budgetType"
    type: "varies"
    description: ""

  - name: "category"
    type: "varies"
    description: ""

  - name: "currency"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "location"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "periodAmount1"
    type: "number, string"
    description: ""

  - name: "periodAmount10"
    type: "number, string"
    description: ""

  - name: "periodAmount11"
    type: "number, string"
    description: ""

  - name: "periodAmount12"
    type: "number, string"
    description: ""

  - name: "periodAmount13"
    type: "number, string"
    description: ""

  - name: "periodAmount14"
    type: "number, string"
    description: ""

  - name: "periodAmount15"
    type: "number, string"
    description: ""

  - name: "periodAmount16"
    type: "number, string"
    description: ""

  - name: "periodAmount17"
    type: "number, string"
    description: ""

  - name: "periodAmount18"
    type: "number, string"
    description: ""

  - name: "periodAmount19"
    type: "number, string"
    description: ""

  - name: "periodAmount2"
    type: "number, string"
    description: ""

  - name: "periodAmount20"
    type: "number, string"
    description: ""

  - name: "periodAmount21"
    type: "number, string"
    description: ""

  - name: "periodAmount22"
    type: "number, string"
    description: ""

  - name: "periodAmount23"
    type: "number, string"
    description: ""

  - name: "periodAmount24"
    type: "number, string"
    description: ""

  - name: "periodAmount3"
    type: "number, string"
    description: ""

  - name: "periodAmount4"
    type: "number, string"
    description: ""

  - name: "periodAmount5"
    type: "number, string"
    description: ""

  - name: "periodAmount6"
    type: "number, string"
    description: ""

  - name: "periodAmount7"
    type: "number, string"
    description: ""

  - name: "periodAmount8"
    type: "number, string"
    description: ""

  - name: "periodAmount9"
    type: "number, string"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "year"
    type: "varies"
    description: ""
---