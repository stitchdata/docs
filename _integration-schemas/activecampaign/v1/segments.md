---
tap: "activecampaign"
version: "0.3"
key: ""

name: "segments"
doc-link: "https://developers.activecampaign.com/reference#segments"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/segments.json"
description: |
  The `{{ table.name }}` table contains information about targeted groups of contacts that meet specified criteria in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all segments"
    doc-link: "https://developers.activecampaign.com/reference#list-all-segments"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The segment ID."
    #foreign-key-id: "segment-id"

  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "hidden"
    type: "integer"
    description: ""
  
  - name: "logic"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "seriesid"
    type: "integer"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""
  - name: "updated_timestamp"
    type: "date-time"
    description: ""
---
