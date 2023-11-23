---
tap: "google-ads"
version: "1"
name: "call_details"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/CallView
description: |
  The `{{ table.name }}` table contains info about call tracking of call-only ads or call extensions.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "ad_group_id"
    type: "integer"
    description: ""
  - name: "campaign_id"
    type: "integer"
    description: ""
  - name: "customer_id"
    type: "integer"
    description: ""  
  - name: "resource_name"
    type: "string"
    description: ""
    primary-key: true
  - name: "caller_country_code"
    type: "string"
    description: ""  
  - name: "caller_area_code"
    type: "string"
    description: ""  
  - name: "call_duration_seconds"
    type: "integer"
    description: ""  
  - name: "start_call_date_time"
    type: "string"
    description: ""  
  - name: "end_call_date_time"
    type: "string"
    description: ""  
  - name: "call_tracking_display_location"
    type: "string"
    description: ""  
  - name: "type"
    type: "string"
    description: ""  
  - name: "call_status"
    type: "string"
    description: ""  
---
