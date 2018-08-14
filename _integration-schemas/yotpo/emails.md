---
tap: "yotpo"
version: "1.0"

name: "emails"
doc-link: https://apidocs.yotpo.com/v1.0/reference#email-analytics-intro
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/emails.json
description: |
  The `emails` table contains data about every email sent from Yotpo.

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
    description: "If applicable, the time the order was placed."

  - name: "product_id"
    type: "string"
    description: "If applicable, the ID of the product the email is associated with."
    foreign-key-id: "product-id"

  - name: "sku"
    type: "string"
    description: "If applicable, the SKU of the product the email is associated with."

  - name: "email_type"
    type: "string"
    doc-link: "https://apidocs.yotpo.com/reference#email-analytics-intro"
    description: |
      The email's type. For example: `reminder`

  - name: "reminder_num"
    type: "number"
    description: "The number of the MAP reminder email."

  - name: "trr_bundle_id"
    type: "string"
    description: "If applicable, the bundle ID associated with the product."

  - name: "trr_bundle_subject"
    type: "string"
    description: "If applicable, the bundle subject associated with the product."

  - name: "review_type"
    type: "string"
    description: "If applicable, the type of review associated with the email."

  - name: "coupon_code"
    type: "string"
    description: "If applicable, the coupon code associated with the email."

  - name: "opened_timestamp"
    type: "string"
    description: "The time the recipient opened the email."

  - name: "clicked_through_timestamp"
    type: "string"
    description: "The time th e recipient clicked through a link in the email."

  - name: "content_creation_timestamp"
    type: "string"
    description: "The time the email content was created."

  - name: "review_form"
    type: "string"
    description: "If applicable, the review form associated with the email."

  - name: "platform"
    type: "string"
    description: "The platform the recipient viewed the email on. For example: `desktop`"

  - name: "invalid_address_timestamp"
    type: "string"
    description: "The time the recipient's email address was marked as invalid."

  - name: "failed_timestamp"
    type: "string"
    description: "The time the email failed to send."

  - name: "unsubscribed_timestamp"
    type: "string"
    description: "The time the recipient unsubscribed from the email list."

  - name: "marked_spam_timestamp"
    type: "string"
    description: "The time the recipient marked the email as spam."

  - name: "arrived_early_timestamp"
    type: "string"
    description: "The time the email arrived early."
---