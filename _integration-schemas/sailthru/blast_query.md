---
tap: "sailthru"
version: "0.2"
key: ""

name: "blast_query"
doc-link: "https://getstarted.sailthru.com/developers/api/job/#blast-query"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/blast_query.json"
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
    #foreign-key-id: "blast-id"

  - name: "profile_id"
    type: "string"
    primary-key: true
    description: "The profile ID."
    #foreign-key-id: "profile-id" 

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
    type: "string"
    description: ""
  - name: "first_ten_clicks_time"
    type: "date-time"
    description: ""
  - name: "open_time"
    type: "date-time"
    description: ""
  
  - name: "purchase_time"
    type: "date-time"
    description: ""
  - name: "send_time"
    type: "date-time"
    description: ""
---
