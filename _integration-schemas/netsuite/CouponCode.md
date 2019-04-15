---
tap: "netsuite"
version: "1.0"

name: "CouponCode"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/couponcode.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CouponCode.json"
description: |
  The `{{ table.name }}` table contains info about the coupon codes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Promotion"

feature-requirements:
  - tab: "Transactions"
    name: "Promotion Codes"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "coupon-code-id"

  - name: "code"
    type: "string"
    description: ""

  - name: "dateSent"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "promotion"
    type: "varies"
    description: ""

  - name: "recipient"
    type: "varies"
    description: ""

  - name: "useCount"
    type: "integer, string"
    description: ""

  - name: "used"
    type: "boolean, string"
    description: ""
---