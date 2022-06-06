---
tap: "shopify"
version: "1"

name: "locations"
doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/location#top"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/locations.json"
description: |
  The `{{ table.name }}` table contains info about .

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of locations"
    doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/location#get-locations"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The event ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","location" | replace: "[ACTION]","last updated" }}

  - name: "admin_graphql_api_id"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","location" | replace: "[ACTION]","created" }}

  - name: "country_code"
    type: "string"
    description: "The two-letter code (ISO 3166-1 alpha-2 format) corresponding to country the location is in."

  - name: "name"
    type: "string"
    description: "The name of the location."

  - name: "address1"
    type: "string"
    description: "The location's street address."

  - name: "address2"
    type: "string"
    description: "The second line of the location's street address."

  - name: "city"
    type: "string"
    description: "The city the location is in."

  - name: "province_code"
    type: "string"
    description: "The province, state, or district code (ISO 3166-2 alpha-2 format) of the location."

  - name: "zip"
    type: "string"
    description: "The zip or postal code."

  - name: "localized_province_name"
    type: "string"
    description: ""

  - name: "localized_country_name"
    type: "string"
    description: "The localized name of the location's country."

  - name: "province"
    type: "string"
    description: "The localized name of the location's region. "

  - name: "phone"
    type: "string"
    description: "The phone number of the location."

  - name: "legacy"
    type: "boolean"
    description: "Whether this is a fulfillment service location."

  - name: "country"
    type: "string"
    description: "The country the location is in."

  - name: "active"
    type: "boolean"
    description: "Whether the location is active."
---