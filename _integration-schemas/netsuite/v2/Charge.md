---
tap: "netsuite"
version: "2"
name: Charge
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Charge.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Charge
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: description
  type: string
  description: ""
- name: timeRecord
  type: varies
  description: ""
- name: amount
  type: string, number
  description: ""
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: stage
  type: varies
  description: ""
- name: billTo
  type: varies
  description: ""
- name: billingAccount
  type: varies
  description: ""
- name: chargeDate
  type: string
  description: ""
- name: use
  type: varies
  description: ""
- name: transactionLine
  type: varies
  description: ""
- name: rule
  type: varies
  description: ""
- name: billingItem
  type: varies
  description: ""
- name: transaction
  type: varies
  description: ""
- name: rate
  type: string
  description: ""
- name: chargeType
  type: varies
  description: ""
- name: subscriptionLine
  type: varies
  description: ""
- name: invoice
  type: varies
  description: ""
- name: currency
  type: varies
  description: ""
- name: invoiceLine
  type: varies
  description: ""
- name: runId
  type: string
  description: ""
- name: projectTask
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: salesOrderLine
  type: varies
  description: ""
- name: salesOrder
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: quantity
  type: string, number
  description: ""
- name: location
  type: varies
  description: ""
---