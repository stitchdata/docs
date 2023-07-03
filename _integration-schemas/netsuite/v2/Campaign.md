---
tap: netsuite
version: "2"
name: Campaign
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Campaign.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Campaign
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: totalRevenue
  type: string, number
  description: ""
- name: leadsGenerated
  type: string, integer
  description: ""
- name: category
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: family
  type: varies
  description: ""
- name: costPerCustomer
  type: string, number
  description: ""
- name: offer
  type: varies
  description: ""
- name: expectedRevenue
  type: string, number
  description: ""
- name: campaignId
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: profit
  type: string, number
  description: ""
- name: startDate
  type: string
  description: ""
- name: itemList
  type: varies
  description: ""
- name: vertical
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: title
  type: string
  description: ""
- name: promotionCode
  type: varies
  description: ""
- name: endDate
  type: string
  description: ""
- name: searchEngine
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: keyword
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: conversions
  type: string, integer
  description: ""
- name: campaignEventList
  type: varies
  description: ""
- name: audience
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: url
  type: string
  description: ""
- name: baseCost
  type: string, number
  description: ""
- name: campaignDirectMailList
  type: varies
  description: ""
- name: uniqueVisitors
  type: string, integer
  description: ""
- name: cost
  type: string, number
  description: ""
- name: convCostPerCustomer
  type: string, number
  description: ""
- name: local
  type: boolean, string
  description: ""
- name: roi
  type: string, number
  description: ""
- name: owner
  type: varies
  description: ""
- name: eventResponseList
  type: varies
  description: ""
- name: campaignEmailList
  type: varies
  description: ""
- name: message
  type: string
  description: ""
