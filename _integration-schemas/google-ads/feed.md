---
tap: "google-ads"
version: "1"
name: "feed"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/Feed
dependent-on: "campaign_criterion"
description: |
  The `{{ table.name }}` table contains info about feeds.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the [`{{ table.dependent-on }}`](#{{ table.dependent-on }}) stream.

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
    
  - name: "attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "attribute"
        type: "object"
        description: ""
        subattributes:
          - name: "type"
            type: "string"
            description: ""
            
          - name: "id"
            type: "integer"
            description: ""
            
          - name: "name"
            type: "string"
            description: ""
            
          - name: "is_part_of_key"
            type: "boolean"
            description: ""

  - name: "attribute_operations"
    type: "array"
    description: ""
    subattributes:
      - name: "operation"
        type: "object"
        description: ""
        subattributes:
          - name: "operator"
            type: "string"
            description: ""
            
          - name: "value"
            type: "object"
            description: ""
            subattributes:
              - name: "type"
                type: "string"
                description: ""
                
              - name: "id"
                type: "integer"
                description: ""
                
              - name: "name"
                type: "string"
                description: ""
                
              - name: "is_part_of_key"
                type: "boolean"
                description: ""
    
  - name: "origin"
    type: ""
    description: ""
    
  - name: "status"
    type: "string"
    description: ""
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "system_feed_generation_data"
    type: "object"
    description: "The system data for the feed. It is one of the objects listed under system_feed_generation_data in the [Google Ads API documentation](https://developers.google.com/google-ads/api/reference/rpc/v10/Feed#system_feed_generation_data)."

---