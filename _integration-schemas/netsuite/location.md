---
tap: "netsuite"
version: "1.0"

name: "Location"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Location.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "allowStorePickup"
    type: "boolean, string"
    description: ""

  - name: "autoAssignmentRegionSetting"
    type: "anything"
    description: ""

  - name: "bufferStock"
    type: "integer, string"
    description: ""

  - name: "businessHoursList"
    type: "anything"
    description: ""

  - name: "classTranslationList"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "dailyShippingCapacity"
    type: "integer, string"
    description: ""

  - name: "excludeLocationRegionsList"
    type: "anything"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "geolocationMethod"
    type: "anything"
    description: ""

  - name: "includeChildren"
    type: "boolean, string"
    description: ""

  - name: "includeLocationRegionsList"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "latitude"
    type: "number, string"
    description: ""

  - name: "locationType"
    type: "anything"
    description: ""

  - name: "logo"
    type: "anything"
    description: ""

  - name: "longitude"
    type: "number, string"
    description: ""

  - name: "mainAddress"
    type: "anything"
    description: ""

  - name: "makeInventoryAvailable"
    type: "boolean, string"
    description: ""

  - name: "makeInventoryAvailableStore"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nextPickupCutOffTime"
    type: "date-time"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "parent"
    type: "anything"
    description: ""

  - name: "returnAddress"
    type: "anything"
    description: ""

  - name: "storePickupBufferStock"
    type: "number, string"
    description: ""

  - name: "subsidiaryList"
    type: "anything"
    description: ""

  - name: "timeZone"
    type: "anything"
    description: ""

  - name: "totalShippingCapacity"
    type: "integer, string"
    description: ""

  - name: "tranPrefix"
    type: "string"
    description: ""

  - name: "useBins"
    type: "boolean, string"
    description: ""
---
