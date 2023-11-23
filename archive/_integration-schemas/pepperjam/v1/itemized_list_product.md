---
tap: "pepperjam"
version: "1"
key: "itemized_list_product"

name: "itemized_list_product"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Product"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/itemized_list_product.json"
description: |
  The `{{ table.name }}` table contains information about products within your itemized lists in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "getItemizedListProducts"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Product"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The product ID."
    # foreign-key-id: "itemized-list-product-id"

  - name: "list_id"
    type: "integer"
    description: ""
    foreign-key-id: "itemized-list-id"

  - name: "name"
    type: "string"
    description: ""
---