---
tap: "recharge"
version: "2"
key: ""

name: "metafields_subscription"
doc-link: https://developer.rechargepayments.com/2021-11/metafields/metafields_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/metafields_subscription.json
description: |
  The `{{ table.name }}` table contains info about metafields related to subscriptions.

replication-method: "Key-based Incremental"

api-method:
  name: "List subscription metafields"
  doc-link: "https://developer.rechargepayments.com/2021-11/metafields/metafields_list"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The subscription metafield ID."
    foreign-key-id: "store-metafield-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the subscription metafield was last updated."

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "key"
    type: "string"
    description: ""

  - name: "namespace"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "string"
    description: ""

  - name: "owner_resource"
    type: "string"
    description: ""

  - name: "value"
    type: "string"
    description: ""

  - name: "value_type"
    type: "string"
    description: ""
---