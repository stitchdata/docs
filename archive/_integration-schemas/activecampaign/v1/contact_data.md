---
tap: "activecampaign"
version: "1"
key: ""

name: "contact_data"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_data.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact datapoint ID."
    #foreign-key-id: "contact-data-id"

  - name: "tstamp"
    type: "date-time"
    description: "The time the contact data timestamp."
    replication-key: true

  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "fb_id"
    type: "integer"
    description: ""
  - name: "fb_name"
    type: "string"
    description: ""
  - name: "ga_campaign_content"
    type: "string"
    description: ""
  - name: "ga_campaign_customsegment"
    type: "string"
    description: ""
  - name: "ga_campaign_medium"
    type: "string"
    description: ""
  - name: "ga_campaign_name"
    type: "string"
    description: ""
  - name: "ga_campaign_source"
    type: "string"
    description: ""
  - name: "ga_campaign_term"
    type: "string"
    description: ""
  - name: "ga_first_visit"
    type: "string"
    description: ""
  - name: "ga_times_visited"
    type: "integer"
    description: ""
  - name: "geo_area"
    type: "string"
    description: ""
  - name: "geo_city"
    type: "string"
    description: ""
  - name: "geo_country"
    type: "string"
    description: ""
  - name: "geo_country2"
    type: "string"
    description: ""
  - name: "geo_ip4"
    type: "string"
    description: ""
  - name: "geo_lat"
    type: "string"
    description: ""
  - name: "geo_lon"
    type: "string"
    description: ""
  - name: "geo_state"
    type: "string"
    description: ""
  - name: "geo_tstamp"
    type: "date-time"
    description: ""
  - name: "geo_tz"
    type: "string"
    description: ""
  - name: "geo_tz_offset"
    type: "string"
    description: ""
  - name: "geo_zip"
    type: "string"
    description: ""
  
  - name: "tw_id"
    type: "integer"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""
  - name: "updated_timestamp"
    type: "date-time"
    description: ""
---