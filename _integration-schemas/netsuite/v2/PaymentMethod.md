---
tap: "netsuite"
version: "2"
name: PaymentMethod
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PaymentMethod.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/PaymentMethod
description: |
  The `{{ table.name }}` table contains info about the customer payment methods in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "payment-method"

replication-method: "Full Table"

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