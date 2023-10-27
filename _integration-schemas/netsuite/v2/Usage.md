---
tap: "netsuite"
version: "2"
name: Usage
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Usage.html
description: |
  The `{{ table.name }}` table contains info about the subscription billing lines in your {{ integration.display_name }} account. For example: Money, time, cellular data, internet data, etc.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "usage"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: usageQuantity
  type: string, number
  description: ""
- name: item
  type: varies
  description: ""
- name: usageSubscription
  type: varies
  description: ""
- name: usageDate
  type: string
  description: ""
- name: customer
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: usageSubscriptionLine
  type: varies
  description: ""
- name: subscriptionPlan
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
---