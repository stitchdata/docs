---
tap: "recharge"
version: "1"
key: "collection"

name: "collections"
doc-link: "https://developer.rechargepayments.com/#list-collections-alpha"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/collections.json"
description: |
  The `{{ table.name }}` table contains info about your collections.

replication-method: "Key-based Incremental"
api-method:
  name: "List collections"
  doc-link: "https://developer.rechargepayments.com/#list-collections-alpha"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The collection ID."
    foreign-key-id: "collection-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time when the collection was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The date and time when the collection was created."

  - name: "name"
    type: "string"
    description: "The name of the collection."
---