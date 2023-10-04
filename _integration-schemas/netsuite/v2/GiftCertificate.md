---
tap: "netsuite"
version: "2"
name: GiftCertificate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/GiftCertificate.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/GiftCertificate
description: |
  The `{{ table.name }}` table contains info about the gift certificates in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "gift-certificate"

replication-method: "Full Table"

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
---