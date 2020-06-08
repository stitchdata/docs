---
tap: "pepperjam"
version: "1"
key: "creative_coupon"

name: "creative_coupon"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CouponCreative"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_coupon.json"
description: |
  The `{{ table.name }}` table contains information about coupon creatives in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "getCouponCreative"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CouponCreative"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The coupon ID."
    #foreign-key-id: "coupon-id"

  - name: "modified"
    type: "date-time"
    description: "The time the coupon was last modified."
    replication-key: true
    
  - name: "coupon_code"
    type: "string"
    description: ""
  - name: "created"
    type: "date-time"
    description: ""
  - name: "description"
    type: "string"
    description: ""
  - name: "end_date"
    type: "date-time"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "personalized"
    type: "integer"
    description: ""
  - name: "private"
    type: "integer"
    description: ""
  - name: "private_affiliates"
    type: "array"
    description: ""
    subattributes:
      - name: "affiliate_id"
        type: "integer"
        description: ""
        foreign-key-id: "affiliate-id"

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""
  - name: "promotions"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "promotion-id"

      - name: "name"
        type: "string"
        description: ""
  - name: "start_date"
    type: "date-time"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "url"
    type: "string"
    description: ""
  - name: "view_date"
    type: "date-time"
    description: ""
---