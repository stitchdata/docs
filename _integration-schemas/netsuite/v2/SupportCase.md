---
tap: "netsuite"
version: "2"
name: SupportCase
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SupportCase.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/SupportCase
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: category
  type: varies
  description: ""
- name: email
  type: string
  description: ""
- name: lastMessageDate
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: serialNumber
  type: varies
  description: ""
- name: issue
  type: varies
  description: ""
- name: incomingMessage
  type: string
  description: ""
- name: caseNumber
  type: string
  description: ""
- name: phone
  type: string
  description: ""
- name: timeItemList
  type: varies
  description: ""
- name: helpDesk
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: emailForm
  type: boolean, string
  description: ""
- name: assigned
  type: varies
  description: ""
- name: startDate
  type: string
  description: ""
- name: searchSolution
  type: string
  description: ""
- name: solutionsList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: insertSolution
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: subsidiary
  type: varies
  description: ""
- name: title
  type: string
  description: ""
- name: module
  type: varies
  description: ""
- name: outgoingMessage
  type: string
  description: ""
- name: inboundEmail
  type: string
  description: ""
- name: endDate
  type: string
  description: ""
- name: product
  type: varies
  description: ""
- name: priority
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalOnly
  type: boolean, string
  description: ""
- name: escalationMessage
  type: string
  description: ""
- name: status
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: emailEmployeesList
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: origin
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: newSolutionFromMsg
  type: string
  description: ""
- name: escalateToList
  type: varies
  description: ""
- name: contact
  type: varies
  description: ""
- name: lastReopenedDate
  type: string
  description: ""
- name: company
  type: varies
  description: ""
- name: profile
  type: varies
  description: ""
---