---
tap: "pepperjam"
version: "1"
key: "term"

name: "term"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Term"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/term.json"
description: |
  The {{ table.name }} table contains information about the terms for your program in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "getTerm"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Term"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The term ID."
    #foreign-key-id: "term-id"

  - name: "cookie_duration"
    type: "string"
    description: ""
  - name: "created"
    type: "date"
    description: ""
  - name: "default"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
---
