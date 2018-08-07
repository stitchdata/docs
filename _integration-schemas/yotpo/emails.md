---
tap: "yotpo"
version: "1.0"

name: "emails"
doc-link: https://apidocs.yotpo.com/v1.0/reference#email-analytics-intro
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/emails.json
description: |
  The `emails`table contains data about every email sent from Yotpo.

replication-method: "Key-based Incremental"

api-method:
  name: Email Analytics Raw data
  doc-link: https://apidocs.yotpo.com/v1.0/reference#raw-data

attributes:

  - name: "email_address"
    type: "string"
    primary-key: true
    description: ""

  - name: "email_sent_timestamp"
    type: "string"
    primary-key: true
    replication-key: true
    description: ""

  - name: "order_id"
    type: "string"
    description: ""

  - name: "order_timestamp"
    type: "string"
    description: ""

  - name: "product_id"
    type: "string"
    description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "email_type"
    type: "string"
    description: ""

  - name: "reminder_num"
    type: "number"
    description: ""

  - name: "trr_bundle_id"
    type: "string"
    description: ""

  - name: "trr_bundle_subject"
    type: "string"
    description: ""

  - name: "review_type"
    type: "string"
    description: ""

  - name: "coupon_code"
    type: "string"
    description: ""

  - name: "opened_timestamp"
    type: "string"
    description: ""

  - name: "clicked_through_timestamp"
    type: "string"
    description: ""

  - name: "content_creation_timestamp"
    type: "string"
    description: ""

  - name: "review_form"
    type: "string"
    description: ""

  - name: "platform"
    type: "string"
    description: ""

  - name: "invalid_address_timestamp"
    type: "string"
    description: ""

  - name: "failed_timestamp"
    type: "string"
    description: ""

  - name: "unsubscribed_timestamp"
    type: "string"
    description: ""

  - name: "marked_spam_timestamp"
    type: "string"
    description: ""

  - name: "arrived_early_timestamp"
    type: "string"
    description: ""
---
