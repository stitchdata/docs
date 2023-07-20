---
tap: "netsuite"
version: "2"
name: Paycheck
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Paycheck.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Paycheck
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: department
  type: varies
  description: ""
- name: address
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: postingPeriod
  type: varies
  description: ""
- name: periodEnding
  type: string
  description: ""
- name: userAmount
  type: string, number
  description: ""
- name: payTimeList
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
- name: paySummaryList
  type: varies
  description: ""
- name: account
  type: varies
  description: ""
- name: batchNumber
  type: string
  description: ""
- name: payContribList
  type: varies
  description: ""
- name: balance
  type: string, number
  description: ""
- name: payPtoList
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: payDisburseList
  type: varies
  description: ""
- name: payEarnList
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: tranDate
  type: string
  description: ""
- name: payTaxList
  type: varies
  description: ""
- name: tranId
  type: string
  description: ""
- name: payExpList
  type: varies
  description: ""
- name: location
  type: varies
  description: ""
- name: entity
  type: varies
  description: ""
- name: payDeductList
  type: varies
  description: ""
- name: workplace
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
- name: payFrequency
  type: string
  description: ""
---