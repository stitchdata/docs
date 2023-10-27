---
tap: "netsuite"
version: "2"
name: CouponCode
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CouponCode.html
description: |
  The `{{ table.name }}` table contains info about the coupon codes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "coupon-code"

replication-method: "Full Table"

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