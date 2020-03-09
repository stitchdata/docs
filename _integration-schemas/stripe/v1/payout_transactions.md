---
tap: "stripe"
version: "1"

name: "payout_transactions"
doc-link: "https://stripe.com/docs/api/payouts"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/payout_transactions.json"
description: "This table contains info about payout transactions."

replication-method: "Full Table Replication"

api-method:
    name: "List all payouts"
    doc-link: "https://stripe.com/docs/api/payouts/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The payout transaction ID."
    foreign-key-id: "payout-transaction-id"

  - name: "payout_id"
    type: "string"
    description: "The payout ID."
    foreign-key-id: "payout-id"
---
