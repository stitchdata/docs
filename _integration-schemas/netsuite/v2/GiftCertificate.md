---
tap: netsuite
version: "2"
name: GiftCertificate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/GiftCertificate.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/GiftCertificate
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: email
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: amountRemaining
  type: string, number
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
- name: sender
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: giftCertCode
  type: string
  description: ""
- name: createdDate
  type: string
  description: ""
- name: originalAmount
  type: string, number
  description: ""
- name: expirationDate
  type: string
  description: ""
- name: message
  type: string
  description: ""
