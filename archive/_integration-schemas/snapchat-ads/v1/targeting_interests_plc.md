---
tap: "snapchat-ads"
version: "1"
key: ""

name: "targeting_interests_plc"
doc-link: https://developers.snapchat.com/api/docs/#interests-placed-visitation-segments
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/shared/targeting.json
description: "This stream retrieves the list of placed visitation segments targeting options by the specified country code"

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
    description: "Id of plc interest"

  - name: "name"
    type: "string"
    description: "Name of the plc interest"

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
    description: "Targeting Group. Only possible value for this stream: `interests`"

  - name: "targeting_type"
    type: "string"
    description: "Targeting Type. Only possible value for this stream: `plc`"
---