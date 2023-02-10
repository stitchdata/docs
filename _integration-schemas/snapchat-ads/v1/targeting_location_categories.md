---
tap: "snapchat-ads"
version: "1"
key: ""

name: "targeting_location_categories"
doc-link: https://developers.snapchat.com/api/docs/#location
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/shared/targeting.json
description: "Location targeting allows an advertiser to target users based on their location."

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
    description: "Location Category ID"

  - name: "name"
    type: "string"
    description: "Location Category Name"

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
    description: "Targeting Group. Only possible value for this stream: `location`"

  - name: "targeting_type"
    type: "string"
    description: "Targeting Type. Only possible value for this stream: `categories_loi`"
---