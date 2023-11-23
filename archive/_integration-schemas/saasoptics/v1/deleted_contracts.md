---
tap: "saasoptics"
version: "1"
key: "deleted-contract"

name: "deleted_contracts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/deleted_contracts.json"
description: |
  The `{{ table.name }}` table contains a list of deleted {{ integration.display_name }} contracts.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the deleted contract."
    foreign-key-id: "contract-id"

  - name: "deleted"
    type: "date-time"
    description: "The date the contract was deleted."
    replication-key: true

  - name: "deleted_by"
    type: "string"
    description: "The user who deleted the contract."
---