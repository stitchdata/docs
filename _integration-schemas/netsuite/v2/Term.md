---
tap: "netsuite"
version: "2"
name: Term
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Term.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Term
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: daysUntilExpiry
  type: string, integer
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: discountPercentDateDriven
  type: string, number
  description: ""
- name: dateDriven
  type: boolean, string
  description: ""
- name: recurrenceFrequency
  type: string
  description: ""
- name: name
  type: string
  description: ""
- name: discountPercent
  type: string, number
  description: ""
- name: repeatEvery
  type: string, integer
  description: ""
- name: percentagesList
  type: varies
  description: ""
- name: daysUntilNetDue
  type: string, integer
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: dayOfMonthNetDue
  type: string, integer
  description: ""
- name: splitEvenly
  type: boolean, string
  description: ""
- name: dueNextMonthIfWithinDays
  type: string, integer
  description: ""
- name: installment
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: preferred
  type: boolean, string
  description: ""
- name: dayDiscountExpires
  type: string, integer
  description: ""
- name: recurrenceCount
  type: string, integer
  description: ""
