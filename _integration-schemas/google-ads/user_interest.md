---
tap: "google-ads"
version: "1"
name: "user_interest"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/UserInterest
dependent-on: "campaign_criterion|ad_group_criterion"
description: |
  The `{{ table.name }}` table contains info about user interests to be targeted.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the following streams:

  {% assign dependents = table.dependent-on | split: "|" %}
  
  {% for dependent in dependents %}
  - [`{{ dependent }}`](#{{ dependent | replace:'_','-'}})
  {% endfor %}

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""
    
  - name: "taxonomy_type"
    type: "string"
    description: ""
    
  - name: "availabilities"
    type: "array"
    description: ""
    subattributes:
      - name: "availability"
        type: "object"
        description: ""
        subattributes:
          - name: "channel"
            type: "object"
            description: ""
            subattributes:
              - name: "availability_mode"
                type: "string"
                description: ""
                
              - name: "advertising_channel_type"
                type: "string"
                description: ""
                
              - name: "advertising_channel_sub_type"
                type: "array"
                description: ""
                subattributes:
                  - name: "type"
                    type: "string"
                    description: ""

              - name: "include_default_channel_sub_type"
                type: "boolean"
                description: ""
            
          - name: "locale"
            type: "array"
            description: ""
            subattributes:
              - name: "item"
                type: "object"
                description: ""
                subattributes:
                  - name: "availability_mode"
                    type: "string"
                    description: ""
                    
                  - name: "country_code"
                    type: "string"
                    description: ""
                    
                  - name: "language_code"
                    type: "string"
                    description: ""
    
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "user_interest_parent"
    type: "string"
    description: ""
    
  - name: "launched_to_all"
    type: "boolean"
    description: ""

---