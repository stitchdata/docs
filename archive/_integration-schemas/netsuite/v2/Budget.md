---
tap: "netsuite"
version: "2"
name: Budget
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Budget.html
description: |
  The `{{ table.name }}` table contains info about the budgets in your {{ integration.display_name }} account. A budget records the expected values of income and expenses for your business. Budgets can be created for specific customers, items, departments, classes, locations, or any combination of these criteria. 

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "budget"

replication-method: "Full Table"

attributes:
- name: category
  type: varies
  description: ""
- name: amount
  type: string, number
  description: ""
- name: department
  type: varies
  description: ""
- name: periodAmount5
  type: string, number
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: accountingBook
  type: string, number
  description: ""
- name: periodAmount14
  type: string, number
  description: ""
- name: periodAmount2
  type: string, number
  description: ""
- name: periodAmount6
  type: string, number
  description: ""
- name: periodAmount3
  type: string, number
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: periodAmount23
  type: string, number
  description: ""
- name: item
  type: varies
  description: ""
- name: periodAmount22
  type: string, number
  description: ""
- name: periodAmount16
  type: string, number
  description: ""
- name: periodAmount4
  type: string, number
  description: ""
- name: periodAmount9
  type: string, number
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: periodAmount10
  type: string, number
  description: ""
- name: periodAmount17
  type: string, number
  description: ""
- name: customer
  type: varies
  description: ""
- name: periodAmount18
  type: string, number
  description: ""
- name: account
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: year
  type: varies
  description: ""
- name: periodAmount8
  type: string, number
  description: ""
- name: periodAmount12
  type: string, number
  description: ""
- name: periodAmount24
  type: string, number
  description: ""
- name: periodAmount13
  type: string, number
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: periodAmount1
  type: string, number
  description: ""
- name: budgetType
  type: varies
  description: ""
- name: periodAmount19
  type: string, number
  description: ""
- name: periodAmount20
  type: string, number
  description: ""
- name: periodAmount7
  type: string, number
  description: ""
- name: location
  type: varies
  description: ""
- name: periodAmount15
  type: string, number
  description: ""
- name: periodAmount11
  type: string, number
  description: ""
- name: periodAmount21
  type: string, number
  description: ""
---