---
tap: "activecampaign"
version: "1"
key: ""

name: "accounts"
doc-link: "https://developers.activecampaign.com/reference#accounts"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains information about accounts in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all accounts"
    doc-link: "https://developers.activecampaign.com/reference#list-all-accounts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the account was last updated."
    replication-key: true

  - name: "account_url"
    type: "string"
    description: ""
  - name: "contact_count"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "deal_count"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---
