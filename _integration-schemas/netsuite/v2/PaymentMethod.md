---
tap: "netsuite"
version: "2"
name: PaymentMethod
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PaymentMethod.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/PaymentMethod
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: payPalEmailAddress
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: visualsList
  type: varies
  description: ""
- name: account
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: merchantAccountsList
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: expressCheckoutArrangement
  type: string
  description: ""
- name: creditCard
  type: boolean, string
  description: ""
- name: undepFunds
  type: boolean, string
  description: ""
- name: isDebitCard
  type: boolean, string
  description: ""
- name: useExpressCheckout
  type: boolean, string
  description: ""
---