---
tap: "impact"
version: "1"
key: "unique-url"

name: "unique_urls"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/unique_urls.json"
description: |
  The `{{ table.name }}` table contains info about unique URLs.

replication-method: "Full Table"

api-method:
  name: "Get unique URLs"
  doc-link: "https://developer.impact.com/default#operations-Unique_Urls-GetUniqueUrls"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "unique-url-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_last_assigned"
    type: "date-time"
    description: ""

  - name: "date_last_released"
    type: "date-time"
    description: ""

  - name: "landing_page"
    type: "string"
    description: ""

  - name: "media_partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-partner-id"

  - name: "media_partner_name"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---