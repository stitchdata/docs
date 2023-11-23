---
tap: "adroll"
version: "1"
key: "segment"

name: "segments"
doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-segment-get"
singer-schema: "https://github.com/singer-io/tap-adroll/blob/master/tap_adroll/schemas/segments.json"
description: |
  The `{{ table.name }}` table contains information about segments, or the lists of users that visit your {{ integration.display_name }} site.

replication-method: "Full Table"

api-method:
  name: "Get advertisable segments"
  doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_segments"

attributes:
  - name: "eid"
    type: "string"
    primary-key: true
    description: "The segment EID."
    foreign-key-id: "segment-id"
    
  - name: "advertisable_eid"
    type: "string"
    description: ""
    foreign-key-id: "advertisable-id"

  - name: "conversion_value"
    type: "string"
    description: ""

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "duration_sec"
    type: "integer"
    description: ""
  
  - name: "group"
    type: "integer"
    description: ""

  - name: "has_default_rule"
    type: "boolean"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "match_method"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "string"
    description: ""

  - name: "pattern"
    type: "string"
    description: ""

  - name: "recent_first_match"
    type: "boolean"
    description: ""

  - name: "rule"
    type: "string"
    description: ""

  - name: "rule_id"
    type: "integer"
    description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "threshold"
    type: "integer"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---