---
tap: "netsuite"
version: "2"
name: PromotionCode
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PromotionCode.html
description: |
  The `{{ table.name }}` table contains info about the promotion codes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "promotion-code"

replication-method: "Full Table"

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