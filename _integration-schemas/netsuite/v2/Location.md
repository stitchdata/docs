---
tap: "netsuite"
version: "2"
name: Location
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Location.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Location
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: timeZone
  type: varies
  description: ""
- name: dailyShippingCapacity
  type: string, integer
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: includeLocationRegionsList
  type: varies
  description: ""
- name: bufferStock
  type: string, integer
  description: ""
- name: parent
  type: varies
  description: ""
- name: tranPrefix
  type: string
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: logo
  type: varies
  description: ""
- name: geolocationMethod
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: autoAssignmentRegionSetting
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: longitude
  type: string, number
  description: ""
- name: useBins
  type: boolean, string
  description: ""
- name: classTranslationList
  type: varies
  description: ""
- name: businessHoursList
  type: varies
  description: ""
- name: soPredictedDays
  type: string, integer
  description: ""
- name: includeInControlTower
  type: boolean, string
  description: ""
- name: makeInventoryAvailableStore
  type: boolean, string
  description: ""
- name: mainAddress
  type: varies
  description: ""
- name: returnAddress
  type: varies
  description: ""
- name: storePickupBufferStock
  type: string, number
  description: ""
- name: allowStorePickup
  type: boolean, string
  description: ""
- name: totalShippingCapacity
  type: string, integer
  description: ""
- name: externalId
  type: string
  description: ""
- name: soPredConfidence
  type: string, number
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: nextPickupCutOffTime
  type: string
  description: ""
- name: makeInventoryAvailable
  type: boolean, string
  description: ""
- name: latitude
  type: string, number
  description: ""
- name: locationType
  type: varies
  description: ""
- name: excludeLocationRegionsList
  type: varies
  description: ""
- name: subsidiaryList
  type: varies
  description: ""
