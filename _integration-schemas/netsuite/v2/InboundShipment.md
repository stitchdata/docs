---
tap: "netsuite"
version: "2"
name: InboundShipment
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/InboundShipment.html
description: |
  The `{{ table.name }}` table contains info about inbound shipments in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "inbound-shipment"

replication-method: "Full Table"

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