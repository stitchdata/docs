---
tap: "saasoptics"
version: "1"
key: "deleted-transactions"

name: "deleted_transactions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/deleted_transactions.json"
description: |
  The `{{ table.name }}` table contains a list of deleted {{ integration.display_name }} transactions.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the deleted transaction."
    foreign-key-id: "transaction-id"

  - name: "deleted"
    type: "date-time"
    description: "The date the transaction was deleted."
    replication-key: true
    
  - name: "deleted_by"
    type: "string"
    description: "The user who deleted the transaction."
---