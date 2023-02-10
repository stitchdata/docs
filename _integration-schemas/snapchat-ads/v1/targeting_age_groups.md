---
tap: "snapchat-ads"
version: "1"
key: ""

name: "targeting_age_groups"
doc-link: https://developers.snapchat.com/api/docs/#demographics-age-groups
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/shared/targeting.json
description: "This stream retrieves the list of age group targeting options."

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
    description: "Age Group ID"

  - name: "name"
    type: "string"
    description: "Age group Value. Example: 18-35"

  - name: "parent_id"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: ""

  - name: "source"
    type: "string"
    description: "Data source"

  - name: "targeting_group"
    type: "string"
    description: "Targeting Group. Only possible value for this stream: `demographics`"

  - name: "targeting_type"
    type: "string"
    description: "Targeting Type name. Only possible value for this stream: `age_group`"

