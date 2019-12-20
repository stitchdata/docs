---
tap: "uservoice"
version: "1.0"

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
    foreign-key-id: "external-account-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the external account was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the external account was created in {{ integration.display_name }}."

  - name: "external_id"
    type: "string"
    description: "The ID of the account in the external system."

  - name: "is_blocker"
    type: "boolean"
    description: "If `true`, feedback associated with the external account has been flagged as a blocker."

  - name: "ltv"
    type: "number"
    description: "The Lifetime Value (LTV) of the external account, represented in USD."

  - name: "ltv_cents"
    type: "integer"
    description: "The Lifetime Value (LTV) of the external account, represented in USD as cents."

  - name: "mrr"
    type: "number"
    description: "The Monthly Recurring Revenue (MRR) of the external account, represented in USD."

  - name: "mrr_cents"
    type: "integer"
    description: "The Monthly Recurring Revenue (MRR) of the external account, represented in USD as cents."

  - name: "name"
    type: "string"
    description: "The name of the external account."

  - name: "nps"
    type: "number"
    description: "The NPS rating associated with the external account."

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