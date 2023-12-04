---
tap: "yotpo"
version: "2"
key: ""

name: "emails"
doc-link: https://apidocs.yotpo.com/v1.0/reference#email-analytics-intro
singer-schema: https://github.com/singer-io/tap-yotpo/tree/master/tap_yotpo/schemas/emails.json
description: |
  The `{{ table.name }}` table contains data about every email sent from {{ integration.display_name }}.

  #### Attribution window {#email-attribution-window}

  When Stitch replicates data for this table, it will use an attribution window of {{ integration.attribution-window }} to fetch updated email statistics such as opens, clicks, etc. This means that every time a replication job runs, the last 30 days' worth of data will be replicated for this table.

  Refer to the [Replication](#replication) section for more info and examples of how the attribution window is used to query for data.

replication-method: "Key-based Incremental"
attribution-window: true

api-method:
  name: Email analytics raw data
  doc-link: https://apidocs.yotpo.com/v1.0/reference#raw-data

attributes:
  - name: "email_address"
    type: "string"
    primary-key: true
    description: "The email address of the recipient."
    foreign-key-id: "email-address-id"

  - name: "email_sent_timestamp"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The time the email was sent to the recipient."

  - name: "order_id"
    type: "string"
    description: "If applicable, the ID of the order the email is associated with."
    # foreign-key-id: "order-id"

  - name: "order_timestamp"
    type: "string"
    description: ""

  - name: "product_id"
    type: "string"
    description: "If applicable, the ID of the product the email is associated with."
    foreign-key-id: "product-id"

  - name: "sku"
    type: "string"
    description: ""

  - name: "email_type"
    type: "string"
    doc-link: "https://apidocs.yotpo.com/reference#email-analytics-intro"
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