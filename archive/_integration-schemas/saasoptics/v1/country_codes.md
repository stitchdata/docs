---
tap: "saasoptics"
version: "1"
key: "country-code"

name: "country_codes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/country_codes.json"
description: |
  The `{{ table.name }}` table contains info about country codes.

replication-method: "Full Table"

api-method:
  name: "Country Codes List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115003604453-Country-Codes-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "country-code-id"
  
  - name: "code"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---