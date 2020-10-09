---
tap: "saasoptics"
version: "1"
key: "deleted-invoices"

name: "deleted_invoices"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/deleted_invoices.json"
description: |
  The `{{ table.name }}` table contains a list of deleted {{ integration.display_name }} invoices.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the deleted invoice."
    foreign-key-id: "invoice-id"

  - name: "deleted"
    type: "date-time"
    description: "The date the invoice was deleted."
    replication-key: true
    
  - name: "deleted_by"
    type: "string"
    description: "The user who deleted the invoice."
---