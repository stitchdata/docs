---
tap: "netsuite"
# version: "1.0"

name: "InboundShipment"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/InboundShipment.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
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

  - name: "internalId"
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
