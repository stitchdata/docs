---
tap: "shippo"
version: "1"

name: "refunds"
doc-link: https://goshippo.com/docs/reference#refunds
singer-schema: https://github.com/singer-io/tap-shippo/blob/master/tap_shippo/schemas/refunds.json
description: |
  The `{{ table.name }}` table contains info about refunds, which are reimbursements for successfully created but **unused** transactions.

  #### Refund processing time and data discrepancies

  If the data in this table doesn't look like you'd expect it to, keep in mind that refunds can take up to 14 days to be processed.

replication-method: "Key-based Incremental"
api-method:
  name: listAllRefunds
  doc-link: https://goshippo.com/docs/reference?version=2016-10-25#refunds-list

attributes:
  - name: "object_id"
    type: "string"
    primary-key: true
    description: "The refund ID."
    #foreign-key-id: "refund-id"

  - name: "object_updated"
    type: "date-time"
    replication-key: true
    description: "The time the refund was last updated."

  - name: "object_created"
    type: "date-time"
    description: "The time the refund was created."

  - name: "object_owner"
    type: "string"
    description: "The username of the user who created the refund."

  - name: "transaction"
    type: "string"
    description: "The ID of the transaction to be refunded."
    foreign-key-id: "transaction-id"

  - name: "test"
    type: "boolean"
    description: "Indicates if the refund was created in test mode."
---