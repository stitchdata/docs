---
tap: netsuite
version: "2"
name: Contact
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Contact.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Contact
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: middleName
  type: string
  description: ""
- name: fax
  type: string
  description: ""
- name: email
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: assistantPhone
  type: string
  description: ""
- name: addressbookList
  type: varies
  description: ""
- name: assistant
  type: varies
  description: ""
- name: defaultAddress
  type: string
  description: ""
- name: subscriptionsList
  type: varies
  description: ""
- name: phone
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: comments
  type: string
  description: ""
- name: categoryList
  type: varies
  description: ""
- name: mobilePhone
  type: string
  description: ""
- name: firstName
  type: string
  description: ""
- name: salutation
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: subsidiary
  type: varies
  description: ""
- name: phoneticName
  type: string
  description: ""
- name: title
  type: string
  description: ""
- name: homePhone
  type: string
  description: ""
- name: supervisor
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: billPay
  type: boolean, string
  description: ""
- name: lastName
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: contactSource
  type: varies
  description: ""
- name: supervisorPhone
  type: string
  description: ""
- name: altEmail
  type: string
  description: ""
- name: image
  type: varies
  description: ""
- name: isPrivate
  type: boolean, string
  description: ""
- name: globalSubscriptionStatus
  type: varies
  description: ""
- name: officePhone
  type: string
  description: ""
- name: dateCreated
  type: string
  description: ""
- name: entityId
  type: string
  description: ""
- name: company
  type: varies
  description: ""
