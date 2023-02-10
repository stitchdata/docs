---
tap: "snapchat-ads"
version: "1"
key: ""

name: "phone_numbers"
doc-link: https://developers.snapchat.com/api/docs/#swipe-to-call-text-phone-number-verification
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/phone_numbers.json
description: "This stream retrieves all verified phone numbers for an Ad Account."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "ad_account_id"
    type: "string"
    description: "AD Account ID"

  - name: "country_code"
    type: "string"
    description: "ISO ALPHA-2 Country Code (lowercase)"

  - name: "created_at"
    type: "date-time"
    description: "Date pf creation"

  - name: "id"
    primary-key: true
    type: "string"
    description: "ID"

  - name: "name"
    type: "string"
    description: "Name"

  - name: "numerical_country_code"
    type: "string"
    description: "NUmerical Country Code"

  - name: "phone_number"
    type: "string"
    description: "Phone NUmber"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last updated"

  - name: "verification_status"
    type: "string"
    description: "Verification Status"


