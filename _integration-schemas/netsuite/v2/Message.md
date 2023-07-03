---
tap: "netsuite"
version: "2"
name: Message
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Message.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Message
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: mediaItemList
  type: varies
  description: ""
- name: messageDate
  type: string
  description: ""
- name: recipient
  type: varies
  description: ""
- name: recordName
  type: string
  description: ""
- name: compressAttachments
  type: boolean, string
  description: ""
- name: cc
  type: string
  description: ""
- name: transaction
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
- name: bcc
  type: string
  description: ""
- name: author
  type: varies
  description: ""
- name: dateTime
  type: string
  description: ""
- name: activity
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: recipientEmail
  type: string
  description: ""
- name: recordTypeName
  type: string
  description: ""
- name: emailed
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: authorEmail
  type: string
  description: ""
- name: subject
  type: string
  description: ""
- name: incoming
  type: boolean, string
  description: ""
- name: message
  type: string
  description: ""
