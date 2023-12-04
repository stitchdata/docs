---
tap: "sailthru"
version: "1"
key: ""

name: "blast_query"
doc-link: "https://getstarted.sailthru.com/developers/api/job/#blast-query"
singer-schema: "https://github.com/singer-io/tap-sailthru/tree/master/tap_sailthru/schemas/blast_query.json"
description: |
  The `{{ table.name }}` table contains information from blast query jobs in your {{ integration.display_name }} account. This is a child table of `blasts`.

replication-method: "Full Table"

api-method:
    name: "get BlastQuery"
    doc-link: "https://getstarted.sailthru.com/developers/api/job/#blast-query"

attributes:
  - name: "blast_id"
    type: "integer"
    primary-key: true
    description: "The blast ID."

  - name: "profile_id"
    type: "string"
    primary-key: true
    description: "The profile ID."

  - name: "click_time"
    type: "date-time"
    description: ""

  - name: "device"
    type: "string"
    description: ""

  - name: "email_hash"
    type: "string"
    description: ""

  - name: "first_ten_clicks"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "first_ten_clicks_time"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "purchase_time"
    type: "date-time"
    description: ""
    
  - name: "send_time"
    type: "date-time"
    description: ""
---
