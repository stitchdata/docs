---
tap: "snapchat-ads"
version: "1"
key: ""

name: "ads"
doc-link: https://developers.snapchat.com/api/docs/#get-all-ads-under-an-ad-account
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/ads.json
description: "This stream retrieves all Ads under a specified Ad account"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "ad_account_id"
    type: "string"
    description: "AD Account ID"

  - name: "ad_squad_id"
    type: "string"
    description: "AD Squad ID"

  - name: "created_at"
    type: "date-time"
    description: "Date of creation for AD"

  - name: "creative_id"
    type: "string"
    description: "Creative ID"

  - name: "id"
    primary-key: true
    type: "string"
    description: "AD ID"

  - name: "name"
    type: "string"
    description: "AD name"

  - name: "paying_advertiser_name"
    type: "string"
    description: "Name of the paying advertiser/political entity"

  - name: "render_type"
    type: "string"
    description: ""

  - name: "review_status"
    type: "string"
    description: "Ad Review Status. Example: PENDING, APPROVED, REJECTED"

  - name: "review_status_reasons"
    type: "array"
    description: "List of Ad Review Rejection Reasons"
    subattributes:
      - name: "items" 
        type: "string"
        description: ""


  - name: "status"
    type: "string"
    description: "Ad status. Example: ACTIVE, PAUSED"

  - name: "third_party_paid_impression_tracking_urls"
    type: "array"
    description: "Third-party impression tags, executed on ad impression"
    subattributes:
    - name: "tracking_url_metadata"
      type: "object"
      description: ""

    - name: "expanded_tracking_url"
      type: "string"
      description: ""

    - name: "tracking_url"
      type: "string"
      description: ""


  - name: "third_party_swipe_tracking_urls"
    type: "array"
    description: "Third-party swipe tags, executed on swipe of attachment"
    subattributes:
    - name: "tracking_url_metadata"
      type: "object"
      description: ""

    - name: "expanded_tracking_url"
      type: "string"
      description: ""

    - name: "tracking_url"
      type: "string"
      description: ""


  - name: "type"
    type: "string"
    description: "Ad type. Example: SNAP_AD, LONGFORM_VIDEO, APP_INSTALL"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last update"
    replication-key: true
---