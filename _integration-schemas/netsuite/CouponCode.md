---
tap: "netsuite"
version: "1.0"

name: "CouponCode"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/couponcode.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CouponCode.json"
description: |
  The `{{ table.name }}` table contains info about the coupon codes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "coupon-code"

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