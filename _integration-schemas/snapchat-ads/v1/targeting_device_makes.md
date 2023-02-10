---
tap: "snapchat-ads"
version: "1"
key: ""

name: "targeting_device_makes"
doc-link: https://developers.snapchat.com/api/docs/#device-make
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/shared/targeting.json
description: "This stream retrieves the list of device make targeting options. Please note that specifying a parent level make option like “Apple/” in the targeting spec will include all devices of the kind “Apple/*” like “Apple/iPad (3rd Gen)/”, “Apple/iPhone 4/”, “Apple/iPhone 7 Plus/” etc."

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "country_code"
    type: "string"
    description: "ISO ALPHA-2 Country Code (lowercase)"

  - name: "id"
    primary-key: true
    type: "string"
    description: "ID of the device maker"

  - name: "name"
    type: "string"
    description: "Name of the device Maker. Example: Google, HTC, AT&T"

  - name: "parent_id"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: ""

  - name: "source"
    type: "string"
    description: "Data Source"

  - name: "targeting_group"
    type: "string"
    description: "Targeting Group. Only possible value for this stream: `device`"

  - name: "targeting_type"
    type: "string"
    description: "Targeting Type. Only possible value for this stream: `marketing_name`"

