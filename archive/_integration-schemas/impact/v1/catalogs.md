---
tap: "impact"
version: "1"
key: "catalog"

name: "catalogs"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/catalogs.json"
description: |
  The `{{ table.name }}` table contains info about the catalogs in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List catalogs"
  doc-link: "https://developer.impact.com/default#operations-Catalogs-ListCatalogs"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "catalog-id"

  - name: "advertiser_id"
    type: "integer"
    description: ""
    foreign-key-id: "advertiser-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "date_last_updated"
    type: "date-time"
    description: ""

  - name: "filename"
    type: "string"
    description: ""

  - name: "items_uri"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "number_of_items"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "upload_method"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---