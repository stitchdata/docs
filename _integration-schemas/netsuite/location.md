---
tap: "netsuite"
version: "1.0"

name: "Location"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/location.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Location.json"
description: |
  The `{{ table.name }}` table contains info about locations.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Locations"

feature-requirements:
  - tab: "Company"
    name: "Locations"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "location-id"

  - name: "allowStorePickup"
    type: "boolean, string"
    description: "Indicates if store pickup is allowed for the location."

  - name: "autoAssignmentRegionSetting"
    type: "varies"
    description: |
      Indicates how location assignment works for the location. Possible values are:

      - `Disallow`
      - `Allow Worldwide`
      - `Allow Worldwide Except Excluded Regions`
      - `Allow Specified Regions Only`

  - name: "bufferStock"
    type: "integer, string"
    description: "The minimum quantity of inventory to be maintained at the location."

  - name: "businessHoursList"
    type: "varies"
    description: ""

  - name: "classTranslationList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "dailyShippingCapacity"
    type: "integer, string"
    description: "The maximum number of orders that can be shipped from the location in a single day. Shipping capacity is based on the number of fulfillment requests created for the location in a one day interval."

  - name: "excludeLocationRegionsList"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "geolocationMethod"
    type: "varies"
    description: |
      The method by which automatic location assignment establishes the geographic position of the location:

  - name: "includeChildren"
    type: "boolean, string"
    description: "Indicates whether the location associated with all the sub-subsidiaries associated with each selected subsidiary."

  - name: "includeLocationRegionsList"
    type: "varies"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: "Indicates if the location is inactive."

  - name: "latitude"
    type: "number, string"
    description: "The latitude coordinate of the location."

  - name: "locationType"
    type: "varies"
    description: |
      The type of the location. Possible values include:

      - `Store`
      - `Warehouse`
      - `Undefined`

  - name: "logo"
    type: "varies"
    description: "The logo for the location."

  - name: "longitude"
    type: "number, string"
    description: "The longitude coordinate of the location."

  - name: "mainAddress"
    type: "varies"
    description: "The main address of the location."

  - name: "makeInventoryAvailable"
    type: "boolean, string"
    description: "Indicates if on-hand inventory stored at the location is available to orders."

  - name: "makeInventoryAvailableStore"
    type: "boolean, string"
    description: "Indicates if on-hand inventory stored at the location is included in the total quantity available that displays in the Web Store."

  - name: "name"
    type: "string"
    description: "The name of the location."

  - name: "nextPickupCutOffTime"
    type: "date-time"
    description: "The next cut-off time for same-day pickup orders at the location."

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: "The parent location, if applicable."

  - name: "returnAddress"
    type: "varies"
    description: "The return address for the location."

  - name: "storePickupBufferStock"
    type: "number, string"
    description: "The minimum inventory to be maintained at the location when creating store pickup orders."

  - name: "subsidiaryList"
    type: "varies"
    description: ""

  - name: "timeZone"
    type: "varies"
    description: "The time zone of the location."

  - name: "totalShippingCapacity"
    type: "integer, string"
    description: "The maximum number of shipping orders that can accumulate in the backlog of orders to be shipped from the location."

  - name: "tranPrefix"
    type: "string"
    description: "The value that is prefixed to transactions from this location."

  - name: "useBins"
    type: "boolean, string"
    description: "Indicates if bins are used to track inventory at the location."
---