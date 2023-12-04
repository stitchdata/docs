---
tap: "tiktok-ads"
version: "1"
key: "advertisers"

name: "advertisers"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1708503235186689
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/advertisers.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, create_time"
valid-replication-keys: "create_time"

attributes:
  - name: "address"
    type: "string"
    description: ""

  - name: "advertiser_account_type"
    type: "string"
    description: ""

  - name: "advertiser_id"
    type: "string"
    description: "Advertiser ID"
    primary-key: true

  - name: "balance"
    type: "number"
    description: ""

  - name: "cellphone_number"
    type: "string"
    description: ""

  - name: "company"
    type: "string"
    description: ""

  - name: "contacter"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "create_time"
    type: "string"
    description: "Advertiser's create time"
    replication-key: true
    primary-key: true

  - name: "currency"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "industry"
    type: "string"
    description: ""

  - name: "language"
    type: "string"
    description: ""

  - name: "license_no"
    type: "string"
    description: ""

  - name: "license_url"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "promotion_area"
    type: "string"
    description: ""

  - name: "promotion_center_city"
    type: "string"
    description: ""

  - name: "promotion_center_province"
    type: "string"
    description: ""

  - name: "rejection_reason"
    type: "string"
    description: ""

  - name: "role"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "telephone_number"
    type: "string"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""
---