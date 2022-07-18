---
tap: "google-ads"
version: "1"
name: "user_list"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/UserList
dependent-on: "campaign_criterion|ad_group_criterion"
description: |
  The `{{ table.name }}` table contains info about lists of user that can be targeted.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the following streams:

  {% assign dependents = table.dependent-on | split: "|" %}
  
  {% for dependent in dependents %}
  - [`{{ dependent }}`](#{{ dependent | replace:'_','-'}})
  {% endfor %}

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    
  - name: "customer_id"
    type: "integer"
    description: ""
    
  - name: "resource_name"
    type: "string"
    description: ""
    
  - name: "membership_status"
    type: "string"
    description: ""
    
  - name: "size_range_for_display"
    type: "string"
    description: ""
    
  - name: "size_range_for_search"
    type: "string"
    description: ""
    
  - name: "type"
    type: "string"
    description: ""
    
  - name: "closing_reason"
    type: "string"
    description: ""
    
  - name: "access_reason"
    type: "string"
    description: ""
    
  - name: "account_user_list_status"
    type: "string"
    description: ""
    
  - name: "read_only"
    type: "boolean"
    description: ""
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "description"
    type: "string"
    description: ""
    
  - name: "integration_code"
    type: "string"
    description: ""
    
  - name: "membership_life_span"
    type: "integer"
    description: ""
    
  - name: "size_for_display"
    type: "integer"
    description: ""
    
  - name: "size_for_search"
    type: "integer"
    description: ""
    
  - name: "eligible_for_search"
    type: "boolean"
    description: ""
    
  - name: "eligible_for_display"
    type: "boolean"
    description: ""
    
  - name: "match_rate_percentage"
    type: "integer"
    description: ""
    
  - name: "user_list"
    type: "object"
    description: "The user list. It is one of the objects listed under user_list in the [Google Ads API documentation](https://developers.google.com/google-ads/api/reference/rpc/v10/UserList#user_list)."

---