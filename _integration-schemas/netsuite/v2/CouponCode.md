---
tap: "netsuite"
version: "2"
name: CouponCode
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CouponCode.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/CouponCode
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: useCount
  type: string, integer
  description: ""
- name: recipient
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: dateSent
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: code
  type: string
  description: ""
- name: promotion
  type: varies
  description: ""
- name: used
  type: boolean, string
  description: ""
---