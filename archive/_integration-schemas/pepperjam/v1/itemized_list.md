---
tap: "pepperjam"
version: "1"
key: "itemized_list"

name: "itemized_list"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#ItemizedList"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/itemized_list.json"
description: |
  The `{{ table.name }}` table contains information about your itemized lists in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "getItemizedList"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#ItemizedList"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The itemized list ID."
    foreign-key-id: "itemized-list-id"
    
  - name: "default"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "product_count"
    type: "integer"
    description: ""
---