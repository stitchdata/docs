---
tap: "saasoptics"
version: "1"
key: "deleted-revenue-entries"

name: "deleted_revenue_entries"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/deleted_revenue_entries.json"
description: |
  The `{{ table.name }}` table contains a list of deleted {{ integration.display_name }} revenue entries.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the deleted revenue entry."
    foreign-key-id: "revenue-entry-id"

  - name: "deleted"
    type: "date-time"
    description: "The date the revenue entry was deleted."
    replication-key: true

  - name: "deleted_by"
    type: "string"
    description: "The user who deleted the revenue entry."
---
