---
tap: "pipedrive"
version: "1.0"
key: "currency"

name: "currency"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/currency.json"
description: |
  The `{{ table.name }}` table contains info about the currencies listed in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all supported currencies"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Currencies"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The currency ID."
    #foreign-key-id: "currency-id"

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "decimal_points"
    type: "integer"
    description: ""

  - name: "is_custom_flag"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "symbol"
    type: "string"
    description: ""
---