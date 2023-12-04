---
tap: "adroll"
version: "1"
key: "ad-group"

name: "ad_groups"
doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-adgroup-get"
singer-schema: "https://github.com/singer-io/tap-adroll/blob/master/tap_adroll/schemas/ad_groups.json"
description: |
  The `{{ table.name }}` table contains info about the adgroups contained within the campaigns of your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get advertisable adgroup"
  doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_adgroups"

attributes:
  - name: "eid"
    type: "string"
    primary-key: true
    description: "The ad group EID."
    foreign-key-id: "adgroup-id"

  - name: "ad_optimization"
    type: "string"
    description: ""

  - name: "ads"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "ad-id"

      - name: "status"
        type: "string"
        description: ""

  - name: "campaign"
    type: "string"
    description: ""

  - name: "coops"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "demographic_targets"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  
  - name: "flight_timezone"
    type: "string"
    description: ""

  - name: "geo_targets"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "is_cats4gold"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "placement_targets"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "platform_targets"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "segments"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "segment-id"

      - name: "is_negative"
        type: "boolean"
        description: ""

  - name: "site_exclusions"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "space_optimization"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "updated_date"
    type: "date-time"
    description: ""
---