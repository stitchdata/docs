---
tap: "impact"
version: "1"
key: "media-partner-group"

name: "media_partner_groups"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/media_partner_groups.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's media partner groups.

replication-method: "Full Table"

api-method:
  name: "Get media partner groups"
  doc-link: "https://developer.impact.com/default#operations-Partner_Groups-GetMediaPartnerGroups"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "media-partner-group-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "media_partners"
    type: "array"
    description: ""
    subattributes:
      - name: "partner_id"
        type: "integer"
        description: ""
        foreign-key-id: "media-partner-id"

      - name: "partner_name"
        type: "string"
        description: ""

      - name: "partner_uri"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---