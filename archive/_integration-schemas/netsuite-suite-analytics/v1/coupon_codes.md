---
tap: "netsuite-suite-analytics"
version: "1"
key: "coupon-code"

name: "coupon_codes"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/couponcode.html"
description: ""
replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}
  - name: "code"
    type: "string"
    description: ""
  - name: "coupon_code_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "coupon-code-id"
  - name: "date_sent"
    type: "date-time"
    description: ""
  - name: "promotion_code_id"
    type: "integer"
    description: ""
  - name: "recipient_id"
    type: "integer"
    description: ""
---