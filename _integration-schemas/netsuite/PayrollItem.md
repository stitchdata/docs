---
tap: "netsuite"
version: "1.0"

name: "PayrollItem"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/payrollitem.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PayrollItem.json"
description: |
  The `{{ table.name }}` table contains info about the payroll items, or payroll transaction line items, in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Payroll Items"

feature-requirements:
  - tab: "Employees"
    name: "Payroll"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "payroll-item-id"

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "employeePaid"
    type: "boolean, string"
    description: ""

  - name: "expenseAccount"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "inactive"
    type: "boolean, string"
    description: ""

  - name: "itemType"
    type: "varies"
    description: ""

  - name: "liabilityAccount"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "vendor"
    type: "varies"
    description: ""
---