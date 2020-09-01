---
tap: "square"
version: "1"
key: ""

name: "bank_accounts"
doc-link: "https://developer.squareup.com/reference/square/bank-accounts-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/bank_accounts.json"
description: |
  The `{{ table.name }}` contains information about a merchant's bank account in {{ integration.display_name }}. This table cannot be replicated with a sandbox account due to restrictions from {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "List bank accounts"
    doc-link: "https://developer.squareup.com/reference/square/bank-accounts-api/get-bank-account"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The bank account ID."
    foreign-key-id: "bank-id"

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
    description: "The location ID of the bank account."
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
