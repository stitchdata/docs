---
tap: "yotpo"
version: "1.0"

name: "unsubscribers"
doc-link: https://apidocs.yotpo.com/reference#introduction-to-unsubscribers
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/unsubscribers.json
description: |
  The `unsubscribers` table contains data about customers who unsubscribed from one of Yotpo's emails.

replication-method: "Key-based Incremental"

replication-key:
  name: "since"

api-method:
  name: Retrieve a list of unsubscribers
  doc-link: https://apidocs.yotpo.com/reference#retrieve-a-list-of-unsubscribers

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The unsubscriber ID."

  - name: "user_email"
    type: "string"
    description: "The email address of the unsubscriber."
    foreign-key: true
    table: "emails"

  - name: "email_type_id"
    type: "number"
    doc-link: "https://apidocs.yotpo.com/reference#section-email-types"
    description: |
      The type of email the user unsubscribed from. Refer to [Yotpo's documentation](https://apidocs.yotpo.com/reference#section-email-types){:target="new"} for a list of possible values.

  - name: "unsubscirbed_by_name"
    type: "string"
    description: |
      **Note**: The misspelling in this field name originates in Yotpo's API. Stitch doesn't have the ability to rename it.
---
