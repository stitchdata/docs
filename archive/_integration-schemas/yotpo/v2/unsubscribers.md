---
tap: "yotpo"
version: "2"
key: ""

name: "unsubscribers"
doc-link: https://apidocs.yotpo.com/reference#introduction-to-unsubscribers
singer-schema: https://github.com/singer-io/tap-yotpo/tree/master/tap_yotpo/schemas/unsubscribers.json
description: |
  The `{{ table.name }}` table contains data about customers who unsubscribed from one of Yotpo's emails.

replication-method: "Full Table"

api-method:
  name: Retrieve a list of unsubscribers
  doc-link: https://apidocs.yotpo.com/reference#retrieve-a-list-of-unsubscribers

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The unsubscriber ID."
    # foreign-key-id: "unsubscriber-id"

  - name: "user_email"
    type: "string"
    description: "The email address of the unsubscriber."
    foreign-key-id: "email-address-id"

  - name: "email_type_id"
    type: "number"
    description: ""
  - name: "unsubscirbed_by_name"
    type: "string"
    description: |
      **Note**: The misspelling in this field name originates in {{ integration.display_name }}'s API. Stitch doesn't have the ability to rename it.
---

