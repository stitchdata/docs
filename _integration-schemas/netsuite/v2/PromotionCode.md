---
tap: "netsuite"
version: "2"
name: PromotionCode
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PromotionCode.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/PromotionCode
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: description
  type: string
  description: ""
- name: freeShipMethod
  type: varies
  description: ""
- name: numberToGenerate
  type: string, integer
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: useType
  type: varies
  description: ""
- name: currencyList
  type: varies
  description: ""
- name: itemsList
  type: varies
  description: ""
- name: excludeItems
  type: boolean, string
  description: ""
- name: minimumOrderAmount
  type: string, number
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: displayLineDiscounts
  type: boolean, string
  description: ""
- name: startDate
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: partnersList
  type: varies
  description: ""
- name: rate
  type: string
  description: ""
- name: isPublic
  type: boolean, string
  description: ""
- name: endDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: code
  type: string
  description: ""
- name: applyDiscountTo
  type: varies
  description: ""
- name: discountType
  type: boolean, string
  description: ""
- name: codePattern
  type: string
  description: ""
- name: discount
  type: varies
  description: ""
- name: locationList
  type: varies
  description: ""
- name: implementation
  type: varies
  description: ""
---