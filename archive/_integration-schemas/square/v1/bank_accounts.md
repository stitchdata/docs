---
tap: "square"
version: "1"
key: "bank-account"

name: "bank_accounts"
doc-link: "https://developer.squareup.com/reference/square/bank-accounts-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/bank_accounts.json"
description: |
  The `{{ table.name }}` contains information about a merchant's bank account in {{ integration.display_name }}.

  **Note**: This table can't be replicated if the **Connect to a sandbox environment** box is checked in the [integration's settings](#add-stitch-data-source) due to limits imposed by {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List bank accounts (v2)"
  doc-link: "https://developer.squareup.com/reference/square/bank-accounts-api/get-bank-account"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The bank account ID."
    foreign-key-id: "bank-account-id"

  - name: "account_number_suffix"
    type: "string"
    description: ""

  - name: "account_type"
    type: "string"
    description: ""

  - name: "bank_name"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "creditable"
    type: "boolean"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "debitable"
    type: "boolean"
    description: ""

  - name: "holder_name"
    type: "string"
    description: ""

  - name: "location_id"
    type: "string"
    description: "The ID of the location associated with the bank account."
    foreign-key-id: "location-id"

  - name: "primary_bank_identification_number"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "version"
    type: "integer"
    description: ""
---