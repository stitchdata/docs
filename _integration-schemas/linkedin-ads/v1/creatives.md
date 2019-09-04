---
tap: "linkedin-ads"
version: "1.0"

name: "creatives"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/creatives.json"
description: ""

replication-method: "Key-based Incremental"


api-method:
    name: "Create and Manage Creatives"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-creatives#search-for-creatives"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
  
  - name: "last_modified_time"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "campaign"
    type: "string"
    description: "The URN identifying the campaign associated with the creative."
  
  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"
  
  - name: "change_audit_stamps"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "object"
        description: ""
        subattributes:
          - name: "time"
            type: "date-time"
            description: ""
      - name: "last_modified"
        type: "object"
        description: ""
        subattributes:
          - name: "time"
            type: "date-time"
            description: ""
  
  - name: "created_time"
    type: "date-time"
    description: ""
  
  - name: "reference"
    type: "string"
    description: "A reference URN for this object to an external system, with semantics varying based on the creative type."
  
  - name: "reference_share_id"
    type: "integer"
    description: ""
  
  - name: "review"
    type: "object"
    description: ""
    subattributes:
      - name: "review_status"
        type: "string"
        description: "The review status of the Ad entity."
  
  - name: "status"
    type: "string"
    description: "The status of the creative."
  
  - name: "type"
    type: "string"
    description: "The type of creative."
  
  - name: "variables"
    type: "object"
    description: "Variables for rendering the creative."
    subattributes:
      - name: "click_uri"
        type: "string"
        description: "Required when creative type is 'TEXT_AD'. Maximum character limit of 500 after URL encoding all special characters. Limit does not include the 'https://' prefix."
      - name: "type"
        type: "string"
        description: ""
      - name: "values"
        type: "null"
        description: ""
  
  - name: "version"
    type: "object"
    description: ""
    subattributes:
      - name: "version_tag"
        type: "string"
        description: ""
---
