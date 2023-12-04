---
tap: "snapchat-ads"
version: "1"
key: ""

name: "targeting_genders"
doc-link: https://developers.snapchat.com/api/docs/#demographics-gender
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/shared/targeting.json
description: "This stream retrieves the list of gender targeting options."

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
    description: "Gender ID"

  - name: "name"
    type: "string"
    description: "Gender Value"

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
    description: "Targeting Group. Only possible value for this stream: `demographics`"

  - name: "targeting_type"
    type: "string"
    description: "Targeting Type. Only possible value for this stream: `gender`"
---