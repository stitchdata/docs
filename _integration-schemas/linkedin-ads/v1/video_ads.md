---
tap: "linkedin-ads"
version: "1.0"

name: "video_ads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/video_ads.json"
description: ""

replication-method: "Key-based Incremental"


api-method:
    name: "Video Ads"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/create-and-manage-video#finders"

attributes:
  - name: "content_reference"
    type: "string"
    primary-key: true
    description: "The content URN. This supports 'UserGeneratedContentPostUrn'."
    foreign-key-id: "content-reference"

  - name: "last_modified_time"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "account"
    type: "string"
    description: "The create-only field to associate an adAccount."
  
  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"
  
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
  
  - name: "content_reference_share_id"
    type: "integer"
    description: ""
  
  - name: "content_reference_ucg_post_id"
    type: "integer"
    description: ""
  
  - name: "created_time"
    type: "date-time"
    description: "The time the video ad was created."
  
  - name: "name"
    type: "string"
    description: "Name of the 'adDirectSponsoredContents'."
  
  - name: "owner"
    type: "string"
    description: "The owner of the organization. This field can be experessed as a URN as well."
  
  - name: "owner_organization_id"
    type: "integer"
    description: ""
    foreign-key-id: "owner-organization-id"
  
  - name: "type"
    type: "string"
    description: "The type of content - in this case, the only possible value will be 'video'."
---
