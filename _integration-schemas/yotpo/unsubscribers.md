---
tap: "yotpo"
version: "1.0"

name: "unsubscribers"
doc-link: https://apidocs.yotpo.com/reference#introduction-to-unsubscribers
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/unsubscribers.json
description: |
  The `unsubscribers` endpoint contains data about customers who unsubscribed from one of Yotpo's emails

replication-method: "Key-based Incremental"

api-method:
  name: Retrieve a List of Unsubscribers
  doc-link: https://apidocs.yotpo.com/reference#retrieve-a-list-of-unsubscribers

attributes:

  - name: "id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "user_email"
    type: "string"
    description: ""

  - name: "email_type_id"
    type: "number"
    description: ""

  - name: "unsubscirbed_by_name"
    type: "string"
    description: "This field is misspelled in the api response!"
---
