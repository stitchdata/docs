---
tap: "netsuite"
version: "2"
name: Issue
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Issue.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Issue
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: reproduce
  type: varies
  description: ""
- name: issueType
  type: varies
  description: ""
- name: buildBroken
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: productTeam
  type: varies
  description: ""
- name: buildTarget
  type: varies
  description: ""
- name: emailAssignee
  type: boolean, string
  description: ""
- name: issueNumber
  type: string
  description: ""
- name: newDetails
  type: string
  description: ""
- name: brokenInVersionList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: versionTarget
  type: varies
  description: ""
- name: assigned
  type: varies
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: targetVersionList
  type: varies
  description: ""
- name: isShowStopper
  type: boolean, string
  description: ""
- name: source
  type: varies
  description: ""
- name: isReviewed
  type: boolean, string
  description: ""
- name: module
  type: varies
  description: ""
- name: fixedInVersionList
  type: varies
  description: ""
- name: issueStatus
  type: varies
  description: ""
- name: product
  type: varies
  description: ""
- name: issueAbstract
  type: string
  description: ""
- name: priority
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: trackCode
  type: varies
  description: ""
- name: emailCellsList
  type: varies
  description: ""
- name: relatedIssuesList
  type: varies
  description: ""
- name: emailEmployeesList
  type: varies
  description: ""
- name: severity
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: buildFixed
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: isOwner
  type: boolean, string
  description: ""
- name: reviewer
  type: varies
  description: ""
- name: issueTagsList
  type: varies
  description: ""
- name: versionFixed
  type: varies
  description: ""
- name: versionBroken
  type: varies
  description: ""
- name: reportedBy
  type: varies
  description: ""
- name: externalAbstract
  type: string
  description: ""
- name: externalDetails
  type: string
  description: ""
