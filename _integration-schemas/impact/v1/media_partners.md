---
tap: "impact"
version: "1"
key: "media-partner"

name: "media_partners"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/media_partners.json"
description: |
  The `{{ table.name }}` table contains info about the media partners in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get media partners"
  doc-link: "https://developer.impact.com/default#operations-Partners-GetMediaPartners"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "media-partner-id"

  - name: "address_line1"
    type: "string"
    description: ""

  - name: "address_line2"
    type: "string"
    description: ""

  - name: "campaigns"
    type: "array"
    description: ""
    subattributes:
      - name: "campaign_id"
        type: "integer"
        description: ""
        foreign-key-id: "campaign-id"

      - name: "campaign_name"
        type: "string"
        description: ""

      - name: "insertion_order_id"
        type: "integer"
        description: ""

      - name: "insertion_order_name"
        type: "string"
        description: ""

      - name: "join_date"
        type: "date-time"
        description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "contact"
    type: "object"
    description: ""
    subattributes:
      - name: "email_address"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "phone_number"
        type: "string"
        description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "country_state"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "groups"
    type: "array"
    description: ""
    subattributes:
      - name: "group_id"
        type: "integer"
        description: ""
        foreign-key-id: "media-partner-group-id"

      - name: "group_name"
        type: "string"
        description: ""

  - name: "mp_value1"
    type: "string"
    description: ""

  - name: "mp_value2"
    type: "string"
    description: ""

  - name: "mp_value3"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "partner_type"
    type: "string"
    description: ""

  - name: "phone_number"
    type: "string"
    description: ""

  - name: "postal_code"
    type: "string"
    description: ""

  - name: "primary_promotional_method"
    type: "string"
    description: ""

  - name: "promoting_countries"
    type: "string"
    description: ""

  - name: "promotional_methods"
    type: "string"
    description: ""

  - name: "rating"
    type: "integer"
    description: ""

  - name: "relationship_state"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""

  - name: "website"
    type: "string"
    description: ""
---