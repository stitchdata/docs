---
tap: netsuite
version: "2"
name: SiteCategory
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SiteCategory.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/SiteCategory
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: description
  type: string
  description: ""
- name: pageTitle
  type: string
  description: ""
- name: searchKeywords
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: itemListLayout
  type: varies
  description: ""
- name: metaTagHtml
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: urlComponent
  type: string
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: storeDisplayThumbnail
  type: varies
  description: ""
- name: sitemapPriority
  type: varies
  description: ""
- name: excludeFromSitemap
  type: boolean, string
  description: ""
- name: parentCategory
  type: varies
  description: ""
- name: presentationItemList
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: storeDetailedDescription
  type: string
  description: ""
- name: categoryListLayout
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: correlatedItemsListLayout
  type: varies
  description: ""
- name: website
  type: varies
  description: ""
- name: translationsList
  type: varies
  description: ""
- name: itemId
  type: string
  description: ""
- name: storeDisplayImage
  type: varies
  description: ""
- name: relatedItemsListLayout
  type: varies
  description: ""
