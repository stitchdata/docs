---
tap: "netsuite"
version: "1"

name: "InboundShipment"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/inboundshipment.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/InboundShipment.json"
description: |
  The `{{ table.name }}` table contains info about inbound shipments in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "inbound-shipment"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "inbound-shipment-id"

  - name: "actualDeliveryDate"
    type: "date-time"
    description: ""

  - name: "actualShippingDate"
    type: "date-time"
    description: ""

  - name: "billOfLading"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "expectedDeliveryDate"
    type: "date-time"
    description: ""

  - name: "expectedShippingDate"
    type: "date-time"
    description: ""

  - name: "externalDocumentNumber"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "itemsList"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "shipmentMemo"
    type: "string"
    description: ""

  - name: "shipmentNumber"
    type: "string"
    description: ""

  - name: "shipmentStatus"
    type: "varies"
    description: ""

  - name: "vesselNumber"
    type: "string"
    description: ""
---