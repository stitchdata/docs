---
tap: "tiktok-ads"
version: "1"
key: "advertisers"

name: "advertisers"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1708503235186689
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/advertisers.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "id, create_time"
valid-replication-keys: "create_time"

attributes:
  - name: "address"
    type: "string"
    description: "Advertiser address information"

  - name: "balance"
    type: "number"
    description: "Account available balance（The unit is related to the advertiser's currency type currency"

  - name: "company"
    type: "string"
    description: "Advertiser's company name"

  - name: "contacter"
    type: "string"
    description: "Contact Person"

  - name: "country"
    type: "string"
    description: "The advertiser's country"

  - name: "create_time"
    type: "string"
    format: "date-time"
    description: "Advertiser's create time"
    replication-key: true
    primary-key: true

  - name: "currency"
    type: "string"
    description: "Type of currency used by advertisers"

  - name: "description"
    type: "string"
    description: "Brand description, i.e. promotional content"

  - name: "email"
    type: "string"
    description: "Advertiser contact email, masked format. For example, d*****h@test.com"

  - name: "id"
    type: "integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "industry"
    type: "string"
    description: "Advertiser industry category. See [Appendix-Industries](https://ads.tiktok.com/marketing_api/docs?id=1739357589575681)"

  - name: "language"
    type: "string"
    description: "Language used by advertisers"

  - name: "license_no"
    type: "string"
    description: "License number"

  - name: "license_url"
    type: "string"
    description: "License preview address, the link is valid for an hour by default."

  - name: "name"
    type: "string"
    description: "Advertiser name"

  - name: "phonenumber"
    type: "string"
    description: "Contact mobile number, desensitised data"

  - name: "promotion_area"
    type: "string"
    description: ""

  - name: "promotion_center_city"
    type: "string"
    description: ""

  - name: "promotion_center_province"
    type: "string"
    description: ""

  - name: "reason"
    type: "string"
    description: "Reason for rejection"

  - name: "role"
    type: "string"
    description: "Advertiser role, see [Enumeration - Advertiser Role](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138)"

  - name: "status"
    type: "string"
    description: "Advertiser status, see [Enumeration - Advertiser Status](https://ads.tiktok.com/marketing_api/docs?id=1737174886619138)"

  - name: "telephone"
    type: "string"
    description: "Fixed phone number, desensitised data"

  - name: "timezone"
    type: "string"
    description: "Ad account time zone including GMT offset. For example, `Etc/GMT`"
---