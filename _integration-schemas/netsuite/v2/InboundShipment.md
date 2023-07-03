---
tap: "netsuite"
version: "2"
name: InboundShipment
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/InboundShipment.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/InboundShipment
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: expectedDeliveryDate
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: shipmentMemo
  type: string
  description: ""
- name: itemsList
  type: varies
  description: ""
- name: expectedShippingDate
  type: string
  description: ""
- name: shipmentStatus
  type: varies
  description: ""
- name: externalDocumentNumber
  type: string
  description: ""
- name: actualDeliveryDate
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: vesselNumber
  type: string
  description: ""
- name: actualShippingDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: shipmentNumber
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: billOfLading
  type: string
  description: ""
- name: shipmentBaseCurrency
  type: string
  description: ""
---