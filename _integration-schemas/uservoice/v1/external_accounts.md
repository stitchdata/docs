---
tap: "uservoice"
# version: "1.0"

name: "external_accounts"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/ExternalAccount
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/external_accounts.py
description: |
  The `{{ table.name }}` table contains info about accounts from external systems.

replication-method: "Key-based Incremental"

api-method:
  name: List external accounts
  doc-link: "https://developer.uservoice.com/docs/api/v2/reference/#list-external-accounts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the external account as it is in {{ integration.display_name }}."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the external account was last updated."

  - name: "external_id"
    type: "string"
    description: "The external ID of the external account."

  - name: "is_blocker"
    type: "boolean"
    description: ""

  - name: "ltv"
    type: "number"
    description: "The LTV of the external account."

  - name: "ltv_cents"
    type: "integer"
    description: "The LTV of the external account, in cents."

  - name: "mrr"
    type: "number"
    description: "The MRR of the external account."

  - name: "mrr_cents"
    type: "integer"
    description: "The MRR of the external account, in cents."

  - name: "name"
    type: "string"
    description: "The name of the external account."

  - name: "nps"
    type: "number"
    description: "The NPS of the external account."

  - name: "plan"
    type: "string"
    description: "The plan associated with the external account."

  - name: "requests_count"
    type: "integer"
    description: "The number of requests associated with the external account."

  - name: "supported_ideas_count"
    type: "integer"
    description: "The number of supported ideas associated with the external account."

  - name: "users_count"
    type: "integer"
    description: "The number of users associated with the external account."
---