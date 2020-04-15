---
tap: "saasoptics"
version: "1"
key: "revenue-entries"

name: "revenue_entries"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/revenue_entries.json"
description: |
  The `{{ table.name }}` table contains info about revenue entries.

replication-method: "Key-based Incremental"

api-method:
  name: "Revenue Entries List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115003674273-Revenue-Entries-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "revenue-entry-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "home_amount"
    type: "number"
    description: ""

  - name: "local_amount"
    type: "number"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "transaction"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"
---