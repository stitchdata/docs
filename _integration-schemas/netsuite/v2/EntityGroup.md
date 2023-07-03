---
tap: "netsuite"
version: "2"
name: EntityGroup
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/EntityGroup.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/EntityGroup
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: email
  type: string
  description: ""
- name: groupType
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: savedSearch
  type: varies
  description: ""
- name: laborResources
  type: string, integer
  description: ""
- name: isFunctionalTeam
  type: boolean, string
  description: ""
- name: isSavedSearch
  type: boolean, string
  description: ""
- name: isSalesRep
  type: boolean, string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: comments
  type: string
  description: ""
- name: groupName
  type: string
  description: ""
- name: isManufacturingWorkCenter
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: isSupportRep
  type: boolean, string
  description: ""
- name: isSalesTeam
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: machineResources
  type: string, integer
  description: ""
- name: restrictionGroup
  type: varies
  description: ""
- name: parentGroupType
  type: varies
  description: ""
- name: isPrivate
  type: boolean, string
  description: ""
- name: isProductTeam
  type: boolean, string
  description: ""
- name: workCalendar
  type: varies
  description: ""
- name: issueRole
  type: varies
  description: ""
- name: groupOwner
  type: varies
  description: ""
