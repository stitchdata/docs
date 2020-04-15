---
tap: "saasoptics"
version: "1"
key: "currency-code"

name: "currency_codes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/currency_codes.json"
description: |
  The `{{ table.name }}` table contains info about currency codes.

replication-method: "Full Table"

api-method:
  name: "Country Codes List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115003604453-Country-Codes-R-"

attributes:
  - name: "code"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "currency-code-id"

  - name: "name"
    type: "string"
    description: ""
---