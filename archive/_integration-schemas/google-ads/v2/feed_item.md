---
tap: "google-ads"
version: "1"
name: "feed_item"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/FeedItem
description: |
  The `{{ table.name }}` table contains infor about a feed item.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "customer_id"
    type: "integer"
    description: ""

  - name: "feed_id"
    type: "integer"
    description: ""

  - name: "id"
    type: "integer"
    description: ""
    primary-key: true

  - name: "resource_name"
    type: "string"
    description: ""

  - name: "attribute_values"
    type: "array"
    description: ""
    subattributes:
      - name: "attribute_value"
        type: "object"
        description: ""
        subattributes: 
          - name: "price_value"
            type: "object"
            description: ""
            subattributes:
              - name: "currency-code"
                type: "string"
                description: ""

              - name: "amount_micros"
                type: "integer"
                description: ""
            
          - name: "integer_values"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "integer"
                description: ""
            
          - name: "boolean_values"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "boolean"
                description: ""
            
          - name: "string_values"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
            
          - name: "double_values"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "double"
                description: ""
            
          - name: "feed_attribute_id"
            type: "integer"
            description: ""
            
          - name: "integer_value"
            type: "integer"
            description: ""
            
          - name: "boolean_value"
            type: "boolean"
            description: ""
            
          - name: "string_value"
            type: "string"
            description: ""
            
          - name: "double_value"
            type: "double"
            description: ""

  - name: "geo_targeting_restriction"
    type: "string"
    description: ""

  - name: "url_custom_parameters"
    type: "array"
    description: ""
    subattributes:
      - name: "parameter"
        type: "object"
        description: ""
        subattributes:
          - name: "key"
            type: "string"
            description: ""
            
          - name: "value"
            type: "string"
            description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "policy_infos"
    type: "array"
    description: ""
    subattributes:
      - name: "info"
        type: "object"
        description: ""
        subattributes:
          - name: "placeholder_type_enum"
            type: "string"
            description: ""
            
          - name: "review_status"
            type: "string"
            description: ""
            
          - name: "approval_status"
            type: "string"
            description: ""
            
          - name: "policy_topic_entries"
            type: "array"
            description: ""
            subattributes:
              - name: "entry"
                type: "object"
                description: ""
                subattributes:
                  - name: "type"
                    type: "string"
                    description: ""
                    
                  - name: "evidences"
                    type: "array"
                    description: ""
                    subattributes:
                      - name: "value"
                        type: "object"
                        description: "Additional information that explains a policy finding. It is one of the objects listed under value in the [Google Ads API documentation](https://developers.google.com/google-ads/api/reference/rpc/v12/PolicyTopicEvidence#value)."
                    
                  - name: "constraints"
                    type: "array"
                    description: ""
                    subattributes:
                      - name: "value"
                        type: "object"
                        description: "Describes the effect on serving that a policy topic entry will have. It is one of the objects listed under value in the [Google Ads API documentation](https://developers.google.com/google-ads/api/reference/rpc/v12/PolicyTopicConstraint#value)."
                    
                  - name: "topic"
                    type: "string"
                    description: ""
            
          - name: "validation_status"
            type: "string"
            description: ""
            
          - name: "validation_errors"
            type: "array"
            description: ""
            subattributes:
              - name: "error"
                type: "object"
                description: ""
                subattributes:
                  - name: "validation_error"
                    type: "string"
                    description: ""

                  - name: "feed_attribute_ids"
                    type: "array"
                    description: ""
                    subattributes:
                      - name: "id"
                        type: "integer"
                        description: ""

                  - name: "description"
                    type: "string"
                    description: ""

                  - name: "extra_info"
                    type: "string"
                    description: ""
            
          - name: "quality_approval_status"
            type: "string"
            description: ""
            
          - name: "quality_disapproval_reasons"
            type: "array"
            description: ""
            subattributes:
              - name: "reason"
                type: "string"
                description: ""
            
          - name: "feed_mapping_resource_name"
            type: "string"
            description: ""

  - name: "feed"
    type: "string"
    description: ""

  - name: "start_date_time"
    type: "string"
    description: ""

  - name: "end_date_time"
    type: "string"
    description: ""

---