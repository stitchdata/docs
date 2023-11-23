---
tap: "lookml"
version: "1"
key: "model"

name: "models"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-lookml/blob/master/tap_lookml/schemas/models.json"
description: |
  The `{{ table.name }}` table contains information about the model file parse items in your GitHub account using the `lkml` filter.

replication-method: "Full Table"

api-method:
    name: "Git API Search"
    doc-link: "https://docs.github.com/en/rest/reference/search#search-code"

attributes:
  - name: "git_owner"
    type: "string"
    primary-key: true
    description: "The owner of the GitHub repository."
  
  - name: "git_repository"
    type: "string"
    primary-key: true
    description: "The GitHub repository."

  - name: "path"
    type: "string"
    primary-key: true
    description: "The URL for the repository."  

  - name: "access_grants"
    type: "array"
    description: ""
    subattributes:
      - name: "allowed_values"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "user_attribute"
        type: "string"
        description: ""
        
  - name: "case_sensitive"
    type: "string"
    description: ""
    
  - name: "connection"
    type: "string"
    description: ""
    
  - name: "datagroups"
    type: "array"
    description: ""
    subattributes:
      - name: "max_cache_age"
        type: "string"
        description: ""
        
      - name: "name"
        type: "string"
        description: ""
        
      - name: "sql_trigger"
        type: "string"
        description: ""
        
  - name: "explores"
    type: "array"
    description: ""
    subattributes:
      - name: "access_filters"
        type: "array"
        description: ""
        subattributes:
          - name: "field"
            type: "string"
            description: ""
            
          - name: "user_attribute"
            type: "string"
            description: ""
            
      - name: "always_filter"
        type: "object"
        description: ""
        subattributes:
          - name: "filters"
            type: "array"
            description: ""
            subattributes:
              - name: "field"
                type: "string"
                description: ""
                
              - name: "value"
                type: "string"
                description: ""
                
      - name: "always_join"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            
      - name: "cancel_grouping_fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            
      - name: "case_sensitive"
        type: "string"
        description: ""
        
      - name: "conditionally_filter"
        type: "object"
        description: ""
        subattributes:
          - name: "filters"
            type: "array"
            description: ""
            subattributes:
              - name: "field"
                type: "string"
                description: ""
                
              - name: "value"
                type: "string"
                description: ""
                
          - name: "unless"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
                
      - name: "description"
        type: "string"
        description: ""
        
      - name: "extends"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            
      - name: "extension"
        type: "string"
        description: ""
        
      - name: "fields"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            
      - name: "from"
        type: "string"
        description: ""
        
      - name: "group_label"
        type: "string"
        description: ""
        
      - name: "hidden"
        type: "string"
        description: ""
        
      - name: "joins"
        type: "array"
        description: ""
        subattributes:
          - name: "fields"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
                
          - name: "foreign_key"
            type: "string"
            description: ""
            
          - name: "from"
            type: "string"
            description: ""
            
          - name: "name"
            type: "string"
            description: ""
            
          - name: "outer_only"
            type: "string"
            description: ""
            
          - name: "relationship"
            type: "string"
            description: ""
            
          - name: "required_access_grants"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
                
          - name: "required_joins"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
                
          - name: "sql_foreign_key"
            type: "string"
            description: ""
            
          - name: "sql_on"
            type: "string"
            description: ""
            
          - name: "sql_table_name"
            type: "string"
            description: ""
            
          - name: "sql_where"
            type: "string"
            description: ""
            
          - name: "type"
            type: "string"
            description: ""
            
          - name: "view_label"
            type: "string"
            description: ""
            
      - name: "label"
        type: "string"
        description: ""
        
      - name: "name"
        type: "string"
        description: ""
        
      - name: "persist_for"
        type: "string"
        description: ""
        
      - name: "persist_with"
        type: "string"
        description: ""
        
      - name: "required_access_grants"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
            
      - name: "sql_always_having"
        type: "string"
        description: ""
        
      - name: "sql_always_where"
        type: "string"
        description: ""
        
      - name: "sql_table_name"
        type: "string"
        description: ""
        
      - name: "symmetric_aggregates"
        type: "string"
        description: ""
        
      - name: "view_label"
        type: "string"
        description: ""
        
      - name: "view_name"
        type: "string"
        description: ""
        
  - name: "fiscal_month_offset"
    type: "string"
    description: ""
  
  - name: "includes"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        
  - name: "label"
    type: "string"
    description: ""
    
  - name: "last_modified"
    type: "date-time"
    description: ""
    
  - name: "map_layers"
    type: "array"
    description: ""
    subattributes:
      - name: "extents_json_url"
        type: "string"
        description: ""
        
      - name: "feature_key"
        type: "string"
        description: ""
        
      - name: "file"
        type: "string"
        description: ""
        
      - name: "format"
        type: "string"
        description: ""
        
      - name: "label"
        type: "string"
        description: ""
        
      - name: "max_zoom_level"
        type: "integer"
        description: ""
        
      - name: "min_zoom_level"
        type: "integer"
        description: ""
        
      - name: "name"
        type: "string"
        description: ""
        
      - name: "projection"
        type: "string"
        description: ""
        
      - name: "property_key"
        type: "string"
        description: ""
        
      - name: "property_label_key"
        type: "string"
        description: ""
        
      - name: "url"
        type: "string"
        description: ""
        
  - name: "named_value_formats"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""
        
      - name: "strict_value_format"
        type: "string"
        description: ""
        
      - name: "value_format"
        type: "string"
        description: ""
  
  - name: "persist_for"
    type: "string"
    description: ""
    
  - name: "persist_with"
    type: "string"
    description: ""
    
  - name: "sha"
    type: "string"
    description: ""
    
  - name: "week_start_day"
    type: "string"
    description: ""
---
